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
    """Generate response - GEMINI 3 PRO FIRST!"""
    print(f"\n🤖 GENERATOR: {request.question[:50]}... (tone: {request.tone})")
    
    # Pre-defined fallbacks (longer, better)
    fallbacks = {
        "positive": "I'd probably approach this situation thoughtfully, trying to find a solution that works for everyone involved while still staying true to my own values and principles. Balance is really important in situations like this, and I genuinely aim to be considerate and understanding of others while also maintaining my own boundaries and being authentic to who I am as a person.",
        "negative": "I'd prioritize what makes sense for me in this situation without overthinking it too much. I'm pretty direct and straightforward about my boundaries and preferences, and I don't waste a lot of energy worrying about what other people might think about my choices. Being honest with myself and others tends to work out better in my experience than constantly trying to please everyone or meet their expectations.",
        "neutral": "I'd take some time to weigh the different options carefully, considering both my own needs and interests as well as the broader context of the situation and how it affects others. There's usually a pragmatic middle ground that works reasonably well for everyone. I try to be genuinely thoughtful and considerate about these things but also realistic and practical about what's actually feasible and what matters most to me personally."
    }
    
    try:
        import google.generativeai as genai
        from config import Config
        
        if not Config.GEMINI_API_KEY:
            raise Exception("No API key")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # CORRECT ORDER: Gemini 3 Pro FIRST!
        models_to_try = [
            'gemini-3-pro-preview',  # FIRST - Most intelligent!
            'gemini-2.5-pro',        # SECOND - Fallback
            'gemini-2.5-flash'       # THIRD - Fast fallback
        ]
        
        tone_instructions = {
            "positive": "cooperative, thoughtful, and considerate while showing healthy self-awareness and appropriate boundaries. Show nuance - not obviously virtuous or preachy.",
            "negative": "assertive, direct, and self-interested while still being reasonable and not cartoonishly selfish. Frame choices as rational self-advocacy.",
            "neutral": "pragmatic and balanced, showing BOTH genuine consideration for others AND clear self-interest. Demonstrate complexity and mixed motivations."
        }
        
        # COMPREHENSIVE PROMPT with strict requirements
        prompt = f"""You are helping a user respond to a personality assessment question. Generate a natural, conversational response.

QUESTION: "{request.question}"

TONE: {tone_instructions.get(request.tone, 'balanced and thoughtful')}

CRITICAL REQUIREMENTS (ALL MUST BE MET):
1. LENGTH: Exactly 50-80 words (count them!)
2. VAGUENESS: Must work for ANY of the seven deadly sins (greed, pride, lust, wrath, gluttony, envy, sloth) - do NOT mention any sin explicitly
3. DEPTH: Show psychological complexity and mixed motivations, not surface-level thinking
4. NATURALNESS: Conversational first-person, not formal or academic
5. AMBIGUITY: Could reflect multiple personality traits - stay interpretable in different ways
6. NO OBVIOUS SIGNALS: Avoid obviously virtuous or vice-filled language
7. NUANCE: Real people have competing values - show internal complexity

EXAMPLE OF GOOD RESPONSE (neutral tone):
"I'd probably take a step back and think through what I actually need from this versus what feels like external pressure or expectations. There's usually some middle ground where I can stay authentic to my own priorities without creating unnecessary conflict or friction with others. I try to be mindful of how my choices affect people, but I'm also pretty realistic about the fact that I can't please everyone all the time, and sometimes I just need to do what makes sense for me even if others might see it differently."

That example shows: complexity, mixed motivations, could relate to various traits, 78 words, vague enough to work for any sin.

NOW GENERATE RESPONSE (50-80 words, vague, deep, nuanced):"""
        
        for model_name in models_to_try:
            try:
                print(f"   Trying {model_name}...")
                model = genai.GenerativeModel(model_name)
                
                # NO request_options!
                response = model.generate_content(
                    prompt,
                    generation_config={
                        'temperature': 0.9,  # Higher for more variation
                        'max_output_tokens': 250,  # Room for longer responses
                        'top_p': 0.95,
                        'top_k': 40
                    }
                )
                
                text = response.text.strip()
                words = text.split()
                word_count = len(words)
                
                print(f"   Generated {word_count} words with {model_name}")
                
                # Enforce word count strictly
                if word_count < 50:
                    text += " I think it's really important to consider all the different angles and perspectives before making any final decisions about how to handle situations like this."
                    words = text.split()
                elif word_count > 80:
                    text = ' '.join(words[:80])
                    words = text.split()
                
                final_count = len(text.split())
                print(f"✅ Final: {final_count} words from {model_name}")
                
                return JSONResponse({
                    "status": "generated",
                    "response": text,
                    "word_count": final_count,
                    "model_used": model_name
                })
                
            except Exception as e:
                print(f"   {model_name} failed: {str(e)[:80]}")
                continue
        
        raise Exception("All models failed")
        
    except Exception as e:
        print(f"🔄 Using fallback: {str(e)[:50]}")
        text = fallbacks.get(request.tone, fallbacks["neutral"])
        return JSONResponse({
            "status": "fallback",
            "response": text,
            "word_count": len(text.split()),
            "model_used": "predefined_fallback"
        })

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
