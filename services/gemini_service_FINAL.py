"""
Gemini Service - Complete with model fallbacks and API key from environment
Uses: Gemini 3 Pro (primary), 2.5 Pro (fallback), 2.5 Flash (fast fallback)
"""

import google.generativeai as genai
import json
import re
from config import Config

class GeminiService:
    """Service for personality analysis using Gemini AI with model fallbacks."""
    
    def __init__(self):
        """Initialize with API key from environment and set up models."""
        # Configure API key from environment variable
        if not Config.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not set in environment variables!")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Initialize models with fallback chain
        self.models = []
        for model_key in ['primary', 'fallback', 'fast_fallback']:
            model_name = Config.MODELS[model_key]
            try:
                model = genai.GenerativeModel(model_name)
                self.models.append({
                    'name': model_name,
                    'model': model,
                    'type': model_key
                })
                print(f"✅ {model_key.capitalize()} model initialized: {model_name}")
            except Exception as e:
                print(f"⚠️ Could not initialize {model_name}: {e}")
        
        if not self.models:
            raise ValueError("No Gemini models could be initialized!")
        
        print(f"✅ Gemini initialized with {len(self.models)} model(s)")
        
        # Timeout and generation config
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _call_with_fallback(self, prompt, timeout=None):
        """Call Gemini with automatic fallback to other models."""
        timeout = timeout or Config.REQUEST_TIMEOUT
        
        for model_info in self.models:
            try:
                print(f"🔮 Trying {model_info['name']}...")
                
                response = model_info['model'].generate_content(
                    prompt,
                    generation_config=self.generation_config,
                    request_options={'timeout': timeout}
                )
                
                print(f"✅ Response from {model_info['name']}")
                return response.text
                
            except Exception as e:
                print(f"⚠️ {model_info['name']} failed: {e}")
                if model_info == self.models[-1]:  # Last model
                    raise Exception(f"All models failed. Last error: {e}")
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse questionnaire response into sin scores."""
        
        prompt = f"""Analyze this response to determine personality traits on the Seven Deadly Sins framework.

Question: {question}
Response: {answer}

For EACH sin, provide:
- score: -5 (shows opposite) to +5 (shows the sin strongly)
- evidence: brief quote showing why

Return ONLY valid JSON (no markdown, no preamble):
{{
  "greed": {{"score": X, "evidence": "quote"}},
  "pride": {{"score": X, "evidence": "quote"}},
  "lust": {{"score": X, "evidence": "quote"}},
  "wrath": {{"score": X, "evidence": "quote"}},
  "gluttony": {{"score": X, "evidence": "quote"}},
  "envy": {{"score": X, "evidence": "quote"}},
  "sloth": {{"score": X, "evidence": "quote"}}
}}

IMPORTANT: Be nuanced. Most responses show mix of traits, not extremes."""

        try:
            response_text = self._call_with_fallback(prompt, Config.GENERATION_TIMEOUT)
            
            # Clean JSON
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            cleaned = cleaned.strip()
            
            result = json.loads(cleaned)
            return result
            
        except Exception as e:
            print(f"❌ Parse response error: {e}")
            # Return neutral scores as fallback
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """Generate comprehensive compatibility analysis."""
        
        print(f"🔮 STARTING generate_full_analysis for {profile_a['name']} & {profile_b['name']}")
        
        # Extract sin scores
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        print(f"📊 Extracted sin scores for both people")
        
        prompt = f"""Generate compatibility analysis for this couple:

{profile_a['name']}: {p1_sins}
{profile_b['name']}: {p2_sins}
Visual: {visual_score}%
HLA: {hla_score}%

Return ONLY valid JSON with these fields:
{{
  "themes": ["Theme 1", "Theme 2", "Theme 3"],
  "deep_analysis": "2-3 paragraph analysis",
  "perceived_similarity": "How they see each other",
  "compatibility_verdict": "One sentence verdict",
  "ui_cards": {{
    "vibe_check": "The overall vibe (2-3 sentences)",
    "first_impression": "Initial attraction dynamics (2-3 sentences)",
    "long_term_key": "What makes this work long-term (2-3 sentences)",
    "green_flag": "Biggest strength (1-2 sentences)",
    "red_flag": "Biggest challenge (1-2 sentences)"
  }}
}}"""

        try:
            print(f"📝 Sending to Gemini...")
            response_text = self._call_with_fallback(prompt, Config.REQUEST_TIMEOUT)
            print(f"📬 Received response from Gemini")
            
            # Clean and parse
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            cleaned = cleaned.strip()
            
            print(f"✂️ Cleaning JSON...")
            result = json.loads(cleaned)
            print(f"✅ Analysis complete! Fields: {list(result.keys())}")
            
            return result
            
        except Exception as e:
            print(f"❌ Full analysis error: {e}")
            import traceback
            traceback.print_exc()
            
            # Return default analysis
            return self._default_analysis(profile_a['name'], profile_b['name'])
    
    def _default_analysis(self, name1, name2):
        """Default analysis if Gemini fails."""
        return {
            "themes": ["Complementary Dynamics", "Shared Growth", "Balanced Energy"],
            "deep_analysis": f"{name1} and {name2} show potential for compatibility with balanced personality traits.",
            "perceived_similarity": "Both individuals demonstrate thoughtful approaches to relationships.",
            "compatibility_verdict": "Moderate to strong compatibility with room for growth.",
            "ui_cards": {
                "vibe_check": "A connection with balanced energy and mutual respect.",
                "first_impression": "Initial attraction based on complementary qualities.",
                "long_term_key": "Sustained compatibility through shared values and communication.",
                "green_flag": "Both show emotional maturity and self-awareness.",
                "red_flag": "May need to work on understanding different communication styles."
            }
        }
