"""
Gemini Service - Uses generate_content with safety settings
Gemini 3/2.5 Pro returning empty? Try with safety settings adjusted
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
        
        # Model order: GEMINI 3 PRO FIRST!
        self.model_names = [
            Config.MODELS['primary'],      # gemini-3-pro-preview
            Config.MODELS['fallback'],     # gemini-2.5-pro
            Config.MODELS['fast_fallback'] # gemini-2.5-flash
        ]
        
        print(f"✅ Gemini service initialized")
        print(f"   Model order: {self.model_names}")
        
        # Relaxed safety settings (might be blocking responses)
        self.safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE',
        }
        
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 8192,
        }
    
    def _extract_text_safe(self, response):
        """Extract text safely from response."""
        # Check candidates exists and has content
        if not hasattr(response, 'candidates'):
            raise Exception("No candidates attribute")
        
        if not response.candidates:
            raise Exception("candidates is None or empty")
        
        if len(response.candidates) == 0:
            raise Exception("candidates list is empty (length 0)")
        
        candidate = response.candidates[0]
        
        # Check finish reason
        if hasattr(candidate, 'finish_reason'):
            reason = str(candidate.finish_reason)
            print(f"   Finish reason: {reason}")
            if reason in ['SAFETY', 'RECITATION', 'OTHER']:
                raise Exception(f"Response blocked: {reason}")
        
        # Check content
        if not hasattr(candidate, 'content'):
            raise Exception("No content attribute in candidate")
        
        if not candidate.content:
            raise Exception("content is None")
        
        # Check parts
        if not hasattr(candidate.content, 'parts'):
            raise Exception("No parts attribute in content")
        
        if not candidate.content.parts:
            raise Exception("parts is None")
        
        if len(candidate.content.parts) == 0:
            raise Exception("parts list is empty (length 0)")
        
        # Get text from first part
        part = candidate.content.parts[0]
        
        if not hasattr(part, 'text'):
            raise Exception("No text attribute in part")
        
        text = part.text
        
        if not text:
            raise Exception("text is None or empty string")
        
        if len(text.strip()) == 0:
            raise Exception("text is only whitespace")
        
        return text.strip()
    
    def _call_with_fallback(self, prompt):
        """
        Call Gemini with model fallback.
        Uses relaxed safety settings.
        """
        for i, model_name in enumerate(self.model_names):
            try:
                print(f"🔮 Attempt {i+1}/{len(self.model_names)}: {model_name}")
                
                model = genai.GenerativeModel(model_name)
                
                print(f"   Generating with safety_settings...")
                
                # Include safety settings to prevent blocking
                response = model.generate_content(
                    prompt,
                    generation_config=self.generation_config,
                    safety_settings=self.safety_settings
                )
                
                print(f"   Received response object")
                print(f"   Extracting text via candidates...")
                
                text = self._extract_text_safe(response)
                
                print(f"✅ SUCCESS with {model_name} ({len(text)} chars)")
                return text
                
            except Exception as e:
                print(f"❌ {model_name} FAILED: {str(e)}")
                
                if i == len(self.model_names) - 1:
                    print(f"\n❌ ALL MODELS FAILED!")
                    import traceback
                    traceback.print_exc()
                    raise Exception(f"All models failed. Last: {str(e)}")
                
                print(f"   → Next model...\n")
                continue
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse questionnaire response. Uses Gemini 3 Pro FIRST."""
        
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
            print(f"\n📝 Parsing: {question[:50]}...")
            response_text = self._call_with_fallback(prompt)
            
            # Clean JSON
            cleaned = response_text.strip()
            cleaned = re.sub(r'^```json\s*', '', cleaned)
            cleaned = re.sub(r'^```\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
            
            if not cleaned:
                raise Exception("Empty response after cleaning")
            
            result = json.loads(cleaned)
            print(f"✅ Parse successful\n")
            return result
            
        except Exception as e:
            print(f"❌ Parse failed: {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in 
                   ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, 
                                     visual_details, hla_details) -> dict:
        """Generate report. Uses Gemini 3 Pro FIRST."""
        
        print(f"\n🔮 REPORT: {profile_a['name']} & {profile_b['name']}")
        
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
            
            if not cleaned:
                raise Exception("Empty response")
            
            result = json.loads(cleaned)
            print(f"✅ Report complete\n")
            return result
            
        except Exception as e:
            print(f"❌ Report error: {e}")
            import traceback
            traceback.print_exc()
            return self._default_analysis(profile_a['name'], profile_b['name'])
    
    def _default_analysis(self, name1, name2):
        """Fallback analysis."""
        return {
            "themes": ["Complementary Dynamics", "Shared Growth", "Balanced Energy"],
            "deep_analysis": f"{name1} and {name2} show compatibility potential with balanced traits and room for growth.",
            "perceived_similarity": "Both demonstrate thoughtful, measured approaches to relationships.",
            "compatibility_verdict": "Moderate to strong compatibility indicated with positive potential.",
            "ui_cards": {
                "vibe_check": "A balanced connection with mutual respect and complementary energy.",
                "first_impression": "Attraction based on visual chemistry and personality balance.",
                "long_term_key": "Sustained compatibility through communication and shared values.",
                "green_flag": "Both demonstrate emotional maturity and self-awareness.",
                "red_flag": "May need to navigate different communication styles."
            }
        }
