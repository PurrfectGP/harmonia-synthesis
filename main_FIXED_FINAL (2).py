"""
Harmonia Main - FIXED (NO request_options)
Response generator that ALWAYS works
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional
import os
import sys
import traceback

sys.path.append(os.path.dirname(__file__))
try:
    from services.gemini_service import GeminiService
    from services.similarity_service import SimilarityService
    from services.visual_service import VisualService
    from services.hla_service import HLAService
    from services.report_service import ReportService
    print("✅ All services imported")
except Exception as e:
    print(f"❌ Import error: {e}")
    traceback.print_exc()

app = FastAPI(title="Harmonia API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROFILES_DB = {}
IMAGES_DB = {}
HLA_DB = {}
REPORTS_DB = {}

def get_services():
    try:
        return (GeminiService(), SimilarityService(), VisualService(), HLAService(), ReportService())
    except Exception as e:
        print(f"❌ Service init error: {e}")
        traceback.print_exc()
        raise

class ProfileRequest(BaseModel):
    user_id: str
    user_name: str
    responses: List[Dict]
    hla_data: Optional[str] = ""

class AnalysisRequest(BaseModel):
    user_a_id: str
    user_b_id: str

class ResponseGeneratorRequest(BaseModel):
    question: str
    tone: str

@app.get("/api/health")
async def health():
    return {"status": "Harmonia API running", "version": "1.0"}

@app.get("/api/test-generator")
async def test_gen():
    return {"status": "accessible", "test": "Response generator endpoint works"}

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    """Generate response - ALWAYS works."""
    print(f"\n🤖 GENERATOR: {request.question[:50]}... (tone: {request.tone})")
    
    # Pre-defined fallbacks
    fallbacks = {
        "positive": "I'd approach this thoughtfully, trying to find a solution that works for everyone while staying true to my values. Balance is important in situations like this, and I aim to be considerate while maintaining my own boundaries.",
        "negative": "I'd prioritize what makes sense for me. I'm direct about my boundaries and don't overthink what others might think. Being authentic matters more than pleasing everyone.",
        "neutral": "I'd weigh the options carefully, considering both my needs and the context. There's usually a pragmatic middle ground. I try to be thoughtful but also realistic about what's feasible."
    }
    
    try:
        import google.generativeai as genai
        from config import Config
        
        if not Config.GEMINI_API_KEY:
            raise Exception("No API key")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Try models
        for model_name in ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-3-pro-preview']:
            try:
                print(f"   Trying {model_name}...")
                model = genai.GenerativeModel(model_name)
                
                prompt = f"""Generate vague {request.tone} response to: "{request.question}"

