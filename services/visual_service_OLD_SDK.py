"""
Visual Service - OLD SDK Version
Uses: import google.generativeai as genai (compatible with requirements.txt)
"""

import google.generativeai as genai
import logging
from PIL import Image
import io
import base64

logger = logging.getLogger(__name__)

class VisualService:
    """Visual compatibility analysis using Gemini Vision API with OLD SDK."""
    
    def __init__(self, api_key: str):
        """Initialize with Gemini API key."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        logger.info("✅ VisualService initialized with OLD SDK")
    
    def extract_features(self, image_bytes: bytes, gemini_service=None) -> dict:
        """
        Extract visual features from image using Gemini Vision.
        Returns quality score and basic features.
        """
        try:
            logger.info("📸 Extracting visual features...")
            
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
            
            response = self.model.generate_content([prompt, image])
            
            # Extract text from response
            if hasattr(response, 'text'):
                try:
                    text = response.text
                except Exception:
                    text = ""
            else:
                text = ""
            
            if not text:
                logger.warning("⚠️ Empty response from Gemini Vision, using defaults")
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
                    'quality_score': features.get('quality_score', 7) * 10,  # Convert 1-10 to percentage
                    'attractiveness': features.get('attractiveness', 7),
                    'expression': features.get('expression', 'neutral'),
                    'impression': features.get('impression', 'friendly'),
                    'confidence': features.get('confidence', 0.7)
                }
                
                logger.info(f"✅ Features extracted: Quality={result['quality_score']:.0f}%, Attractiveness={result['attractiveness']}/10")
                return result
                
            except json.JSONDecodeError:
                logger.warning(f"⚠️ Failed to parse JSON, using defaults. Response: {text[:100]}")
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
        """
        Calculate mutual attraction score based on visual features.
        Uses bidirectional assessment with reciprocity bonus.
        """
        try:
            logger.info("💕 Calculating mutual attraction...")
            
            # Get base attractiveness scores
            attr_a = features_a.get('attractiveness', 7)
            attr_b = features_b.get('attractiveness', 7)
            
            # A's attraction to B (based on B's attractiveness)
            a_to_b = (attr_b / 10) * 100
            
            # B's attraction to A (based on A's attractiveness)
            b_to_a = (attr_a / 10) * 100
            
            # Quality factor (lower quality reduces confidence)
            quality_factor_a = features_a.get('quality_score', 70) / 100
            quality_factor_b = features_b.get('quality_score', 70) / 100
            avg_quality = (quality_factor_a + quality_factor_b) / 2
            
            # Base mutual score (average of bidirectional)
            base_score = (a_to_b + b_to_a) / 2
            
            # Reciprocity bonus (when both are similarly attractive)
            diff = abs(attr_a - attr_b)
            if diff <= 2:
                reciprocity_bonus = 10  # Both similarly attractive
            elif diff <= 4:
                reciprocity_bonus = 5   # Somewhat balanced
            else:
                reciprocity_bonus = 0   # Mismatch
            
            # Final score with quality adjustment
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
                'method': 'Gemini Vision Analysis',
                'note': 'Scores based on photo quality and visual chemistry assessment'
            }
            
            logger.info(f"✅ Mutual attraction: {final_score:.1f}% (A→B: {a_to_b:.1f}%, B→A: {b_to_a:.1f}%)")
            return result
            
        except Exception as e:
            logger.error(f"❌ Attraction calculation error: {e}")
            return {
                'mutual_attraction_score': 50.0,
                'a_to_b': 50.0,
                'b_to_a': 50.0,
                'reciprocity_bonus': 0,
                'confidence': 0.5,
                'method': 'Default (error occurred)',
                'note': 'Error in visual analysis'
            }
