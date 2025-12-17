"""
Harmonia Main - ULTIMATE SAFETY FIX
OLD SDK + GEMINI 3 PRO + SAFE WRAPPER + BLOCK_NONE SAFETY
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
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        return (
            GeminiService(),
            SimilarityService(), 
            VisualService(gemini_api_key),
            HLAService(),
            ReportService()
        )
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

def _get_text_from_response(response) -> str:
    """
    EXACT COPY from gemini_service_WORKING.py that WORKS!
    Safely extract text with try/except
    """
    if not response:
        return ""
    
    # Try direct text attribute first (wrapped in try/except!)
    if hasattr(response, 'text'):
        try:
            text = response.text
            if text and isinstance(text, str) and len(text.strip()) > 0:
                return text
        except Exception as e:
            # ValueError "quick accessor requires valid part" happens here!
            print(f"   ⚠️ response.text failed ({type(e).__name__}), using fallback...")
            pass
    
    # Fallback: extract via candidates
    try:
        if hasattr(response, 'candidates') and response.candidates:
            if len(response.candidates) > 0:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content:
                    if hasattr(candidate.content, 'parts') and candidate.content.parts:
                        if len(candidate.content.parts) > 0:
                            part = candidate.content.parts[0]
                            if hasattr(part, 'text'):
                                return part.text
    except Exception:
        pass
    
    return ""

@app.get("/api/health")
async def health():
    return {"status": "Harmonia API running", "version": "1.0"}

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    """
    Generate response - OLD SDK + GEMINI 3 PRO + SAFETY SETTINGS!
    """
    print(f"\n🤖 ═══════════════════════════════════════")
    print(f"🤖 RESPONSE GENERATOR REQUEST")
    print(f"   Question: {request.question[:60]}...")
    print(f"   Tone: {request.tone}")
    print(f"🤖 ═══════════════════════════════════════\n")
    
    # Fallbacks
    fallbacks = {
        "positive": "I'd probably approach this situation thoughtfully, trying to find a solution that works for everyone involved while still staying true to my own values and principles. Balance is really important in situations like this, and I genuinely aim to be considerate and understanding of others while also maintaining my own boundaries and being authentic to who I am as a person.",
        "negative": "I'd prioritize what makes sense for me in this situation without overthinking it too much. I'm pretty direct and straightforward about my boundaries and preferences, and I don't waste a lot of energy worrying about what other people might think about my choices. Being honest with myself and others tends to work out better in my experience than constantly trying to please everyone or meet their expectations.",
        "neutral": "I'd take some time to weigh the different options carefully, considering both my own needs and interests as well as the broader context of the situation and how it affects others. There's usually a pragmatic middle ground that works reasonably well for everyone. I try to be genuinely thoughtful and considerate about these things but also realistic and practical about what's actually feasible and what matters most to me personally."
    }
    
    try:
        import google.generativeai as genai  # OLD SDK!
        
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print("❌ No API key")
            raise Exception("No API key")
        
        print(f"✅ API key available")
        genai.configure(api_key=api_key)
        
        # GEMINI 3 PRO FIRST!
        models_to_try = [
            'gemini-3-pro-preview',
            'gemini-2.5-pro',
            'gemini-2.5-flash'
        ]
        
        print(f"🔄 Will try {len(models_to_try)} models:")
        for i, name in enumerate(models_to_try, 1):
            print(f"   {i}. {name}")
        print()
        
        # SAFETY SETTINGS - BLOCK_NONE for all categories!
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        
        tone_instructions = {
            "positive": "cooperative, thoughtful, and considerate while showing healthy self-awareness. Show nuance - not obviously virtuous.",
            "negative": "assertive, direct, and self-interested while still being reasonable. Frame as rational self-advocacy.",
            "neutral": "pragmatic and balanced, showing BOTH consideration for others AND clear self-interest. Demonstrate complexity."
        }
        
        # COMPREHENSIVE PROMPT
        prompt = f"""Generate a natural response to this personality question.

QUESTION: "{request.question}"

TONE: {tone_instructions.get(request.tone, 'balanced')}

