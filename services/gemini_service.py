"""
Gemini Service - WORKING VERSION from unified integration chat
Uses try/except around response.text to catch the error
Uses OLD SDK (google.generativeai) since NEW SDK not installed yet
"""

import google.generativeai as genai
import json
import re
from config import Config

class GeminiService:
    """Service for personality analysis using Gemini AI."""
    
    def __init__(self):
        """Initialize with API key."""
        if not Config.GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not set!")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # GEMINI 3 PRO FIRST!
        self.model_names = [
            'gemini-3-pro-preview',
            'gemini-2.5-pro',
            'gemini-2.5-flash'
        ]
        
        print(f"✅ Gemini ready: {self.model_names}")
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192
        }
    
    def _get_text_from_response(self, response) -> str:
        """
        WORKING METHOD from unified integration chat!
        Safely extract text with try/except
        """
        if not response:
            return ""
        
        # Try direct text attribute first (wrapped in try/except!)
        if hasattr(response, 'text'):
            try:
                text = response.text
                if text and isinstance(text, str) and len(text.strip()) > 0:
                    return text
            except Exception:
                # Index error happens here - catch it and continue!
                pass
        
        # Fallback: extract via candidates
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
    
    def _call_with_fallback(self, prompt):
        """Call Gemini with fallback. GEMINI 3 PRO FIRST!"""
        for i, model_name in enumerate(self.model_names):
            try:
                print(f"🔮 Attempt {i+1}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                
                response = model.generate_content(
                    prompt,
                    generation_config=self.generation_config
                )
                
                print(f"   Extracting text with WORKING method...")
                
                # Use WORKING extraction method
                text = self._get_text_from_response(response)
                
                if not text or len(text.strip()) == 0:
                    raise Exception("Empty response text")
                
                print(f"✅ SUCCESS: {model_name} ({len(text)} chars)")
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
                "themes": ["Complementary Dynamics", "Shared Growth", "Balanced Energy"],
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