50-80 words, works for ANY personality trait. Be conversational."""
                
                # NO request_options!
                response = model.generate_content(
                    prompt,
                    generation_config={'temperature': 0.8, 'max_output_tokens': 150}
                )
                
                text = response.text.strip()
                words = text.split()
                
                if len(words) < 50:
                    text += " I try to stay thoughtful."
                elif len(words) > 80:
                    text = ' '.join(words[:80])
                
                print(f"✅ Generated with {model_name}")
                return JSONResponse({"status": "generated", "response": text, "word_count": len(text.split())})
                
            except Exception as e:
                print(f"   {model_name} failed: {str(e)[:50]}")
                continue
        
        raise Exception("All models failed")
        
    except Exception as e:
        print(f"🔄 Using fallback: {str(e)[:50]}")
        text = fallbacks.get(request.tone, fallbacks["neutral"])
        return JSONResponse({"status": "fallback", "response": text, "word_count": len(text.split())})

@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    try:
        gemini, _, visual, _, _ = get_services()
        contents = await file.read()
        features = visual.extract_features(contents, gemini)
        IMAGES_DB[user_id] = {"features": features, "filename": file.filename, "uploaded_at": datetime.now().isoformat()}
        return {"status": "uploaded", "features": features}
    except Exception as e:
        print(f"❌ Image upload: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    try:
        _, _, _, hla, _ = get_services()
        contents = await file.read()
        text = contents.decode('utf-8')
        parsed = hla.parse_hla_input(text)
        HLA_DB[user_id] = parsed
        snp_count = len(parsed) if isinstance(parsed, list) else 0
        return {"status": "uploaded", "snps_extracted": snp_count}
    except Exception as e:
        print(f"❌ DNA upload: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

@app.post("/api/submit-profile")
async def submit_profile(request: ProfileRequest):
    try:
        gemini, _, _, hla, _ = get_services()
        sins_aggregate = {}
        
        for resp in request.responses:
            try:
                result = await gemini.parse_response(resp['question'], resp['answer'])
                for sin, data in result.items():
                    if sin not in sins_aggregate:
                        sins_aggregate[sin] = {'scores': [], 'evidences': []}
                    sins_aggregate[sin]['scores'].append(data['score'])
                    sins_aggregate[sin]['evidences'].append(data.get('evidence', ''))
            except:
                continue
        
        sins_profile = {}
        for sin, data in sins_aggregate.items():
            avg = sum(data['scores']) / len(data['scores']) if data['scores'] else 0
            sins_profile[sin] = {'score': avg, 'evidence': data['evidences'][0] if data['evidences'] else ''}
        
        PROFILES_DB[request.user_id] = {"name": request.user_name, "sins": sins_profile, "raw_responses": request.responses}
        
        if request.hla_data:
            try:
                HLA_DB[request.user_id] = hla.parse_hla_input(request.hla_data)
            except:
                pass
        
        return {"status": "profile_created", "user_id": request.user_id}
    except Exception as e:
        print(f"❌ Profile: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

@app.post("/api/analyze")
async def analyze_compatibility(request: AnalysisRequest):
    try:
        gemini, similarity, visual, hla, report = get_services()
        
        if request.user_a_id not in PROFILES_DB or request.user_b_id not in PROFILES_DB:
            raise HTTPException(404, "Profiles not found")
        
        p1 = PROFILES_DB[request.user_a_id]
        p2 = PROFILES_DB[request.user_b_id]
        
        visual_result = {"mutual_attraction_score": 50.0}
        if request.user_a_id in IMAGES_DB and request.user_b_id in IMAGES_DB:
            try:
                visual_result = visual.calculate_mutual_attraction(IMAGES_DB[request.user_a_id]['features'], IMAGES_DB[request.user_b_id]['features'])
            except:
                pass
        
        hla_result = {"compatibility_score": 50.0}
        if request.user_a_id in HLA_DB and request.user_b_id in HLA_DB:
            try:
                hla_result = hla.calculate_hla_compatibility(HLA_DB[request.user_a_id], HLA_DB[request.user_b_id])
            except:
                pass
        
        try:
            personality_score = similarity.calculate_perceived_similarity(p1['sins'], p2['sins'])
        except:
            personality_score = 50.0
        
        analysis = await gemini.generate_full_analysis(p1, p2, visual_result['mutual_attraction_score'], hla_result['compatibility_score'], visual_result, hla_result)
        
        overall = (visual_result['mutual_attraction_score'] * 0.50 + personality_score * 0.35 + hla_result['compatibility_score'] * 0.15)
        
        try:
            os.makedirs("harmonia_outputs", exist_ok=True)
            report_filename = f"harmonia_outputs/report_{request.user_a_id}_{request.user_b_id}.docx"
            report.generate_full_report(p1, p2, analysis, visual_result, hla_result, personality_score, {}, report_filename)
            REPORTS_DB[f"{request.user_a_id}_{request.user_b_id}"] = report_filename
        except:
            pass
        
        return {
            "overall_score": round(overall, 1),
            "components": {
                "visual": {"score": round(visual_result['mutual_attraction_score'], 1)},
                "personality": {"score": round(personality_score, 1)},
                "hla": {"score": round(hla_result['compatibility_score'], 1)}
            },
            "analysis": analysis,
            "chart_data": {
                "labels": ["Greed", "Pride", "Lust", "Wrath", "Gluttony", "Envy", "Sloth"],
                "p1_name": p1['name'],
                "p2_name": p2['name'],
                "p1_scores": [p1['sins'].get(s, {'score': 0})['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]],
                "p2_scores": [p2['sins'].get(s, {'score': 0})['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]]
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Analysis: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
    try:
        report_key = f"{user_a_id}_{user_b_id}"
        if report_key not in REPORTS_DB:
            raise HTTPException(404, "Report not found")
        filepath = REPORTS_DB[report_key]
        if not os.path.exists(filepath):
            raise HTTPException(404, "File not found")
        return FileResponse(filepath, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=f"harmonia_report_{user_a_id}_{user_b_id}.docx")
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Download: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

os.makedirs("harmonia_outputs", exist_ok=True)

app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

print("✅ Harmonia API initialized - NO request_options errors!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
