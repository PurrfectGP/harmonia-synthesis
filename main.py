
from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict, Optional
import json, os, asyncio, sys, logging, base64
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

from services.gemini_service import GeminiService
from services.similarity_service import SimilarityService
from services.visual_service import VisualService
from services.hla_service import HLAService
from services.dna_service import DNAService
from services.report_service import ReportService
from config import Settings

app = FastAPI(title="Harmonia Synthesis", version="2.6.0")
settings = Settings()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

PROFILES_DB, IMAGES_DB, HLA_DB, REPORTS_DB, PROGRESS_DB = {}, {}, {}, {}, {}
SIN_ORDER = ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]

class ProfileSubmission(BaseModel):
    user_id: str
    user_name: str
    responses: Dict[str, str]
    hla_data: Optional[str] = None

class ComparisonRequest(BaseModel):
    user_a_id: str
    user_b_id: str

class PartnerRating(BaseModel):
    rater_id: str
    partner_id: str
    rating: int

class GenerateResponseRequest(BaseModel):
    question: str
    sentiment: str = "positive"

_services = None
def get_services():
    global _services
    if _services is None:
        logger.info("🔧 Initializing services...")
        _services = (GeminiService(settings.GEMINI_API_KEY), SimilarityService(), VisualService(), HLAService(), DNAService(), ReportService())
        logger.info("✅ All services ready")
    return _services

async def process_profile_task(user_id: str, user_name: str, responses: dict, hla_data: str, gemini, hla_service):
    logger.info(f"⚡ Processing {user_name}...")
    PROGRESS_DB[user_id] = {"stage": "starting", "percent": 5, "message": "Starting analysis..."}

    agg_sins = {k: {"score": 0, "confidence": 0, "evidence_list": []} for k in SIN_ORDER}
    total = len(responses)

    for i, (q_id, text) in enumerate(responses.items()):
        pct = 10 + int((i / max(total, 1)) * 70)
        PROGRESS_DB[user_id] = {"stage": "analyzing", "percent": pct, "message": f"Analyzing response {i+1}/{total}..."}
        logger.info(f"📝 [{user_name}] Response {i+1}/{total}")

        try:
            parsed = await gemini.parse_response(q_id, text)
            for sin, data in parsed.get("sins", {}).items():
                if sin in agg_sins:
                    agg_sins[sin]["score"] += data.get("score", 0)
                    agg_sins[sin]["confidence"] += data.get("confidence", 0.5)
                    if data.get("evidence"):
                        agg_sins[sin]["evidence_list"].append(data["evidence"])
        except Exception as e:
            logger.error(f"❌ Parse error: {e}")

        await asyncio.sleep(0.2)

    PROGRESS_DB[user_id] = {"stage": "finalizing", "percent": 85, "message": "Calculating scores..."}

    count = max(1, total)
    for sin in agg_sins:
        agg_sins[sin]["score"] = round(agg_sins[sin]["score"] / count, 2)
        agg_sins[sin]["confidence"] = round(agg_sins[sin]["confidence"] / count, 2)

    PROGRESS_DB[user_id] = {"stage": "genetics", "percent": 92, "message": "Processing HLA data..."}
    hla_alleles = hla_service.parse_hla_input(hla_data or "")
    HLA_DB[user_id] = hla_alleles

    PROFILES_DB[user_id] = {
        "name": user_name,
        "sins": agg_sins,
        "style": {"detail_level": "high"},
        "raw_responses": responses,
        "created_at": datetime.now().isoformat()
    }

    PROGRESS_DB[user_id] = {"stage": "complete", "percent": 100, "message": "Profile ready!"}
    logger.info(f"✅ {user_name} profile complete!")
    logger.info(f"📊 Sins: {json.dumps({s: agg_sins[s]['score'] for s in SIN_ORDER})}")

@app.post("/api/submit-profile")
async def submit_profile(sub: ProfileSubmission, bg: BackgroundTasks):
    logger.info(f"📥 Profile submission: {sub.user_name}")
    services = get_services()
    PROGRESS_DB[sub.user_id] = {"stage": "queued", "percent": 0, "message": "Queued..."}
    bg.add_task(process_profile_task, sub.user_id, sub.user_name, sub.responses, sub.hla_data or "", services[0], services[3])
    return {"status": "processing", "user_id": sub.user_id}

