"""
Harmonia Main - PRODUCTION QUALITY
2.5 PRO FIRST for best responses!
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
    print(f"❌ Import: {e}")

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

def _get_text_from_response(response) -> str:
    if not response:
        return ""
    if hasattr(response, 'text'):
        try:
            t = response.text
            if t and len(t.strip()) > 0:
                return t
        except:
            pass
    try:
        if hasattr(response, 'candidates') and response.candidates and len(response.candidates) > 0:
            c = response.candidates[0]
            if hasattr(c, 'content') and c.content and hasattr(c.content, 'parts') and c.content.parts and len(c.content.parts) > 0:
                if hasattr(c.content.parts[0], 'text'):
                    return c.content.parts[0].text
    except:
        pass
    return ""

@app.get("/api/health")
async def health():
    return {"status": "running"}

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    print(f"\n🤖 {request.question[:40]}... ({request.tone})")
    
    fb = {
        "positive": "I'd approach this thoughtfully, finding solutions that work for everyone while staying true to my values. Balance matters, and I aim to be considerate while maintaining boundaries and being authentic.",
        "negative": "I'd prioritize what makes sense without overthinking. I'm direct about boundaries and don't waste energy on others' opinions. Being honest works better than trying to please everyone.",
        "neutral": "I'd weigh options carefully, considering my needs and broader context. There's usually pragmatic middle ground. I try to be thoughtful but realistic about what's feasible."
    }
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        models = ['gemini-2.5-pro', 'gemini-2.5-flash', 'gemini-1.5-pro']
        safety = [{"category": c, "threshold": "BLOCK_NONE"} for c in ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]]
        
        tones = {"positive": "cooperative, thoughtful", "negative": "assertive, direct", "neutral": "pragmatic, balanced"}
        
        prompt = f"""Generate response.
Q: "{request.question}"
TONE: {tones.get(request.tone, 'balanced')}
50-80 words, vague, deep, natural, ambiguous, nuanced.
Return ONLY response."""
        
        for idx, m in enumerate(models, 1):
            try:
                print(f"🔮 {idx}: {m}")
                model = genai.GenerativeModel(m)
                r = model.generate_content(prompt, generation_config={'temperature': 0.9, 'max_output_tokens': 250}, safety_settings=safety)
                
                text = _get_text_from_response(r)
                if not text:
                    raise Exception("Empty")
                
                words = text.strip().split()
                if len(words) < 50:
                    text += " I consider perspectives."
                    words = text.split()
                elif len(words) > 80:
                    text = ' '.join(words[:80])
                    words = text.split()
                
                print(f"✅ {len(words)} words\n")
                return JSONResponse({"status": "ok", "response": text, "word_count": len(words), "model": m})
                
            except Exception as e:
                print(f"❌ {m}: {str(e)[:50]}")
                if idx == len(models):
                    t = fb.get(request.tone, fb['neutral'])
                    return JSONResponse({"status": "fallback", "response": t, "word_count": len(t.split())})
                
    except Exception as e:
        print(f"❌ {e}")
        t = fb.get(request.tone, fb['neutral'])
        return JSONResponse({"status": "error", "response": t})

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
