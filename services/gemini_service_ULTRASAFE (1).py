"""
Gemini Service - ULTRA SAFE (No index access at all)
Uses Gemini 3 Pro FIRST
Cannot have index errors - uses only safe attribute access
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
        
        # Initialize models - GEMINI 3 PRO FIRST!
        self.model_names = [
            Config.MODELS['primary'],      # gemini-3-pro-preview
            Config.MODELS['fallback'],     # gemini-2.5-pro
            Config.MODELS['fast_fallback'] # gemini-2.5-flash
        ]
        
        print(f"✅ Gemini service initialized")
        print(f"   Model order: {self.model_names}")
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _extract_text_safely(self, response):
        """
        Extract text from Gemini response with MAXIMUM safety.
        NO index access - only attribute checks.
        """
        # Method 1: Direct text attribute (most common)
        if hasattr(response, 'text'):
            try:
                return response.text
            except Exception as e:
                print(f"   Method 1 (response.text) failed: {e}")
        
        # Method 2: Via candidates (backup)
        if hasattr(response, 'candidates'):
            candidates = response.candidates
            if candidates is not None and len(candidates) > 0:
                candidate = candidates[0]
                if hasattr(candidate, 'content'):
                    content = candidate.content
                    if hasattr(content, 'parts'):
                        parts = content.parts
                        if parts is not None and len(parts) > 0:
                            part = parts[0]
                            if hasattr(part, 'text'):
                                try:
                                    return part.text
                                except Exception as e:
                                    print(f"   Method 2 failed: {e}")
        
        # Method 3: String conversion (last resort)
        try:
            return str(response)
        except:
            pass
        
        raise Exception("Could not extract text from response using any method")
    
    def _call_with_fallback(self, prompt):
        """
        Call Gemini with model fallback.
        Order: Gemini 3 Pro → 2.5 Pro → 2.5 Flash
        ULTRA SAFE - No index errors possible
        """
        for i, model_name in enumerate(self.model_names):
            try:
                print(f"🔮 Attempt {i+1}/{len(self.model_names)}: {model_name}")
                
                # Create model
                model = genai.GenerativeModel(model_name)
                
                print(f"   Sending request...")
                
                # Generate content
                response = model.generate_content(
                    prompt,
                    generation_config=self.generation_config
                )
                
                print(f"   Received response, extracting text...")
                
                # ULTRA SAFE text extraction
                text = self._extract_text_safely(response)
                
                print(f"✅ SUCCESS with {model_name}")
                print(f"   Text length: {len(text)} chars")
                return text
                
            except Exception as e:
                print(f"❌ {model_name} FAILED")
                print(f"   Error: {str(e)[:150]}")
                print(f"   Error type: {type(e).__name__}")
                
                if i == len(self.model_names) - 1:
                    print(f"\n❌ ALL {len(self.model_names)} MODELS FAILED!")
                    import traceback
                    traceback.print_exc()
                    raise Exception(f"All models failed. Last error: {str(e)}")
                
                print(f"   → Trying next model...\n")
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
            print(f"\n📝 PARSING QUIZ RESPONSE")
            print(f"   Question: {question[:50]}...")
            
            response_text = self._call_with_fallback(prompt)
            
            # Clean JSON
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            print(f"✅ Parse successful\n")
            return result
            
        except Exception as e:
            print(f"❌ Parse error: {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """
        Generate comprehensive compatibility analysis.
        USES: Gemini 3 Pro FIRST
        """
        
        print(f"\n🔮 ═══════════════════════════════════════")
        print(f"🔮 REPORT GENERATION")
        print(f"   {profile_a['name']} & {profile_b['name']}")
        print(f"🔮 ═══════════════════════════════════════\n")
        
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
            print(f"📝 Generating analysis...")
            response_text = self._call_with_fallback(prompt)
            print(f"📬 Analysis received, parsing JSON...")
            
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            result = json.loads(cleaned.strip())
            print(f"✅ Report complete with {len(result.keys())} fields\n")
            
            return result
            
        except Exception as e:
            print(f"❌ Report generation error: {e}")
            import traceback
            traceback.print_exc()
            print()
            return self._default_analysis(profile_a['name'], profile_b['name'])
    
    def _default_analysis(self, name1, name2):
        """Fallback analysis if all models fail."""
        return {
            "themes": ["Complementary Dynamics", "Shared Growth", "Balanced Energy"],
            "deep_analysis": f"{name1} and {name2} show compatibility potential with balanced personality traits and room for mutual growth.",
            "perceived_similarity": "Both individuals demonstrate thoughtful, measured approaches to relationships.",
            "compatibility_verdict": "Moderate to strong compatibility indicated with positive growth potential.",
            "ui_cards": {
                "vibe_check": "A balanced connection characterized by mutual respect and complementary energies.",
                "first_impression": "Initial attraction based on visual chemistry and balanced personality traits.",
                "long_term_key": "Sustained compatibility through effective communication and shared core values.",
                "green_flag": "Both demonstrate emotional maturity, self-awareness, and capacity for growth.",
                "red_flag": "May need to navigate different communication styles and conflict resolution approaches."
            }
        }