@app.get("/api/status/{user_id}")
async def check_status(user_id: str):
    return {"ready": user_id in PROFILES_DB, "progress": PROGRESS_DB.get(user_id, {"stage": "unknown", "percent": 0, "message": "Unknown"})}

@app.post("/api/generate-response")
async def generate_response(req: GenerateResponseRequest):
    logger.info(f"🎲 Generate {req.sentiment} response")
    response = await get_services()[0].generate_test_response(req.question, req.sentiment)
    return {"response": response}

@app.post("/api/upload-dna/{user_id}")
async def upload_dna(user_id: str, file: UploadFile = File(...)):
    logger.info(f"🧬 DNA upload: {user_id}")
    dna_service = get_services()[4]
    content = (await file.read()).decode('utf-8', errors='ignore')
    hla_data = dna_service.parse_csv(content)
    HLA_DB[user_id] = hla_data
    return {"status": "parsed", "hla_alleles": dna_service.format_for_display(hla_data), "diversity_score": dna_service.estimate_diversity_score(hla_data)}

@app.post("/api/upload-image/{user_id}")
async def upload_image(user_id: str, file: UploadFile = File(...)):
    logger.info(f"🖼️ Image upload: {user_id}")
    contents = await file.read()
    features = get_services()[2].extract_features(contents)
    IMAGES_DB[user_id] = {"features": features, "filename": file.filename, "raw_bytes": contents}
    return {"status": "uploaded", "features": features}

@app.get("/api/get-partner-image/{user_id}")
async def get_partner_image(user_id: str, partner_id: str):
    if partner_id not in IMAGES_DB:
        return {"has_image": False}
    img = IMAGES_DB[partner_id]
    return {"has_image": True, "image_base64": base64.b64encode(img.get("raw_bytes", b"")).decode(), "features": img.get("features", {})}

@app.post("/api/rate-partner-image")
async def rate_partner_image(rating: PartnerRating):
    logger.info(f"⭐ Rating: {rating.rater_id} -> {rating.partner_id} = {rating.rating}/10")
    return get_services()[2].store_partner_rating(rating.rater_id, rating.partner_id, rating.rating)

