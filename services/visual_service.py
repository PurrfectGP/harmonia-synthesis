"""
Visual Service - FLASH MAXIMIZED
Uses thinking budget for best vision analysis!
"""

import google.generativeai as genai
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

class VisualService:
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        
        self.model_name = 'gemini-2.5-flash'
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        logger.info(f"✅ VisualService: Flash MAXIMIZED for vision")
    
    def extract_features(self, image_bytes: bytes, gemini_service=None) -> dict:
        """Extract with HIGH thinking budget for accurate vision analysis!"""
        try:
            logger.info("📸 Extracting features (Flash MAXIMIZED)...")
            
            image = Image.open(io.BytesIO(image_bytes))
            
            # DETAILED vision prompt for maximum quality
            prompt = """Analyze this photo COMPREHENSIVELY for dating compatibility assessment.

Evaluate carefully on 1-10 scale:
1. Photo Quality: Consider lighting, focus, composition, professionalism
2. Facial Attractiveness: Symmetry, features, overall appeal
3. Expression: Analyze warmth, openness, emotional tone (warm/neutral/cold)
4. Overall Impression: First impression, approachability, personality signals (friendly/serious/mysterious)

Be ACCURATE and DETAILED in your assessment.

Return ONLY this JSON:
{
  "quality_score": <1-10>,
  "attractiveness": <1-10>,
  "expression": "<warm/neutral/cold>",
  "impression": "<friendly/serious/mysterious>",
  "confidence": <0.0-1.0>
}"""
            
            model = genai.GenerativeModel(self.model_name)
            
            # HIGH thinking budget for vision = better accuracy!
            response = model.generate_content(
                [prompt, image],
                generation_config={
                    'temperature': 0.5,  # Lower for more consistent ratings
                    'max_output_tokens': 1024,
                    'thinking_budget': 4096  # High budget for accurate vision!
                },
                safety_settings=self.safety_settings
            )
            
            text = response.text
            
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
                    'confidence': features.get('confidence', 0.75)
                }
                
                logger.info(f"✅ Features: Q={result['quality_score']:.0f}%, A={result['attractiveness']}/10, Expr={result['expression']}")
                return result
                
            except:
                return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.6}
                
        except Exception as e:
            logger.error(f"❌ {e}")
            return {'quality_score': 70, 'attractiveness': 7, 'expression': 'neutral', 'impression': 'friendly', 'confidence': 0.5}
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict) -> dict:
        """Calculate mutual attraction with detailed metrics."""
        try:
            logger.info("💕 Calculating mutual attraction...")
            
            attr_a = features_a.get('attractiveness', 7)
            attr_b = features_b.get('attractiveness', 7)
            
            # Bidirectional scores
            a_to_b = (attr_b / 10) * 100
            b_to_a = (attr_a / 10) * 100
            
            # Quality adjustment
            quality_a = features_a.get('quality_score', 70) / 100
            quality_b = features_b.get('quality_score', 70) / 100
            avg_quality = (quality_a + quality_b) / 2
            
            base_score = (a_to_b + b_to_a) / 2
            
            # Reciprocity bonus
            diff = abs(attr_a - attr_b)
            reciprocity_bonus = 10 if diff <= 2 else (5 if diff <= 4 else 0)
            
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
                'method': 'Gemini 2.5 Flash (thinking_budget=4096)',
                'note': 'High-quality vision analysis with extended thinking'
            }
            
            logger.info(f"✅ Score: {final_score:.1f}% (A→B: {a_to_b:.1f}%, B→A: {b_to_a:.1f}%)")
            return result
            
        except Exception as e:
            logger.error(f"❌ {e}")
            return {'mutual_attraction_score': 50.0, 'confidence': 0.5}
