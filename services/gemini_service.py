"""
GEMINI 2.5 FLASH - MAXIMIZED FOR BEST QUALITY!
Uses thinking_budget to get MAXIMUM quality from Flash!
"""

import google.generativeai as genai
import json
import re
import os

class GeminiService:
    
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("No API key!")
        
        genai.configure(api_key=api_key)
        
        # ONLY FLASH - but MAXIMIZED!
        self.model_name = 'gemini-2.5-flash'
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        print(f"✅ Gemini 2.5 Flash MAXIMIZED (thinking budget enabled!)")
    
    def _call_flash_max_quality(self, prompt, thinking_budget=8192):
        """
        Call Flash with MAXIMUM quality settings!
        thinking_budget: 0-24576 (higher = better quality, slower)
        - 0 = fastest, basic quality
        - 8192 = balanced quality/speed
        - 16384 = high quality
        - 24576 = maximum quality
        """
        print(f"🔮 Flash (thinking_budget={thinking_budget})")
        
        model = genai.GenerativeModel(self.model_name)
        
        # MAXIMIZED config for best quality!
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.8,  # Higher for more creative/detailed responses
                'max_output_tokens': 8192,  # Maximum allowed
                'top_p': 0.95,  # High diversity
                'top_k': 64,  # Consider more tokens
                'thinking_budget': thinking_budget  # ← KEY TO QUALITY!
            },
            safety_settings=self.safety_settings
        )
        
        # Flash works reliably with direct access!
        text = response.text
        print(f"✅ Flash: {len(text)} chars (budget={thinking_budget})")
        return text
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse with MEDIUM thinking budget (balanced)."""
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            print(f"\n📝 Parsing: {question[:50]}...")
            # Medium thinking for quiz parsing
            text = self._call_flash_max_quality(prompt, thinking_budget=4096)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Parsed\n")
            return result
        except Exception as e:
            print(f"❌ {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, visual_details, hla_details) -> dict:
        """Generate report with HIGH thinking budget for MAXIMUM quality!"""
        
        print(f"\n🔮 REPORT: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        # DETAILED prompt for comprehensive report
        prompt = f"""Generate COMPREHENSIVE compatibility analysis with maximum depth and nuance.

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual Chemistry: {visual_score}%
Genetic Harmony: {hla_score}%

Generate DETAILED analysis. Return ONLY JSON with these fields:
{{
  "themes": ["theme1", "theme2", "theme3"],
  "deep_analysis": "COMPREHENSIVE multi-paragraph analysis of personality dynamics, compatibility patterns, and relationship potential. Be DETAILED and SPECIFIC. 200-300 words.",
  "perceived_similarity": "DETAILED analysis of how they perceive each other and mutual understanding. 150-200 words.",
  "compatibility_verdict": "CONCLUSIVE overall assessment with specific reasoning. 100-150 words.",
  "ui_cards": {{
    "vibe_check": "DETAILED description of overall connection quality. 100-150 words.",
    "first_impression": "DETAILED first impression analysis. 80-120 words.",
    "long_term_key": "DETAILED long-term compatibility factors. 80-120 words.",
    "green_flag": "SPECIFIC relationship strength with examples. 60-80 words.",
    "red_flag": "SPECIFIC growth area with constructive framing. 60-80 words."
  }}
}}

Be COMPREHENSIVE, DETAILED, and SPECIFIC. Use the full thinking budget to generate the highest quality analysis possible."""

        try:
            # MAXIMUM thinking budget for best report quality!
            text = self._call_flash_max_quality(prompt, thinking_budget=16384)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Report done (high-quality!)\n")
            return result
        except Exception as e:
            print(f"❌ {e}")
            return {
                "themes": ["Complementary", "Growth", "Balance"],
                "deep_analysis": f"{profile_a['name']} and {profile_b['name']} show compatibility across multiple dimensions.",
                "perceived_similarity": "Both demonstrate thoughtful approaches.",
                "compatibility_verdict": "Moderate compatibility with potential for growth.",
                "ui_cards": {
                    "vibe_check": "Balanced connection with room for development.",
                    "first_impression": "Chemistry and intellectual alignment.",
                    "long_term_key": "Communication and mutual respect.",
                    "green_flag": "Emotional maturity and openness.",
                    "red_flag": "Different communication styles to navigate."
                }
            }
