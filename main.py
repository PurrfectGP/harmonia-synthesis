"""
Main - FLASH with FORCED LONG RESPONSES
Uses detailed examples to force 70-80 word outputs!
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Optional
import os, sys, traceback

sys.path.append(os.path.dirname(__file__))
try:
    from services.gemini_service import GeminiService
    from services.similarity_service import SimilarityService
    from services.visual_service import VisualService
    from services.hla_service import HLAService
    from services.report_service import ReportService
    print("✅ Services imported")
except Exception as e:
    print(f"❌ {e}")

app = FastAPI(title="Harmonia")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

PROFILES_DB, IMAGES_DB, HLA_DB, REPORTS_DB = {}, {}, {}, {}

def get_services():
    api_key = os.getenv('GEMINI_API_KEY')
    return (GeminiService(), SimilarityService(), VisualService(api_key), HLAService(), ReportService())

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
    return {"status": "running"}

def _extract_text_safely_from_response(response) -> str:
    """Safely extract text from Gemini response, handling blocked/empty responses."""
    try:
        # Check if response has candidates
        if not response.candidates:
            print("⚠️  No candidates in response")
            return None

        # Check the first candidate
        candidate = response.candidates[0]

        # Check finish reason
        finish_reason = candidate.finish_reason
        if finish_reason == 2:  # SAFETY
            print(f"⚠️  Response blocked by safety filters")
            return None
        elif finish_reason == 3:  # RECITATION
            print(f"⚠️  Response blocked due to recitation")
            return None
        elif finish_reason not in [0, 1]:  # 0=UNSPECIFIED, 1=STOP (normal completion)
            print(f"⚠️  Unexpected finish_reason: {finish_reason}")
            return None

        # Try to get text
        if hasattr(candidate.content, 'parts') and candidate.content.parts:
            text = ''.join(part.text for part in candidate.content.parts if hasattr(part, 'text'))
            if text.strip():
                return text.strip()

        # Fallback to response.text if available
        if hasattr(response, 'text') and response.text:
            return response.text.strip()

        print("⚠️  Response has no text content")
        return None

    except Exception as e:
        print(f"⚠️  Error extracting text: {e}")
        return None

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    """FORCE 70-80 word responses with detailed examples!"""
    print(f"\n🤖 GEN: {request.question[:50]}... ({request.tone})")

    # 80-word fallbacks
    fb = {
        "positive": "I'd probably approach this situation thoughtfully and carefully, trying to find a solution that genuinely works for everyone involved while still staying true to my own core values and principles. Balance is really important to me in situations like this, and I genuinely aim to be considerate and understanding of others while also maintaining my own boundaries and being authentic to who I am as a person. I think finding that middle ground where everyone feels heard and respected makes the most sense.",
        "negative": "I'd prioritize what makes sense for me in this situation without overthinking it too much or getting caught up in worrying about everyone else's opinions. I'm pretty direct and straightforward about my boundaries and preferences, and I don't waste a lot of unnecessary energy worrying about what other people might think about my choices or decisions. Being honest with myself and others tends to work out better in my experience than constantly trying to please everyone or meet their expectations.",
        "neutral": "I'd take some time to weigh the different options carefully and thoughtfully, considering both my own needs and interests as well as the broader context of the situation and how it affects other people involved. There's usually a pragmatic middle ground that works reasonably well for everyone if you look for it. I try to be genuinely thoughtful and considerate about these things but also realistic and practical about what's actually feasible and what matters most to me personally in the long run."
    }

    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

        safety = [{"category": c, "threshold": "BLOCK_NONE"} for c in ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]]
        
        # FORCE LONG with multiple examples!
        tone_examples = {
            "positive": """Example: "I'd probably approach this situation thoughtfully and carefully, trying to find a solution that genuinely works for everyone involved while still staying true to my own core values and principles. Balance is really important to me in situations like this, and I genuinely aim to be considerate and understanding of others while also maintaining my own boundaries and being authentic to who I am as a person. I think finding that middle ground where everyone feels heard and respected makes the most sense." (80 words)""",
            
            "negative": """Example: "I'd prioritize what makes sense for me in this situation without overthinking it too much or getting caught up in worrying about everyone else's opinions. I'm pretty direct and straightforward about my boundaries and preferences, and I don't waste a lot of unnecessary energy worrying about what other people might think about my choices or decisions. Being honest with myself and others tends to work out better in my experience than constantly trying to please everyone or meet their expectations." (80 words)""",
            
            "neutral": """Example: "I'd take some time to weigh the different options carefully and thoughtfully, considering both my own needs and interests as well as the broader context of the situation and how it affects other people involved. There's usually a pragmatic middle ground that works reasonably well for everyone if you look for it. I try to be genuinely thoughtful and considerate about these things but also realistic and practical about what's actually feasible and what matters most to me personally in the long run." (80 words)"""
        }
        
        # FORCE LENGTH with explicit instructions + example
        prompt = f"""You MUST generate a response that is EXACTLY 70-80 words. This is CRITICAL.

QUESTION: "{request.question}"

TONE: {request.tone}

{tone_examples.get(request.tone, tone_examples['neutral'])}

Now generate a SIMILAR LENGTH response (70-80 words like the example above) for the question. 

CRITICAL: Your response MUST be 70-80 words. Count carefully. Be detailed, thoughtful, and conversational. Match the example's length and style.

