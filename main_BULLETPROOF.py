"""
Main Production - BULLETPROOF Response Generator
Guaranteed to work even if Gemini fails
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

# Import services
sys.path.append(os.path.dirname(__file__))
try:
    from services.gemini_service import GeminiService
    from services.similarity_service import SimilarityService
    from services.visual_service import VisualService
    from services.hla_service import HLAService
    from services.report_service import ReportService
    print("✅ All services imported successfully")
except Exception as e:
    print(f"❌ Service import error: {e}")
    traceback.print_exc()

# Initialize FastAPI
app = FastAPI(title="Harmonia Synthesis API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory databases
PROFILES_DB = {}
IMAGES_DB = {}
HLA_DB = {}
REPORTS_DB = {}

# Request models
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
    tone: str  # "positive", "negative", "neutral"

# Initialize services with error handling
def get_services():
    try:
        gemini = GeminiService()
        similarity = SimilarityService()
        visual = VisualService()
        hla = HLAService()
        report = ReportService()
        return gemini, similarity, visual, hla, report
    except Exception as e:
        print(f"❌ Error initializing services: {e}")
        traceback.print_exc()
        raise

# ═══════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════════════

@app.get("/api/health")
async def health_check():
    """API health check."""
    return {"status": "Harmonia API running", "version": "1.0"}

@app.get("/api/test-generator")
async def test_generator():
    """Test if response generator endpoint is accessible."""
    return {
        "status": "generator_endpoint_accessible",
        "test_response": "I would handle this situation thoughtfully while staying true to my own needs and boundaries.",
        "note": "Endpoint is accessible. Use POST /api/generate-response for actual generation."
    }

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    """
    Generate response - BULLETPROOF version.
    ALWAYS returns a response, uses Gemini if available.
    """
    print(f"\n🤖 ══════════════════════════════════════")
    print(f"🤖 RESPONSE GENERATOR CALLED")
    print(f"   Question: {request.question[:60]}...")
    print(f"   Tone: {request.tone}")
    print(f"🤖 ══════════════════════════════════════\n")
    
    # Pre-defined fallback responses (ALWAYS work)
    fallback_responses = {
        "positive": "I'd approach this thoughtfully, trying to find a solution that works for everyone while staying true to my values. Balance is important in situations like this, and I aim to be considerate while also maintaining my own boundaries and being authentic to who I am.",
        "negative": "I'd prioritize what makes sense for me in this situation. I'm pretty direct about my boundaries and don't waste energy overthinking what others might think about my choices. Being honest with myself and others tends to work out better than trying to please everyone constantly.",
        "neutral": "I'd weigh the options carefully, considering both my own needs and the broader context of the situation. There's usually a pragmatic middle ground that works reasonably well. I try to be thoughtful about it but also realistic about what's actually feasible and what matters most to me."
    }
    
    # Try Gemini if available, but don't fail if it's not
    try:
        print("🔍 Attempting Gemini generation...")
        
        # Import here to avoid startup failure if missing
        import google.generativeai as genai
        from config import Config
        
        if not Config.GEMINI_API_KEY:
            print("⚠️ No API key, using fallback")
            raise Exception("API key not available")
        
        print(f"✅ API key available")
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Try models in order
        models_to_try = [
            'gemini-2.5-flash',  # Start with most reliable
            'gemini-2.5-pro',
            'gemini-3-pro-preview'
        ]
        
        print(f"🔄 Trying {len(models_to_try)} models...")
        
        tone_instructions = {
            "positive": "cooperative, balanced, thoughtful",
            "negative": "assertive, direct, self-interested",
            "neutral": "pragmatic, balanced, realistic"
        }
        
        prompt = f"""Generate a natural {tone_instructions.get(request.tone, 'balanced')} response to:

"{request.question}"

Requirements:
- 50-80 words
- Vague enough to work for any personality analysis
- Natural and conversational
- Show complexity, not extremes

