"""
Gemini Service - SIMPLIFIED (No complex async)
Uses Gemini 3 Pro FIRST
NO request_options, NO complex async wrapping
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
        
        # Initialize models in CORRECT ORDER
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
        print(f"   Model order: {[m['name'] for m in self.models]}")
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _call_with_fallback(self, prompt):
        """
        Call Gemini with model fallback.
        Order: Gemini 3 Pro → 2.5 Pro → 2.5 Flash
        NO complex async, NO request_options
        """
        for i, model_info in enumerate(self.models):
            try:
                print(f"🔮 Attempt {i+1}/{len(self.models)}: {model_info['name']}")
                
                # Simple synchronous call
                response = model_info['model'].generate_content(
                    prompt,
                    generation_config=self.generation_config
                )
                
                # SAFE text extraction
                try:
                    text = response.text
                except Exception as text_error:
                    print(f"   ⚠️ response.text failed: {text_error}")
                    # Try alternative extraction
                    if hasattr(response, 'candidates') and response.candidates:
                        if hasattr(response.candidates[0], 'content'):
                            if hasattr(response.candidates[0].content, 'parts'):
                                if response.candidates[0].content.parts:
                                    text = response.candidates[0].content.parts[0].text
                                else:
                                    raise Exception("Empty parts list")
                            else:
                                raise Exception("No parts attribute")
                        else:
                            raise Exception("No content attribute")
                    else:
                        raise Exception("No candidates")
                
                print(f"✅ SUCCESS with {model_info['name']}")
                return text
                
            except Exception as e:
                print(f"❌ {model_info['name']} failed: {str(e)[:100]}")
                print(f"   Error type: {type(e).__name__}")
                
                if i == len(self.models) - 1:
                    import traceback
                    print("   Full traceback:")
                    traceback.print_exc()
                    raise Exception(f"All models failed. Last error: {str(e)}")
                
                print(f"   → Trying next model...")
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """
        Parse questionnaire response into sin scores.
        USES: Gemini 3 Pro FIRST
        """
        
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
            print(f"📝 Parsing response for: {question[:50]}...")
            response_text = self._call_with_fallback(prompt)
            
            # Clean JSON
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            print(f"✅ Parsed successfully")
            return result
            
        except Exception as e:
            print(f"❌ Parse error: {e}")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """
        Generate comprehensive compatibility analysis.
        USES: Gemini 3 Pro FIRST
        """
        
        print(f"🔮 REPORT GENERATION: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        prompt = f"""Generate comprehensive compatibility analysis:

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual Chemistry: {visual_score}%
Genetic Harmony: {hla_score}%

Return ONLY valid JSON:
{{
  "themes": ["3 connection themes"],
  "deep_analysis": "2-3 detailed paragraphs analyzing compatibility",
  "perceived_similarity": "How they perceive each other (1-2 sentences)",
  "compatibility_verdict": "Clear one-sentence verdict",
  "ui_cards": {{
    "vibe_check": "Overall relationship vibe (2-3 sentences)",
    "first_impression": "Initial attraction dynamics (2-3 sentences)",
    "long_term_key": "Long-term compatibility factor (2-3 sentences)",
    "green_flag": "Biggest relationship strength (1-2 sentences)",
    "red_flag": "Biggest challenge to address (1-2 sentences)"
  }}
}}"""

        try:
            print(f"📝 Generating full analysis...")
            response_text = self._call_with_fallback(prompt)
            print(f"📬 Analysis received")
            
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            print(f"✅ Report complete with {len(result.keys())} fields")
            
            return result
            
        except Exception as e:
            print(f"❌ Report generation error: {e}")
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