Write ONLY the response (no preamble, no quotation marks):"""
        
        print(f"🔮 Gemini (FORCED LONG)")

        # Use model from environment or default to Gemini 3 Flash (fast with Pro reasoning)
        model_name = os.getenv('GEMINI_MODEL', 'gemini-3-flash-preview')
        model = genai.GenerativeModel(model_name)

        # FORCE maximum output!
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 1.0,  # MAXIMUM for longest output!
                'max_output_tokens': 400,  # Even more room!
                'top_p': 1.0,  # Consider ALL tokens!
                'top_k': 64,
                'candidate_count': 1
            },
            safety_settings=safety
        )

        text = _extract_text_safely_from_response(response)

        # If empty response, use fallback immediately
        if not text:
            print(f"❌ Empty response from Gemini API, using fallback")
            t = fb.get(request.tone, fb['neutral'])
            return JSONResponse({"status": "fallback", "response": t, "word_count": len(t.split()), "reason": "empty_response"})

        # Remove quotes if model added them
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        if text.startswith("'") and text.endswith("'"):
            text = text[1:-1]
        
        words = text.split()
        count = len(words)
        
        print(f"   Generated: {count} words")
        
        # AGGRESSIVE padding if still too short
        if count < 50:
            print(f"   FORCING to 50+ words...")
            additions = [
                " I think it's really important to consider all the different angles and perspectives involved in situations like this before making any kind of final decision.",
                " At the end of the day, I try to balance my own needs with being thoughtful about how my choices might affect other people around me.",
                " It's not always easy to find the right approach, but I believe in being genuine and authentic rather than just going along with what others expect."
            ]
            # Add until we hit 50+
            for add in additions:
                if len(text.split()) >= 50:
                    break
                text += add
            words = text.split()
            count = len(words)
            print(f"   After padding: {count} words")
        
        # Trim if over 80
        if count > 80:
            print(f"   Trimming to 80")
            text = ' '.join(words[:80])
            words = text.split()
        
        final = len(words)
        print(f"✅ FINAL: {final} words\n")
        
        return JSONResponse({"status": "generated", "response": text, "word_count": final, "model_used": "gemini-2.5-flash"})
                
    except Exception as e:
        print(f"❌ ERROR: {e}")
        traceback.print_exc()
        t = fb.get(request.tone, fb['neutral'])
        return JSONResponse({"status": "fallback", "response": t, "word_count": len(t.split())})

@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    s = get_services()
    c = await file.read()
    f = s[2].extract_features(c)
    IMAGES_DB[user_id] = {"features": f, "filename": file.filename}
    return {"status": "uploaded", "features": f}

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    s = get_services()
    c = await file.read()
    p = s[3].parse_hla_input(c.decode('utf-8'))
    HLA_DB[user_id] = p
    return {"status": "uploaded", "snps_extracted": len(p) if p else 0}

@app.post("/api/submit-profile")
async def submit_profile(request: ProfileRequest):
    s = get_services()
    sins = {x: {'score': 0, 'evidence': ''} for x in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    for r in request.responses:
        res = await s[0].parse_response(r['question'], r['answer'])
        for sin, data in res.items():
            sins[sin]['score'] += data.get('score', 0)
            if data.get('evidence'):
                sins[sin]['evidence'] = data['evidence']
    
    if request.responses:
        for sin in sins:
            sins[sin]['score'] /= len(request.responses)
    
    PROFILES_DB[request.user_id] = {"name": request.user_name, "sins": sins, "raw_responses": request.responses}
    if request.hla_data:
        HLA_DB[request.user_id] = s[3].parse_hla_input(request.hla_data)
    return {"status": "profile_created", "user_id": request.user_id}

@app.post("/api/analyze")
async def analyze(request: AnalysisRequest):
    s = get_services()
    p1, p2 = PROFILES_DB[request.user_a_id], PROFILES_DB[request.user_b_id]
    
    vr = {'mutual_attraction_score': 50.0}
    if request.user_a_id in IMAGES_DB and request.user_b_id in IMAGES_DB:
        vr = s[2].calculate_mutual_attraction(IMAGES_DB[request.user_a_id]['features'], IMAGES_DB[request.user_b_id]['features'])
    
    hr = {'compatibility_score': 50.0}
    if request.user_a_id in HLA_DB and request.user_b_id in HLA_DB:
        hr = s[3].calculate_hla_compatibility(HLA_DB[request.user_a_id], HLA_DB[request.user_b_id])
    
    ps = s[1].calculate_perceived_similarity(p1['sins'], p2['sins'])
    an = await s[0].generate_full_analysis(p1, p2, vr['mutual_attraction_score'], hr['compatibility_score'], vr, hr)
    
    os.makedirs("harmonia_outputs", exist_ok=True)
    rf = f"harmonia_outputs/report_{request.user_a_id}_{request.user_b_id}.docx"
    s[4].generate_full_report(p1, p2, an, vr, hr, ps, {'visual': 50, 'personality': 35, 'hla': 15}, rf)
    REPORTS_DB[f"{request.user_a_id}_{request.user_b_id}"] = rf
    
    ov = vr['mutual_attraction_score'] * 0.50 + ps * 0.35 + hr['compatibility_score'] * 0.15
    
    return {
        "overall_score": round(ov, 1),
        "components": {"visual": {"score": vr['mutual_attraction_score']}, "personality": {"score": ps}, "hla": {"score": hr['compatibility_score']}},
        "analysis": an,
        "chart_data": {"labels": ["Greed", "Pride", "Lust", "Wrath", "Gluttony", "Envy", "Sloth"], "p1_name": p1['name'], "p2_name": p2['name'], "p1_scores": [p1['sins'][x]['score'] for x in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]], "p2_scores": [p2['sins'][x]['score'] for x in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]]}
    }

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
    k = f"{user_a_id}_{user_b_id}"
    if k not in REPORTS_DB:
        raise HTTPException(404, "Not found")
    return FileResponse(REPORTS_DB[k], media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=f"harmonia_{k}.docx")

app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
