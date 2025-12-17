"""
Gemini Service - Using NEW google-genai SDK (not legacy google-generativeai)
The old SDK was deprecated Nov 30, 2025!
"""

from google import genai
import json
import re
from config import Config

class GeminiService:
    """Service using NEW Google Gen AI SDK."""
    
    def __init__(self):
        """Initialize with NEW SDK."""
        if not Config.GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not set!")
        
        # NEW SDK client
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        
        # Model order: GEMINI 3 PRO FIRST!
        self.model_names = [
            Config.MODELS['primary'],      # gemini-3-pro-preview
            Config.MODELS['fallback'],     # gemini-2.5-pro
            Config.MODELS['fast_fallback'] # gemini-2.5-flash
        ]
        
        print(f"✅ NEW Gemini SDK initialized")
        print(f"   Models: {self.model_names}")
        
        self.config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _call_with_fallback(self, prompt):
        """Call using NEW SDK."""
        for i, model_name in enumerate(self.model_names):
            try:
                print(f"🔮 Attempt {i+1}: {model_name}")
                
                # NEW SDK method
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=self.config
                )
                
                # NEW SDK - response.text should work!
                text = response.text
                
                if not text or len(text.strip()) == 0:
                    raise Exception("Empty response")
                
                print(f"✅ SUCCESS: {len(text)} chars")
                return text
                
            except Exception as e:
                print(f"❌ {model_name} failed: {str(e)[:100]}")
                
                if i == len(self.model_names) - 1:
                    raise Exception(f"All models failed: {str(e)}")
                
                print(f"   → Next model...")
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse questionnaire response."""
        
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            print(f"\n📝 Parsing: {question[:50]}...")
            text = self._call_with_fallback(prompt)
            
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Parsed\n")
            return result
            
        except Exception as e:
            print(f"❌ Parse error: {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """Generate report."""
        
        print(f"\n🔮 REPORT: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        prompt = f"""Generate compatibility analysis. Return ONLY JSON:
{{"themes": ["...", "...", "..."], "deep_analysis": "...", "perceived_similarity": "...", "compatibility_verdict": "...", "ui_cards": {{"vibe_check": "...", "first_impression": "...", "long_term_key": "...", "green_flag": "...", "red_flag": "..."}}}}

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual: {visual_score}%, HLA: {hla_score}%"""

        try:
            text = self._call_with_fallback(prompt)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Report done\n")
            return result
            
        except Exception as e:
            print(f"❌ Report error: {e}")
            return {
                "themes": ["Complementary", "Growth", "Balance"],
                "deep_analysis": f"{profile_a['name']} and {profile_b['name']} show compatibility.",
                "perceived_similarity": "Both are thoughtful.",
                "compatibility_verdict": "Moderate compatibility.",
                "ui_cards": {
                    "vibe_check": "Balanced connection.",
                    "first_impression": "Chemistry and balance.",
                    "long_term_key": "Communication matters.",
                    "green_flag": "Emotional maturity.",
                    "red_flag": "Different styles."
                }
            }
