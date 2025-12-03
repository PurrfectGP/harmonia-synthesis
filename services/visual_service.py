
import numpy as np
from PIL import Image
import io
import hashlib
import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class VisualService:
    def __init__(self):
        self.rating_store = {}
        self.partner_ratings = {}
        logger.info("VisualService ready")

    def extract_features(self, image_bytes: bytes) -> dict:
        try:
            img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            arr = np.array(img)
            h, w = arr.shape[:2]
            brightness = float(np.mean(arr))
            contrast = float(np.std(arr))
            quality = min(100, max(0, 50 + (brightness-127)*0.1 + (contrast-50)*0.2 + min(w,h)/100*2))
            return {"image_id": hashlib.md5(image_bytes[:1000]).hexdigest()[:12], "brightness": round(brightness,2),
                    "contrast": round(contrast,2), "dimensions": f"{w}x{h}", "quality_score": round(quality,1)}
        except Exception as e:
            logger.error(f"Feature error: {e}")
            return {"quality_score": 50.0, "error": str(e)}

    def store_rating(self, user_id: str, image_id: str, rating: int, features: dict = None) -> dict:
        if user_id not in self.rating_store:
            self.rating_store[user_id] = []
        self.rating_store[user_id].append({"image_id": image_id, "rating": max(1,min(10,rating)), "features": features or {}})
        return {"stored": True}

    def store_partner_rating(self, rater_id: str, partner_id: str, rating: int) -> dict:
        self.partner_ratings[f"{rater_id}_rates_{partner_id}"] = {"rating": max(1,min(10,rating))}
        logger.info(f"Stored partner rating: {rater_id} -> {partner_id} = {rating}")
        return {"stored": True, "rating": rating}

    def get_partner_rating(self, rater_id: str, partner_id: str) -> Optional[int]:
        data = self.partner_ratings.get(f"{rater_id}_rates_{partner_id}")
        return data.get("rating") if data else None

    def get_user_ratings(self, user_id: str) -> List[dict]:
        return self.rating_store.get(user_id, [])

    def analyze_preferences(self, user_id: str) -> dict:
        ratings = self.get_user_ratings(user_id)
        if len(ratings) < 3:
            return {"has_enough_data": False, "ratings_count": len(ratings)}
        avg = sum(r['rating'] for r in ratings) / len(ratings)
        return {"has_enough_data": True, "ratings_count": len(ratings), "average_rating": round(avg,2)}

    def calculate_mutual_attraction(self, features_a: dict, features_b: dict, prefs_a: dict = None, prefs_b: dict = None, partner_rating_a: int = None, partner_rating_b: int = None) -> dict:
        qa = features_a.get('quality_score', 50) if features_a else 50
        qb = features_b.get('quality_score', 50) if features_b else 50
        base = (qa + qb) / 2

        bonus = 0
        a_to_b = qb * 0.85
        b_to_a = qa * 0.85

        if partner_rating_a is not None:
            a_to_b = partner_rating_a * 10
            bonus += 5 if partner_rating_a >= 7 else 0
        if partner_rating_b is not None:
            b_to_a = partner_rating_b * 10
            bonus += 5 if partner_rating_b >= 7 else 0

        final = min(100, base + bonus)
        return {"mutual_attraction_score": round(final,1), "a_to_b": round(a_to_b,1), "b_to_a": round(b_to_a,1),
                "quality_a": qa, "quality_b": qb, "partner_rating_a_to_b": partner_rating_a, "partner_rating_b_to_a": partner_rating_b}

    def get_default_score(self) -> dict:
        return {"mutual_attraction_score": 65.0, "a_to_b": 65.0, "b_to_a": 65.0, "quality_a": 50, "quality_b": 50}
