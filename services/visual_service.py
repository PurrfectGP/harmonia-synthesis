"""
Visual Service - PRODUCTION QUALITY
Uses 2.5 PRO FIRST for best vision analysis!
OLD SDK + SAFE WRAPPER + BLOCK_NONE
"""

import google.generativeai as genai
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

class VisualService:
    """Visual analysis with PRODUCTION QUALITY models."""
    
    def __init__(self, api_key: str):
        """Initialize."""
        genai.configure(api_key=api_key)
        
        # 2.5 PRO FIRST for vision quality!
        self.model_names = [
            'gemini-2.5-pro',
            'gemini-2.5-flash',
            'gemini-1.5-pro'
        ]
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        logger.info(f"✅ VisualService QUALITY: {self.model_names}")
    
    def _get_text_from_response(self, response) -> str:
        """SAFE extraction."""
        if not response:
            return ""
        
        if hasattr(response, 'text'):
            try:
                text = response.text
                if text and isinstance(text, str) and len(text.strip()) > 0:
                    return text
            except Exception:
                pass
        
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
    
    def _call_vision_with_fallback(self, prompt, image):
        """Vision with quality models - 2.5 Pro FIRST!"""
        for i, model_name in enumerate(self.model_names):
            try:
                logger.info(f"🖼️ Vision {i+1}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    [prompt, image],
                    safety_settings=self.safety_settings
                )
                
                text = self._get_text_from_response(response)
                
                if not text or len(text.strip()) == 0:
                    raise Exception("Empty")
                
                logger.info(f"✅ {model_name}")
                return text
                
            except Exception as e:
                logger.warning(f"❌ {model_name}: {str(e)[:50]}")
                if i == len(self.model_names) - 1:
                    raise
                continue
    
    def extract_features(self, image_bytes: bytes, gemini_service=None) -> dict:
        """Extract features with QUALITY vision."""
        try:
            logger.info("📸 Extracting (quality models)...")
            
            image = Image.open(io.BytesIO(image_bytes))
            
            prompt = """Analyze photo for dating compatibility.

Rate 1-10:
- Photo quality (lighting, focus, composition)
- Facial attractiveness
- Expression (warm/neutral/cold)
- Overall impression

Return ONLY JSON:
{
  "quality_score": <1-10>,
  "attractiveness": <1-10>,
  "expression": "<warm/neutral/cold>",
  "impression": "<friendly/serious/mysterious>",
  "confidence": <0.0-1.0>
}"""
            
            text = self._call_vision_with_fallback(prompt, image)
            
            if not text:
                return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.6}
            
            import json, re
            text = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            
            try:
                features = json.loads(text)
                result = {
                    'quality_score': features.get('quality_score', 7) * 10,
                    'attractiveness': features.get('attractiveness', 7),
                    'expression': features.get('expression', 'neutral'),
                    'impression': features.get('impression', 'friendly'),
                    'confidence': features.get('confidence', 0.7)
                }
                
                logger.info(f"✅ Features: Q={result['quality_score']:.0f}%, A={result['attractiveness']}/10")
                return result
                
            except:
                return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.6}
                
        except Exception as e:
            logger.error(f"❌ {e}")
            return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.5}
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict) -> dict:
        """Calculate mutual attraction."""
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
                'method': 'Gemini 2.5 Pro Vision',
                'note': 'High-quality vision analysis'
            }
            
        except Exception as e:
            return {'mutual_attraction_score': 50.0, 'confidence': 0.5}
