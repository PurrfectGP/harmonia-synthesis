"""
Harmonia Main - FLASH MAXIMIZED
Response generator optimized for LONGEST, BEST responses!
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

@app.post("/api/generate-response")
async def generate_response(request: ResponseGeneratorRequest):
    """MAXIMIZED response generator - longest, best responses!"""
    print(f"\n🤖 GEN: {request.question[:50]}... ({request.tone})")
    
    # LONGER fallbacks (80 words each)
    fb = {
        "positive": "I'd probably approach this situation thoughtfully and carefully, trying to find a solution that genuinely works for everyone involved while still staying true to my own core values and principles. Balance is really important to me in situations like this, and I genuinely aim to be considerate and understanding of others while also maintaining my own boundaries and being authentic to who I am as a person. I think finding that middle ground where everyone feels heard and respected makes the most sense.",
        "negative": "I'd prioritize what makes sense for me in this situation without overthinking it too much or getting caught up in worrying about everyone else's opinions. I'm pretty direct and straightforward about my boundaries and preferences, and I don't waste a lot of unnecessary energy worrying about what other people might think about my choices or decisions. Being honest with myself and others tends to work out better in my experience than constantly trying to please everyone or meet their expectations.",
        "neutral": "I'd take some time to weigh the different options carefully and thoughtfully, considering both my own needs and interests as well as the broader context of the situation and how it affects other people involved. There's usually a pragmatic middle ground that works reasonably well for everyone if you look for it. I try to be genuinely thoughtful and considerate about these things but also realistic and practical about what's actually feasible and what matters most to me personally in the long run."
    }
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        safety = [{"category": c, "threshold": "BLOCK_NONE"} for c in ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]]
        
        tones = {
            "positive": "cooperative, thoughtful, and considerate while showing healthy self-awareness and appropriate boundaries. Show nuance - not obviously virtuous or preachy. Demonstrate genuine care balanced with self-respect.",
            "negative": "assertive, direct, and self-interested while still being reasonable and not cartoonishly selfish. Frame choices as rational self-advocacy. Show you're not a pushover but also not mean.",
            "neutral": "pragmatic and balanced, showing BOTH genuine consideration for others AND clear self-interest. Demonstrate complexity and mixed motivations. Real people have competing values - show internal complexity and nuanced thinking."
        }
        
        # MAXIMIZED prompt for LONGEST, BEST responses
        prompt = f"""You are helping generate a personality assessment response. Create a natural, conversational answer.

QUESTION: "{request.question}"

TONE: {tones.get(request.tone, 'balanced and thoughtful')}

CRITICAL REQUIREMENTS (ALL MUST BE MET):
1. LENGTH: Target 70-80 words (be generous with detail!)
2. VAGUENESS: Must work for ANY of the seven deadly sins - do NOT mention any sin explicitly
3. DEPTH: Show deep psychological complexity, mixed motivations, internal conflicts
4. NATURALNESS: Conversational first-person, like talking to a friend, not formal
5. AMBIGUITY: Could reflect multiple personality traits - stay interpretable in different ways
6. NO OBVIOUS SIGNALS: Avoid obviously virtuous or vice-filled language - be subtle
7. NUANCE: Real people have competing values - show rich internal complexity
8. SPECIFICITY: Include concrete thoughts and reasoning, not generic statements
9. AUTHENTICITY: Sound like a real person's actual thought process

EXAMPLE OF EXCELLENT RESPONSE (neutral, 78 words):
"I'd probably take a step back and think through what I actually need from this versus what feels like external pressure or expectations from others. There's usually some middle ground where I can stay authentic to my own priorities without creating unnecessary conflict or friction. I try to be mindful of how my choices affect people, but I'm also pretty realistic about the fact that I can't please everyone all the time, and sometimes I just need to do what makes sense for me even if others might see it differently or have their own opinions about it."

That shows: deep complexity, mixed motivations, could relate to various traits, 78 words, vague enough to work for any sin, authentic voice.

NOW GENERATE A SIMILARLY DETAILED RESPONSE (aim for 70-80 words, rich detail, authentic voice):"""
        
        print(f"🔮 Flash (MAXIMIZED for quality)")
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # MAXIMIZED config for LONGEST, BEST responses!
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.95,  # HIGH for creativity and detail!
                'max_output_tokens': 300,  # Extra room for longer responses
                'top_p': 0.98,  # Maximum diversity
                'top_k': 64,
                'thinking_budget': 2048  # Medium budget (response gen doesn't need max)
            },
            safety_settings=safety
        )
        
        text = response.text.strip()
        words = text.split()
        count = len(words)
        
        print(f"   Generated: {count} words")
        
        # Enforce 50-80 word range
        if count < 50:
            print(f"   ⚠️ Short ({count}), padding to 50+")
            text += " I think it's important to really consider all the different angles and perspectives before making any final decisions about how to handle situations like this in a thoughtful way."
            words = text.split()
        elif count > 80:
            print(f"   ⚠️ Long ({count}), trimming to 80")
            text = ' '.join(words[:80])
            words = text.split()
        
        final = len(words)
        print(f"✅ {final} words (MAXIMIZED quality!)\n")
        
        return JSONResponse({"status": "generated", "response": text, "word_count": final, "model_used": "gemini-2.5-flash-maximized"})
                
    except Exception as e:
        print(f"❌ {e}")
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