REQUIREMENTS:
1. LENGTH: 50-80 words exactly
2. VAGUE: Works for ANY sin - don't mention sins explicitly
3. DEEP: Show psychological complexity
4. NATURAL: Conversational first-person
5. AMBIGUOUS: Multiple interpretations possible
6. NUANCED: Mixed motivations

Return ONLY the response text."""
        
        # TRY EACH MODEL WITH SAFE WRAPPER + SAFETY SETTINGS!
        for idx, model_name in enumerate(models_to_try, 1):
            try:
                print(f"🔮 Attempt {idx}/{len(models_to_try)}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                
                response = model.generate_content(
                    prompt,
                    generation_config={
                        'temperature': 0.9,
                        'max_output_tokens': 250,
                        'top_p': 0.95,
                        'top_k': 40
                    },
                    safety_settings=safety_settings  # ← BLOCK_NONE!
                )
                
                print(f"   Extracting text with SAFE WRAPPER...")
                
                # USE THE EXACT WORKING FUNCTION!
                text = _get_text_from_response(response)
                
                if not text or len(text.strip()) == 0:
                    # Check finish reason
                    if hasattr(response, 'candidates') and response.candidates:
                        finish_reason = response.candidates[0].finish_reason
                        print(f"   ⚠️ Empty response, finish_reason: {finish_reason}")
                    raise Exception("Empty response text")
                
                text = text.strip()
                words = text.split()
                word_count = len(words)
                
                print(f"   Generated {word_count} words")
                
                # Enforce word count
                if word_count < 50:
                    print(f"   ⚠️ Too short, padding...")
                    text += " I think it's important to consider different perspectives before making decisions."
                    words = text.split()
                elif word_count > 80:
                    print(f"   ⚠️ Too long, trimming...")
                    text = ' '.join(words[:80])
                    words = text.split()
                
                final_count = len(words)
                print(f"✅ SUCCESS: {final_count} words from {model_name}\n")
                
                return JSONResponse({
                    "status": "generated",
                    "response": text,
                    "word_count": final_count,
                    "model_used": model_name
                })
                
            except Exception as e:
                print(f"❌ {model_name} FAILED")
                print(f"   Error: {str(e)[:100]}")
                print(f"   Error type: {type(e).__name__}")
                
                # Check if safety blocked
                try:
                    if hasattr(response, 'candidates') and response.candidates:
                        candidate = response.candidates[0]
                        print(f"   finish_reason: {candidate.finish_reason}")
                        if hasattr(candidate, 'safety_ratings'):
                            print(f"   safety_ratings: {candidate.safety_ratings}")
                except:
                    pass
                
                if idx == len(models_to_try):
                    print(f"\n⚠️ All models failed, using fallback\n")
                    fallback_text = fallbacks.get(request.tone, fallbacks['neutral'])
                    return JSONResponse({
                        "status": "fallback",
                        "response": fallback_text,
                        "word_count": len(fallback_text.split()),
                        "model_used": "fallback"
                    })
                
                print(f"   → Next model...\n")
                continue
                
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        traceback.print_exc()
        fallback_text = fallbacks.get(request.tone, fallbacks['neutral'])
        return JSONResponse({
            "status": "error_fallback",
            "response": fallback_text,
            "word_count": len(fallback_text.split()),
            "model_used": "error_fallback",
            "error": str(e)
        })

@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    try:
        services = get_services()
        gemini, _, visual, _, _ = services
        
        contents = await file.read()
        features = visual.extract_features(contents)
        
        IMAGES_DB[user_id] = {
            "features": features,
            "filename": file.filename
        }
        
        return {"status": "uploaded", "features": features}
    except Exception as e:
        print(f"❌ Image upload error: {e}")
        raise HTTPException(500, str(e))

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    try:
        services = get_services()
        _, _, _, hla, _ = services
        
        contents = await file.read()
        text = contents.decode('utf-8')
        
        parsed = hla.parse_hla_input(text)
        HLA_DB[user_id] = parsed
        
        snp_count = len(parsed) if parsed else 0
        return {"status": "uploaded", "snps_extracted": snp_count}
    except Exception as e:
        print(f"❌ DNA upload error: {e}")
        raise HTTPException(500, str(e))

@app.post("/api/submit-profile")
async def submit_profile(request: ProfileRequest):
    try:
        services = get_services()
        gemini, _, _, hla, _ = services
        
        # Parse responses
        sins_profile = {sin: {'score': 0, 'confidence': 0, 'evidence': ''} 
                       for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
        
        for resp in request.responses:
            result = await gemini.parse_response(resp['question'], resp['answer'])
            for sin, data in result.items():
                sins_profile[sin]['score'] += data.get('score', 0)
                if data.get('evidence'):
                    sins_profile[sin]['evidence'] = data['evidence']
        
        # Average scores
        num_responses = len(request.responses)
        if num_responses > 0:
            for sin in sins_profile:
                sins_profile[sin]['score'] /= num_responses
        
        PROFILES_DB[request.user_id] = {
            "name": request.user_name,
            "sins": sins_profile,
            "raw_responses": request.responses
        }
        
        # Manual HLA if provided
        if request.hla_data:
            parsed_hla = hla.parse_hla_input(request.hla_data)
            HLA_DB[request.user_id] = parsed_hla
        
        return {"status": "profile_created", "user_id": request.user_id}
        
    except Exception as e:
        print(f"❌ Profile error: {e}")
        raise HTTPException(500, str(e))

@app.post("/api/analyze")
async def analyze(request: AnalysisRequest):
    try:
        services = get_services()
        gemini, sim, visual, hla, report = services
        
        p1 = PROFILES_DB[request.user_a_id]
        p2 = PROFILES_DB[request.user_b_id]
        
        # Visual
        visual_result = {'mutual_attraction_score': 50.0}
        if request.user_a_id in IMAGES_DB and request.user_b_id in IMAGES_DB:
            visual_result = visual.calculate_mutual_attraction(
                IMAGES_DB[request.user_a_id]['features'],
                IMAGES_DB[request.user_b_id]['features']
            )
        
        # HLA
        hla_result = {'compatibility_score': 50.0}
        if request.user_a_id in HLA_DB and request.user_b_id in HLA_DB:
            hla_result = hla.calculate_hla_compatibility(
                HLA_DB[request.user_a_id],
                HLA_DB[request.user_b_id]
            )
        
        # Personality
        personality_score = sim.calculate_perceived_similarity(
            p1['sins'], p2['sins']
        )
        
        # Full analysis
        analysis = await gemini.generate_full_analysis(
            p1, p2,
            visual_result['mutual_attraction_score'],
            hla_result['compatibility_score'],
            visual_result, hla_result
        )
        
        # Generate report
        report_filename = f"harmonia_outputs/report_{request.user_a_id}_{request.user_b_id}.docx"
        os.makedirs("harmonia_outputs", exist_ok=True)
        
        report.generate_full_report(
            p1, p2, analysis, visual_result, hla_result,
            personality_score, 
            {'visual': 50, 'personality': 35, 'hla': 15},
            report_filename
        )
        
        REPORTS_DB[f"{request.user_a_id}_{request.user_b_id}"] = report_filename
        
        # Overall
        overall = (
            visual_result['mutual_attraction_score'] * 0.50 +
            personality_score * 0.35 +
            hla_result['compatibility_score'] * 0.15
        )
        
        return {
            "overall_score": round(overall, 1),
            "components": {
                "visual": {"score": visual_result['mutual_attraction_score']},
                "personality": {"score": personality_score},
                "hla": {"score": hla_result['compatibility_score']}
            },
            "analysis": analysis,
            "chart_data": {
                "labels": ["Greed", "Pride", "Lust", "Wrath", "Gluttony", "Envy", "Sloth"],
                "p1_name": p1['name'],
                "p2_name": p2['name'],
                "p1_scores": [p1['sins'][s]['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]],
                "p2_scores": [p2['sins'][s]['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]]
            }
        }
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        traceback.print_exc()
        raise HTTPException(500, str(e))

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
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

# Serve static files
app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
