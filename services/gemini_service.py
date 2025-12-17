"""
Gemini Service - DIAGNOSTIC VERSION
Prints EVERYTHING about response to find the issue
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
        
        # GEMINI 3 PRO FIRST!
        self.model_names = [
            Config.MODELS['primary'],
            Config.MODELS['fallback'],
            Config.MODELS['fast_fallback']
        ]
        
        print(f"✅ Models: {self.model_names}")
        
        self.safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE',
        }
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'max_output_tokens': 8192,
        }
    
    def _diagnose_response(self, response):
        """Print EVERYTHING about the response object."""
        print(f"\n   🔍 DIAGNOSING RESPONSE OBJECT:")
        print(f"      Type: {type(response)}")
        print(f"      Dir: {[x for x in dir(response) if not x.startswith('_')][:10]}")
        
        if hasattr(response, 'candidates'):
            print(f"      Has candidates: YES")
            candidates = response.candidates
            print(f"      Candidates type: {type(candidates)}")
            print(f"      Candidates is None: {candidates is None}")
            
            if candidates is not None:
                print(f"      Candidates length: {len(candidates)}")
                
                if len(candidates) > 0:
                    candidate = candidates[0]
                    print(f"      Candidate[0] type: {type(candidate)}")
                    print(f"      Candidate[0] attrs: {[x for x in dir(candidate) if not x.startswith('_')][:10]}")
                    
                    if hasattr(candidate, 'finish_reason'):
                        print(f"      Finish reason: {candidate.finish_reason}")
                    
                    if hasattr(candidate, 'content'):
                        print(f"      Has content: YES")
                        content = candidate.content
                        print(f"      Content type: {type(content)}")
                        print(f"      Content is None: {content is None}")
                        
                        if content is not None:
                            print(f"      Content attrs: {[x for x in dir(content) if not x.startswith('_')][:10]}")
                            
                            if hasattr(content, 'parts'):
                                print(f"      Has parts: YES")
                                parts = content.parts
                                print(f"      Parts type: {type(parts)}")
                                print(f"      Parts is None: {parts is None}")
                                
                                if parts is not None:
                                    print(f"      Parts length: {len(parts)}")
                                    
                                    if len(parts) > 0:
                                        part = parts[0]
                                        print(f"      Part[0] type: {type(part)}")
                                        print(f"      Part[0] attrs: {[x for x in dir(part) if not x.startswith('_')][:10]}")
                                        
                                        if hasattr(part, 'text'):
                                            text = part.text
                                            print(f"      Part text length: {len(text) if text else 'None'}")
                                            print(f"      Part text preview: {text[:100] if text else 'None'}")
                                    else:
                                        print(f"      ❌ Parts is EMPTY LIST!")
                            else:
                                print(f"      ❌ NO parts attribute!")
                    else:
                        print(f"      ❌ NO content attribute!")
                else:
                    print(f"      ❌ Candidates is EMPTY LIST!")
        else:
            print(f"      ❌ NO candidates attribute!")
        
        print(f"   🔍 END DIAGNOSIS\n")
    
    def _call_with_fallback(self, prompt):
        """Call with diagnostic output."""
        for i, model_name in enumerate(self.model_names):
            try:
                print(f"\n🔮 Attempt {i+1}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                
                response = model.generate_content(
                    prompt,
                    generation_config=self.generation_config,
                    safety_settings=self.safety_settings
                )
                
                print(f"   ✅ Response object received")
                
                # DIAGNOSE THE RESPONSE
                self._diagnose_response(response)
                
                # Try to extract
                text = response.candidates[0].content.parts[0].text
                
                print(f"✅ SUCCESS: {len(text)} chars")
                return text
                
            except Exception as e:
                print(f"❌ FAILED: {str(e)}")
                
                if i == len(self.model_names) - 1:
                    raise
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse response."""
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            text = self._call_with_fallback(prompt)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            return json.loads(cleaned)
        except:
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
            return json.loads(cleaned)
        except:
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
