"""
Visual Service - Using NEW google-genai SDK
"""

from google import genai  # NEW SDK!
import io
from PIL import Image
from config import Config
import json
import re

class VisualService:
    """Service for visual/image analysis using NEW SDK."""
    
    def __init__(self):
        """Initialize with NEW SDK."""
        if not Config.GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not set!")
        
        # NEW SDK client
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        
        # Vision models
        self.model_names = [
            Config.MODELS['primary'],
            Config.MODELS['fallback'],
            Config.MODELS['fast_fallback']
        ]
        
        print(f"✅ Visual service with NEW SDK")
        print(f"   Models: {self.model_names}")
    
    def extract_features(self, image_data: bytes, gemini_service=None) -> dict:
        """Extract features from uploaded image."""
        return self.analyze_image(image_data, gemini_service)
    
    def analyze_image(self, image_data: bytes, gemini_service=None) -> dict:
        """Analyze image."""
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
            return {
                'quality_score': 50.0,
                'error': str(e),
                'expression': 'neutral',
                'attractiveness': 5
            }
    
    def _analyze_with_vision(self, image):
        """Analyze image using NEW SDK."""
        import base64
        from io import BytesIO
        
        # Convert PIL image to base64
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode()
        
        prompt = """Analyze this photo:
1. Facial expression
2. Overall impression  
3. Attractiveness (1-10)

Return JSON:
{"expression": "...", "impression": "...", "attractiveness": X}"""
        
        for model_name in self.model_names:
            try:
                print(f"📸 Analyzing with {model_name}...")
                
                # NEW SDK with image
                from google.genai import types
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=[
                        types.Part.from_text(text=prompt),
                        types.Part.from_bytes(
                            data=img_bytes,
                            mime_type='image/jpeg'
                        )
                    ]
                )
                
                text = response.text.strip()
                text = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text)
                result = json.loads(text.strip())
                
                print(f"✅ Vision: {model_name}")
                return result
                
            except Exception as e:
                print(f"⚠️ {model_name} vision failed: {str(e)[:50]}")
                continue
        
        # All failed
        return {
            'expression': 'neutral',
            'impression': 'standard',
            'attractiveness': 5
        }
    
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