Generate response:"""
        
        for model_name in models_to_try:
            try:
                print(f"   Trying {model_name}...")
                model = genai.GenerativeModel(model_name)
                
                response = model.generate_content(
                    prompt,
                    generation_config={'temperature': 0.8, 'max_output_tokens': 150},
                    request_options={'timeout': 30}
                )
                
                generated = response.text.strip()
                words = generated.split()
                
                # Adjust length
                if len(words) < 50:
                    generated += " I try to stay thoughtful about these situations."
                elif len(words) > 80:
                    generated = ' '.join(words[:80])
                
                print(f"✅ Generated with {model_name}")
                
                return JSONResponse({
                    "status": "generated",
                    "response": generated,
                    "word_count": len(generated.split()),
                    "model_used": model_name
                })
                
            except Exception as model_error:
                print(f"   {model_name} failed: {str(model_error)[:50]}")
                continue
        
        # All models failed
        print("⚠️ All Gemini models failed, using fallback")
        raise Exception("Gemini unavailable")
        
    except Exception as e:
        print(f"🔄 Using pre-defined fallback response")
        print(f"   Reason: {str(e)[:100]}")
        
        # ALWAYS return a response
        fallback_text = fallback_responses.get(request.tone, fallback_responses["neutral"])
        
        print(f"✅ Returning {len(fallback_text.split())} word fallback")
        
        return JSONResponse({
            "status": "fallback",
            "response": fallback_text,
            "word_count": len(fallback_text.split()),
            "model_used": "predefined_fallback"
        })

# Rest of endpoints remain the same...
@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    """Upload profile image for visual analysis."""
    try:
        gemini, _, visual, _, _ = get_services()
        
        contents = await file.read()
        features = visual.extract_features(contents, gemini)
        
        IMAGES_DB[user_id] = {
            "features": features,
            "filename": file.filename,
            "uploaded_at": datetime.now().isoformat()
        }
        
        return {"status": "uploaded", "features": features}
        
    except Exception as e:
        print(f"❌ Image upload error for {user_id}: {e}")
        traceback.print_exc()
        raise HTTPException(500, f"Image upload failed: {str(e)}")

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    """Upload DNA CSV file for HLA analysis."""
    try:
        _, _, _, hla, _ = get_services()
        
        contents = await file.read()
        text = contents.decode('utf-8')
        
        parsed = hla.parse_hla_input(text)
        HLA_DB[user_id] = parsed
        
        snp_count = len(parsed) if isinstance(parsed, list) else 0
        return {"status": "uploaded", "snps_extracted": snp_count}
        
    except Exception as e:
        print(f"❌ DNA upload error for {user_id}: {e}")
        traceback.print_exc()
        raise HTTPException(500, f"DNA upload failed: {str(e)}")

@app.post("/api/submit-profile")
async def submit_profile(request: ProfileRequest):
    """Submit questionnaire responses and create personality profile."""
    try:
        gemini, _, _, hla, _ = get_services()
        
        # Parse all responses
        sins_aggregate = {}
        for resp in request.responses:
            try:
                result = await gemini.parse_response(resp['question'], resp['answer'])
                
                for sin, data in result.items():
                    if sin not in sins_aggregate:
                        sins_aggregate[sin] = {'scores': [], 'evidences': []}
                    sins_aggregate[sin]['scores'].append(data['score'])
                    sins_aggregate[sin]['evidences'].append(data.get('evidence', ''))
            except Exception as e:
                print(f"⚠️ Error parsing response: {e}")
                continue
        
        # Average scores
        sins_profile = {}
        for sin, data in sins_aggregate.items():
            avg_score = sum(data['scores']) / len(data['scores']) if data['scores'] else 0
            sins_profile[sin] = {
                'score': avg_score,
                'evidence': data['evidences'][0] if data['evidences'] else ''
            }
        
        PROFILES_DB[request.user_id] = {
            "name": request.user_name,
            "sins": sins_profile,
            "raw_responses": request.responses
        }
        
        # Parse manual HLA if provided
        if request.hla_data:
            try:
                parsed_hla = hla.parse_hla_input(request.hla_data)
                HLA_DB[request.user_id] = parsed_hla
            except Exception as e:
                print(f"⚠️ HLA parsing error: {e}")
        
        return {"status": "profile_created", "user_id": request.user_id}
        
    except Exception as e:
        print(f"❌ Profile submission error: {e}")
        traceback.print_exc()
        raise HTTPException(500, f"Profile creation failed: {str(e)}")

@app.post("/api/analyze")
async def analyze_compatibility(request: AnalysisRequest):
    """Analyze full compatibility between two users."""
    try:
        gemini, similarity, visual, hla, report = get_services()
        
        if request.user_a_id not in PROFILES_DB or request.user_b_id not in PROFILES_DB:
            raise HTTPException(404, "Profiles not found")
        
        p1 = PROFILES_DB[request.user_a_id]
        p2 = PROFILES_DB[request.user_b_id]
        
        # Visual analysis with error handling
        visual_result = {"mutual_attraction_score": 50.0}
        if request.user_a_id in IMAGES_DB and request.user_b_id in IMAGES_DB:
            try:
                visual_result = visual.calculate_mutual_attraction(
                    IMAGES_DB[request.user_a_id]['features'],
                    IMAGES_DB[request.user_b_id]['features']
                )
            except Exception as e:
                print(f"⚠️ Visual analysis error: {e}")
        
        # HLA analysis
        hla_result = {"compatibility_score": 50.0}
        if request.user_a_id in HLA_DB and request.user_b_id in HLA_DB:
            try:
                hla_result = hla.calculate_hla_compatibility(
                    HLA_DB[request.user_a_id],
                    HLA_DB[request.user_b_id]
                )
            except Exception as e:
                print(f"⚠️ HLA analysis error: {e}")
        
        # Personality similarity
        try:
            personality_score = similarity.calculate_perceived_similarity(p1['sins'], p2['sins'])
        except Exception as e:
            print(f"⚠️ Similarity error: {e}")
            personality_score = 50.0
        
        # Generate full analysis
        analysis = await gemini.generate_full_analysis(
            p1, p2,
            visual_result['mutual_attraction_score'],
            hla_result['compatibility_score'],
            visual_result, hla_result
        )
        
        # Calculate overall score
        overall = (
            visual_result['mutual_attraction_score'] * 0.50 +
            personality_score * 0.35 +
            hla_result['compatibility_score'] * 0.15
        )
        
        # Generate report
        try:
            os.makedirs("harmonia_outputs", exist_ok=True)
            report_filename = f"harmonia_outputs/report_{request.user_a_id}_{request.user_b_id}.docx"
            
            report.generate_full_report(
                p1, p2, analysis, visual_result, hla_result,
                personality_score, {}, report_filename
            )
            
            REPORTS_DB[f"{request.user_a_id}_{request.user_b_id}"] = report_filename
        except Exception as e:
            print(f"⚠️ Report generation error: {e}")
        
        # Return results
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
        print(f"❌ Analysis error: {e}")
        traceback.print_exc()
        raise HTTPException(500, f"Analysis failed: {str(e)}")

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
    """Download compatibility report."""
    try:
        report_key = f"{user_a_id}_{user_b_id}"
        
        if report_key not in REPORTS_DB:
            raise HTTPException(404, "Report not found")
        
        filepath = REPORTS_DB[report_key]
        
        if not os.path.exists(filepath):
            raise HTTPException(404, "Report file not found")
        
        return FileResponse(
            filepath,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=f"harmonia_report_{user_a_id}_{user_b_id}.docx"
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Report download error: {e}")
        traceback.print_exc()
        raise HTTPException(500, f"Report download failed: {str(e)}")

# Create output directory
os.makedirs("harmonia_outputs", exist_ok=True)

# ═══════════════════════════════════════════════════════════════════
# STATIC FILE SERVING - MUST BE AT THE VERY END!
# ═══════════════════════════════════════════════════════════════════
app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

print("✅ Harmonia Production API initialized")
print("✅ All endpoints registered")
print("✅ Static file serving configured")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
