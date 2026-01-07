"""
Visual Service - NO thinking_budget (OLD SDK)
Maximized with temp/tokens/top_p instead!
"""

import google.generativeai as genai
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

class VisualService:

    def __init__(self, api_key: str, model_name: str = None):
        import os
        genai.configure(api_key=api_key)
        # Use model from parameter, environment, or default
        self.model_name = model_name or os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        logger.info(f"✅ VisualService: {self.model_name}")

    def _extract_text_safely(self, response) -> str:
        """Safely extract text from Gemini response, handling blocked/empty responses."""
        try:
            # Check if response has candidates
            if not response.candidates:
                logger.warning("⚠️  No candidates in response")
                return None

            # Check the first candidate
            candidate = response.candidates[0]

            # Check finish reason
            finish_reason = candidate.finish_reason
            if finish_reason == 2:  # SAFETY
                logger.warning(f"⚠️  Response blocked by safety filters")
                return None
            elif finish_reason == 3:  # RECITATION
                logger.warning(f"⚠️  Response blocked due to recitation")
                return None
            elif finish_reason not in [0, 1]:  # 0=UNSPECIFIED, 1=STOP (normal completion)
                logger.warning(f"⚠️  Unexpected finish_reason: {finish_reason}")
                return None

            # Try to get text
            if hasattr(candidate.content, 'parts') and candidate.content.parts:
                text = ''.join(part.text for part in candidate.content.parts if hasattr(part, 'text'))
                if text.strip():
                    return text.strip()

            # Fallback to response.text if available
            if hasattr(response, 'text') and response.text:
                return response.text.strip()

            logger.warning("⚠️  Response has no text content")
            return None

        except Exception as e:
            logger.warning(f"⚠️  Error extracting text: {e}")
            return None
    
    def extract_features(self, image_bytes: bytes, gemini_service=None) -> dict:
        try:
            logger.info("📸 Extracting...")
            image = Image.open(io.BytesIO(image_bytes))

            prompt = """Analyze photo for dating compatibility. Rate 1-10: quality, attractiveness, expression, impression. Return ONLY JSON:
{"quality_score": <1-10>, "attractiveness": <1-10>, "expression": "<warm/neutral/cold>", "impression": "<friendly/serious/mysterious>", "confidence": <0.0-1.0>}"""

            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content([prompt, image], generation_config={'temperature': 0.4, 'max_output_tokens': 1024, 'top_p': 0.9, 'top_k': 40}, safety_settings=self.safety_settings)

            text = self._extract_text_safely(response)

            # If empty response, use fallback
            if not text:
                logger.error("❌ Empty response from Gemini API, using fallback")
                return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.5}

            import json, re
            text = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            features = json.loads(text)

            result = {
                'quality_score': features.get('quality_score', 7) * 10,
                'attractiveness': features.get('attractiveness', 7),
                'expression': features.get('expression', 'neutral'),
                'impression': features.get('impression', 'friendly'),
                'confidence': features.get('confidence', 0.75)
            }

            logger.info(f"✅ Q={result['quality_score']:.0f}%, A={result['attractiveness']}/10")
            return result
        except Exception as e:
            logger.error(f"❌ {e}")
            return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.5}
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict) -> dict:
        try:
            attr_a = features_a.get('attractiveness', 7)
            attr_b = features_b.get('attractiveness', 7)
            a_to_b = (attr_b / 10) * 100
            b_to_a = (attr_a / 10) * 100
            quality_a = features_a.get('quality_score', 70) / 100
            quality_b = features_b.get('quality_score', 70) / 100
            avg_quality = (quality_a + quality_b) / 2
            base_score = (a_to_b + b_to_a) / 2
            diff = abs(attr_a - attr_b)
            reciprocity_bonus = 10 if diff <= 2 else (5 if diff <= 4 else 0)
            final_score = min(100, (base_score + reciprocity_bonus) * avg_quality)
            
            return {
                'mutual_attraction_score': round(final_score, 1),
                'a_to_b': round(a_to_b, 1),
                'b_to_a': round(b_to_a, 1),
                'reciprocity_bonus': reciprocity_bonus,
                'quality_a': features_a.get('quality_score', 70),
                'quality_b': features_b.get('quality_score', 70),
                'person_a_attractiveness': attr_a,
                'person_b_attractiveness': attr_b,
                'person_a_expression': features_a.get('expression', 'neutral'),
                'person_b_expression': features_b.get('expression', 'neutral'),
                'confidence': (features_a.get('confidence', 0.7) + features_b.get('confidence', 0.7)) / 2,
                'method': 'Gemini 2.5 Flash MAXIMIZED',
                'note': 'Optimized settings for quality'
            }
        except Exception as e:
            return {'mutual_attraction_score': 50.0, 'confidence': 0.5}
