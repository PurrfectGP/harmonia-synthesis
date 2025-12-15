"""
Harmonia Synthesis - Main Application
Complete with all endpoints and static file serving
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional
import os
import sys

# Import services
sys.path.append(os.path.dirname(__file__))
from services.gemini_service import GeminiService
from services.similarity_service import SimilarityService
from services.visual_service import VisualService
from services.hla_service import HLAService
from services.report_service import ReportService

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

# Initialize services
def get_services():
    gemini = GeminiService()
    similarity = SimilarityService()
    visual = VisualService()
    hla = HLAService()
    report = ReportService()
    return gemini, similarity, visual, hla, report

# Request models
class ProfileRequest(BaseModel):
    user_id: str
    user_name: str
    responses: List[Dict]
    hla_data: Optional[str] = ""

class AnalysisRequest(BaseModel):
    user_a_id: str
    user_b_id: str

# ═══════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════════════

@app.get("/")
async def root():
    return {"status": "Harmonia API running", "version": "1.0"}

@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    """Upload profile image for visual analysis."""
    gemini, _, visual, _, report = get_services()
    
    contents = await file.read()
    features = visual.extract_features(contents, gemini)
    
    IMAGES_DB[user_id] = {
        "features": features,
        "filename": file.filename,
        "uploaded_at": datetime.now().isoformat()
    }
    
    return {"status": "uploaded", "features": features}

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    """Upload DNA CSV file for HLA analysis."""
    _, _, _, hla, _ = get_services()
    
    contents = await file.read()
    text = contents.decode('utf-8')
    
    parsed = hla.parse_hla_input(text)
    HLA_DB[user_id] = parsed
    
    snp_count = len(parsed) if isinstance(parsed, list) else 0
    return {"status": "uploaded", "snps_extracted": snp_count}

@app.post("/api/submit-profile")
async def submit_profile(request: ProfileRequest):
    """Submit questionnaire responses and create personality profile."""
    gemini, _, _, hla, _ = get_services()
    
    # Parse all responses into sins profile
    sins_aggregate = {}
    for resp in request.responses:
        result = await gemini.parse_response(resp['question'], resp['answer'])
        
        # Aggregate scores
        for sin, data in result.items():
            if sin not in sins_aggregate:
                sins_aggregate[sin] = {'scores': [], 'evidences': []}
            sins_aggregate[sin]['scores'].append(data['score'])
            sins_aggregate[sin]['evidences'].append(data.get('evidence', ''))
    
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
        parsed_hla = hla.parse_hla_input(request.hla_data)
        HLA_DB[request.user_id] = parsed_hla
    
    return {"status": "profile_created", "user_id": request.user_id}

@app.post("/api/analyze")
async def analyze_compatibility(request: AnalysisRequest):
    """Analyze full compatibility between two users."""
    gemini, similarity, visual, hla, report = get_services()
    
    # Get profiles
    if request.user_a_id not in PROFILES_DB or request.user_b_id not in PROFILES_DB:
        raise HTTPException(404, "Profiles not found")
    
    p1 = PROFILES_DB[request.user_a_id]
    p2 = PROFILES_DB[request.user_b_id]
    
    # Visual analysis
    visual_result = {"mutual_attraction_score": 50.0}
    if request.user_a_id in IMAGES_DB and request.user_b_id in IMAGES_DB:
        visual_result = visual.calculate_mutual_attraction(
            IMAGES_DB[request.user_a_id]['features'],
            IMAGES_DB[request.user_b_id]['features']
        )
    
    # HLA analysis
    hla_result = {"compatibility_score": 50.0}
    if request.user_a_id in HLA_DB and request.user_b_id in HLA_DB:
        hla_result = hla.calculate_hla_compatibility(
            HLA_DB[request.user_a_id],
            HLA_DB[request.user_b_id]
        )
    
    # Personality similarity
    personality_score = similarity.calculate_perceived_similarity(p1['sins'], p2['sins'])
    
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
    os.makedirs("harmonia_outputs", exist_ok=True)
    report_filename = f"harmonia_outputs/report_{request.user_a_id}_{request.user_b_id}.docx"
    
    report.generate_full_report(
        p1, p2, analysis, visual_result, hla_result,
        personality_score, {}, report_filename
    )
    
    REPORTS_DB[f"{request.user_a_id}_{request.user_b_id}"] = report_filename
    
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
            "p1_scores": [p1['sins'][s]['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]],
            "p2_scores": [p2['sins'][s]['score'] for s in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]]
        }
    }

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
    """Download compatibility report."""
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

# ═══════════════════════════════════════════════════════════════════
# CRITICAL FIX: Mount /data/ folder BEFORE / catch-all
# ═══════════════════════════════════════════════════════════════════
app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

print("✅ Harmonia API initialized")
print("✅ Static file serving configured:")
print("   - /data/ → data/ folder")
print("   - / → frontend/ folder")
