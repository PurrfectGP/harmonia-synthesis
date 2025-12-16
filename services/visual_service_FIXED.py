"""
Visual Service - Fixed (NO request_options parameter)
"""

import google.generativeai as genai
import io
from PIL import Image
from config import Config
import json
import re

class VisualService:
    """Service for visual/image analysis using Gemini Vision."""
    
    def __init__(self):
        """Initialize with API key from Render environment."""
        if not Config.GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not set!")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Initialize vision models
        self.vision_models = []
        for model_name in [Config.MODELS['primary'], Config.MODELS['fallback'], Config.MODELS['fast_fallback']]:
            try:
                model = genai.GenerativeModel(model_name)
                self.vision_models.append({'name': model_name, 'model': model})
                print(f"✅ Vision: {model_name}")
            except Exception as e:
                print(f"⚠️ {model_name}: {e}")
        
        if not self.vision_models:
            raise ValueError("❌ No vision models!")
        
        print(f"✅ Visual service ready with {len(self.vision_models)} model(s)")
    
    def extract_features(self, image_data: bytes, gemini_service=None) -> dict:
        """Extract features from uploaded image."""
        return self.analyze_image(image_data, gemini_service)
    
    def analyze_image(self, image_data: bytes, gemini_service=None) -> dict:
        """Analyze image and extract features."""
        try:
            image = Image.open(io.BytesIO(image_data))
            width, height = image.size
            
            quality_score = min(100, (width * height) / 10000)
            
            vision_result = self._analyze_with_vision(image)
            
            return {
                'quality_score': round(quality_score, 1),
                'width': width,
                'height': height,
                **vision_result
            }
            
        except Exception as e:
            print(f"⚠️ Image analysis error: {e}")
            import traceback
            traceback.print_exc()
            return {
                'quality_score': 50.0,
                'error': str(e),
                'expression': 'neutral',
                'attractiveness': 5
            }
    
    def _analyze_with_vision(self, image):
        """Analyze image using Gemini Vision. NO request_options."""
        prompt = """Analyze this photo:
1. Facial expression
2. Overall impression
3. Attractiveness (1-10)

Return JSON:
{"expression": "...", "impression": "...", "attractiveness": X}"""
        
        for model_info in self.vision_models:
            try:
                print(f"📸 Analyzing with {model_info['name']}...")
                
                # NO request_options parameter!
                response = model_info['model'].generate_content([prompt, image])
                
                text = response.text.strip()
                text = re.sub(r'^```json\s*', '', text)
                text = re.sub(r'^```\s*', '', text)
                text = re.sub(r'\s*```$', '', text)
                
                result = json.loads(text.strip())
                print(f"✅ Vision complete: {model_info['name']}")
                
                return result
                
            except Exception as e:
                print(f"⚠️ {model_info['name']} failed: {str(e)[:50]}")
                if model_info == self.vision_models[-1]:
                    return {
                        'expression': 'neutral',
                        'impression': 'standard',
                        'attractiveness': 5
                    }
                continue
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict) -> dict:
        """Calculate mutual attraction score."""
        try:
            attr_a = features_a.get('attractiveness', 5)
            attr_b = features_b.get('attractiveness', 5)
            
            import math
            mutual_score = math.sqrt(attr_a * attr_b) * 10
            
            return {
                'mutual_attraction_score': round(mutual_score, 1),
                'confidence': 0.7,
                'method': 'vision_analysis',
                'person_a_attractiveness': attr_a,
                'person_b_attractiveness': attr_b,
                'person_a_expression': features_a.get('expression', 'N/A'),
                'person_b_expression': features_b.get('expression', 'N/A')
            }
        except Exception as e:
            print(f"⚠️ Mutual attraction error: {e}")
            return self.get_default_score()
    
    def get_default_score(self) -> dict:
        """Default when no images."""
        return {
            'mutual_attraction_score': 50.0,
            'confidence': 0.5,
            'method': 'default',
            'note': 'Visual analysis unavailable.'
        }
