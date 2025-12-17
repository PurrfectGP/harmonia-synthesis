"""
Gemini Service - Complete Fix
NO request_options parameter (not supported)
Uses Gemini 3 Pro → 2.5 Pro → 2.5 Flash fallbacks
"""

import google.generativeai as genai
import json
import re
from config import Config

class GeminiService:
    """Service for personality analysis using Gemini AI."""
    
    def __init__(self):
        """Initialize with API key from Render environment."""
        if not Config.GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not set!")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Initialize models
        self.models = []
        for model_key in ['primary', 'fallback', 'fast_fallback']:
            model_name = Config.MODELS[model_key]
            try:
                model = genai.GenerativeModel(model_name)
                self.models.append({'name': model_name, 'model': model})
                print(f"✅ {model_key.title()}: {model_name}")
            except Exception as e:
                print(f"⚠️ {model_name} init failed: {e}")
        
        if not self.models:
            raise ValueError("❌ No models available!")
        
        print(f"✅ Gemini ready with {len(self.models)} model(s)")
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _call_with_fallback(self, prompt):
        """Call Gemini with model fallback. NO request_options."""
        for i, model_info in enumerate(self.models):
            try:
                print(f"🔮 Attempt {i+1}: {model_info['name']}")
                
                # NO request_options parameter!
                response = model_info['model'].generate_content(
                    prompt,
                    generation_config=self.generation_config
                )
                
                print(f"✅ Response from {model_info['name']}")
                return response.text
                
            except Exception as e:
                print(f"⚠️ {model_info['name']} failed: {str(e)[:100]}")
                if i == len(self.models) - 1:
                    raise Exception(f"All models failed. Last: {str(e)}")
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse questionnaire response into sin scores."""
        
        prompt = f"""Analyze this response for Seven Deadly Sins framework.

Question: {question}
Response: {answer}

For EACH sin, provide score (-5 to +5) and evidence:

Return ONLY valid JSON:
{{
  "greed": {{"score": X, "evidence": "quote"}},
  "pride": {{"score": X, "evidence": "quote"}},
  "lust": {{"score": X, "evidence": "quote"}},
  "wrath": {{"score": X, "evidence": "quote"}},
  "gluttony": {{"score": X, "evidence": "quote"}},
  "envy": {{"score": X, "evidence": "quote"}},
  "sloth": {{"score": X, "evidence": "quote"}}
}}

Be nuanced."""

        try:
            response_text = self._call_with_fallback(prompt)
            
            # Clean JSON
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            return result
            
        except Exception as e:
            print(f"❌ Parse error: {e}")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """Generate comprehensive compatibility analysis."""
        
        print(f"🔮 Generating analysis: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        prompt = f"""Generate compatibility analysis:

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual: {visual_score}%
HLA: {hla_score}%

Return ONLY valid JSON:
{{
  "themes": ["3 themes"],
  "deep_analysis": "2-3 paragraphs",
  "perceived_similarity": "1-2 sentences",
  "compatibility_verdict": "1 sentence",
  "ui_cards": {{
    "vibe_check": "2-3 sentences",
    "first_impression": "2-3 sentences",
    "long_term_key": "2-3 sentences",
    "green_flag": "1-2 sentences",
    "red_flag": "1-2 sentences"
  }}
}}"""

        try:
            response_text = self._call_with_fallback(prompt)
            
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            print(f"✅ Analysis complete")
            
            return result
            
        except Exception as e:
            print(f"❌ Analysis error: {e}")
            import traceback
            traceback.print_exc()
            return self._default_analysis(profile_a['name'], profile_b['name'])
    
    def _default_analysis(self, name1, name2):
        """Fallback analysis."""
        return {
            "themes": ["Complementary Dynamics", "Shared Growth", "Balanced Energy"],
            "deep_analysis": f"{name1} and {name2} show compatibility potential with balanced traits.",
            "perceived_similarity": "Both demonstrate thoughtful approaches.",
            "compatibility_verdict": "Moderate to strong compatibility indicated.",
            "ui_cards": {
                "vibe_check": "A balanced connection with mutual respect.",
                "first_impression": "Attraction based on chemistry and balance.",
                "long_term_key": "Compatibility through communication and values.",
                "green_flag": "Both show emotional maturity.",
                "red_flag": "May need to work on communication styles."
            }
        }
