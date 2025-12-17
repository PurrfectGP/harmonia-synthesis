"""
Visual Service - ULTIMATE FIX
OLD SDK + GEMINI 3 PRO + SAFE WRAPPER + BLOCK_NONE SAFETY
"""

import google.generativeai as genai
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

class VisualService:
    """Visual compatibility analysis using Gemini 3 Pro Vision with OLD SDK."""
    
    def __init__(self, api_key: str):
        """Initialize with Gemini API key."""
        genai.configure(api_key=api_key)
        
        # GEMINI 3 PRO for vision analysis!
        self.model_names = [
            'gemini-3-pro-preview',
            'gemini-2.5-pro',
            'gemini-2.5-flash'
        ]
        
        # SAFETY SETTINGS - BLOCK_NONE!
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        logger.info(f"✅ VisualService ready: {self.model_names}")
        logger.info(f"✅ Safety: BLOCK_NONE")
    
    def _get_text_from_response(self, response) -> str:
        """Safe text extraction with try/except."""
        if not response:
            return ""
        
        # Try direct text attribute
        if hasattr(response, 'text'):
            try:
                text = response.text
                if text and isinstance(text, str) and len(text.strip()) > 0:
                    return text
            except Exception:
                pass
        
        # Fallback: candidates
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
        """Call Gemini Vision with fallback - GEMINI 3 PRO FIRST!"""
        for i, model_name in enumerate(self.model_names):
            try:
                logger.info(f"🖼️ Vision attempt {i+1}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    [prompt, image],
                    safety_settings=self.safety_settings  # ← BLOCK_NONE!
                )
                
                # Safe text extraction
                text = self._get_text_from_response(response)
                
                if not text or len(text.strip()) == 0:
                    raise Exception("Empty response")
                
                logger.info(f"✅ Vision success: {model_name}")
                return text
                
            except Exception as e:
                logger.warning(f"❌ {model_name} failed: {str(e)[:60]}")
                if i == len(self.model_names) - 1:
                    raise Exception(f"All vision models failed: {e}")
                continue
    
    def extract_features(self, image_bytes: bytes, gemini_service=None) -> dict:
        """Extract visual features from image using Gemini 3 Pro Vision."""
        try:
            logger.info("📸 Extracting visual features with Gemini 3 Pro...")
            
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_bytes))
            
            # Analyze with Gemini Vision
            prompt = """Analyze this photo for dating compatibility assessment.
            
Rate the following on a scale of 1-10:
- Photo quality (lighting, focus, composition)
- Facial attractiveness
- Expression (warm/cold, open/closed)
- Overall impression

Return ONLY a JSON object:
{
  "quality_score": <1-10>,
  "attractiveness": <1-10>,
  "expression": "<warm/neutral/cold>",
  "impression": "<friendly/serious/mysterious>",
  "confidence": <0.0-1.0>
}"""
            
            text = self._call_vision_with_fallback(prompt, image)
            
            if not text:
                logger.warning("⚠️ Empty response, using defaults")
                return {
                    'quality_score': 70,
                    'attractiveness': 7,
                    'expression': 'neutral',
                    'impression': 'friendly',
                    'confidence': 0.6
                }
            
            # Parse JSON response
            import json
            import re
            
            # Clean response
            text = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            
            try:
                features = json.loads(text)
                
                # Normalize to expected format
                result = {
                    'quality_score': features.get('quality_score', 7) * 10,
                    'attractiveness': features.get('attractiveness', 7),
                    'expression': features.get('expression', 'neutral'),
                    'impression': features.get('impression', 'friendly'),
                    'confidence': features.get('confidence', 0.7)
                }
                
                logger.info(f"✅ Features: Quality={result['quality_score']:.0f}%, Attract={result['attractiveness']}/10")
                return result
                
            except json.JSONDecodeError:
                logger.warning(f"⚠️ JSON parse failed, using defaults")
                return {
                    'quality_score': 70,
                    'attractiveness': 7,
                    'expression': 'neutral',
                    'impression': 'friendly',
                    'confidence': 0.6
                }
                
        except Exception as e:
            logger.error(f"❌ Feature extraction error: {e}")
            return {
                'quality_score': 70,
                'attractiveness': 7,
                'expression': 'neutral',
                'impression': 'friendly',
                'confidence': 0.5
            }
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict) -> dict:
        """Calculate mutual attraction score."""
        try:
            logger.info("💕 Calculating mutual attraction...")
            
            attr_a = features_a.get('attractiveness', 7)
            attr_b = features_b.get('attractiveness', 7)
            
            a_to_b = (attr_b / 10) * 100
            b_to_a = (attr_a / 10) * 100
            
            quality_factor_a = features_a.get('quality_score', 70) / 100
            quality_factor_b = features_b.get('quality_score', 70) / 100
            avg_quality = (quality_factor_a + quality_factor_b) / 2
            
            base_score = (a_to_b + b_to_a) / 2
            
            diff = abs(attr_a - attr_b)
            if diff <= 2:
                reciprocity_bonus = 10
            elif diff <= 4:
                reciprocity_bonus = 5
            else:
                reciprocity_bonus = 0
            
            final_score = min(100, (base_score + reciprocity_bonus) * avg_quality)
            
            result = {
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
                'method': 'Gemini 3 Pro Vision Analysis',
                'note': 'Scores based on photo quality and visual chemistry assessment'
            }
            
            logger.info(f"✅ Mutual attraction: {final_score:.1f}%")
            return result
            
        except Exception as e:
            logger.error(f"❌ Attraction calculation error: {e}")
            return {
                'mutual_attraction_score': 50.0,
                'confidence': 0.5,
                'method': 'Default (error occurred)'
            }