@app.post("/api/compare")
async def compare_profiles(req: ComparisonRequest):
    logger.info(f"🔮 COMPARE: {req.user_a_id} vs {req.user_b_id}")

    if req.user_a_id not in PROFILES_DB:
        logger.error(f"❌ Profile not found: {req.user_a_id}")
        raise HTTPException(404, f"Profile not found: {req.user_a_id}")
    if req.user_b_id not in PROFILES_DB:
        logger.error(f"❌ Profile not found: {req.user_b_id}")
        raise HTTPException(404, f"Profile not found: {req.user_b_id}")

    services = get_services()
    gemini, sim_service, visual_service, hla_service, _, report_service = services

    p1, p2 = PROFILES_DB[req.user_a_id], PROFILES_DB[req.user_b_id]
    logger.info(f"📊 Comparing: {p1['name']} vs {p2['name']}")

    # Visual
    logger.info("🖼️ Visual analysis...")
    img_a = IMAGES_DB.get(req.user_a_id, {}).get("features", {})
    img_b = IMAGES_DB.get(req.user_b_id, {}).get("features", {})
    pr_a = visual_service.get_partner_rating(req.user_a_id, req.user_b_id)
    pr_b = visual_service.get_partner_rating(req.user_b_id, req.user_a_id)

    if img_a or img_b:
        visual_result = visual_service.calculate_mutual_attraction(img_a or {}, img_b or {}, partner_rating_a=pr_a, partner_rating_b=pr_b)
    else:
        visual_result = visual_service.get_default_score()
    logger.info(f"🖼️ Visual score: {visual_result.get('mutual_attraction_score', 50)}")

    # Personality
    logger.info("🧠 Personality analysis...")
    similarity_result = sim_service.calculate_perceived_similarity(p1, p2)
    logger.info(f"🧠 Personality score: {similarity_result.get('percentage', 50)}")

    # HLA
    logger.info("🧬 HLA analysis...")
    hla_a, hla_b = HLA_DB.get(req.user_a_id, {}), HLA_DB.get(req.user_b_id, {})
    has_hla = False
    if isinstance(hla_a, dict) and any(hla_a.values()):
        has_hla = True
    elif hla_a:
        has_hla = True
    # Check if we have HLA data
    has_hla_data = False
    if isinstance(hla_a, dict) and any(hla_a.values()):
        has_hla_data = True
    elif hla_a:
        has_hla_data = True

    hla_result = hla_service.calculate_dissimilarity(hla_a, hla_b) if has_hla_data else hla_service.get_default_score()
    logger.info(f"🧬 HLA score: {hla_result.get('compatibility_score', 50)}")

    # AI Analysis
    logger.info("🤖 Generating AI analysis...")
    try:
        analysis = await gemini.generate_full_analysis(
            p1, p2,
            visual_score=visual_result.get('mutual_attraction_score', 50),
            hla_score=hla_result.get('compatibility_score', 50),
            visual_details=visual_result,
            hla_details=hla_result,
            image_ratings={"p1_rated_p2": pr_a, "p2_rated_p1": pr_b}
        )
        logger.info("✅ AI analysis complete")
    except Exception as e:
        logger.error(f"❌ AI analysis failed: {e}")
        analysis = gemini._default_analysis(p1['name'], p2['name'])

    # Calculate overall
    weights = {'visual': settings.VISUAL_WEIGHT, 'personality': settings.PERSONALITY_WEIGHT, 'hla': settings.HLA_WEIGHT}
    overall = (
        visual_result.get('mutual_attraction_score', 50) * weights['visual'] / 100 +
        similarity_result.get('percentage', 50) * weights['personality'] / 100 +
        hla_result.get('compatibility_score', 50) * weights['hla'] / 100
    )
    logger.info(f"📊 Overall score: {overall:.1f}%")

    # Report
    logger.info("📄 Generating report...")
    report_filename = f"harmonia_outputs/report_{p1['name']}_{p2['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    try:
        report_service.generate_full_report(p1, p2, analysis, visual_result, hla_result, similarity_result, weights, report_filename)
        REPORTS_DB[f"{req.user_a_id}_{req.user_b_id}"] = report_filename
        logger.info(f"✅ Report saved: {report_filename}")
    except Exception as e:
        logger.error(f"❌ Report error: {e}")
        report_filename = None

    # Chart data
    p1_scores = [round(p1['sins'].get(s, {}).get('score', 0), 2) for s in SIN_ORDER]
    p2_scores = [round(p2['sins'].get(s, {}).get('score', 0), 2) for s in SIN_ORDER]
    logger.info(f"📈 {p1['name']} scores: {p1_scores}")
    logger.info(f"📈 {p2['name']} scores: {p2_scores}")

    result = {
        "overall_score": round(overall, 1),
        "components": {
            "visual": {"score": round(visual_result.get('mutual_attraction_score', 50), 1), "weight": weights['visual'], "details": visual_result},
            "personality": {"score": round(similarity_result.get('percentage', 50), 1), "weight": weights['personality'], "details": similarity_result},
            "hla": {"score": round(hla_result.get('compatibility_score', 50), 1), "weight": weights['hla'], "details": hla_result}
        },
        "analysis": analysis,
        "chart_data": {
            "labels": [s.capitalize() for s in SIN_ORDER],
            "p1_scores": p1_scores,
            "p2_scores": p2_scores,
            "p1_name": p1['name'],
            "p2_name": p2['name']
        },
        "report_file": report_filename
    }

    logger.info("✅ COMPARISON COMPLETE - Sending response")
    return result

@app.get("/api/download-report/{user_a_id}/{user_b_id}")
async def download_report(user_a_id: str, user_b_id: str):
    key = f"{user_a_id}_{user_b_id}"
    if key not in REPORTS_DB or not os.path.exists(REPORTS_DB[key]):
        raise HTTPException(404, "Report not found")
    return FileResponse(REPORTS_DB[key], media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=os.path.basename(REPORTS_DB[key]))

@app.get("/api/health")
async def health():
    return {"status": "healthy", "version": "2.6.0", "profiles": len(PROFILES_DB)}

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
