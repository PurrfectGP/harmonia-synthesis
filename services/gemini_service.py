"""
Gemini Service - FLASH MAXIMIZED (NO thinking_budget)
OLD SDK compatible - maximizes quality without thinking_budget!
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
        
        self.model_name = 'gemini-2.5-flash'
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        print(f"✅ Gemini 2.5 Flash MAXIMIZED (OLD SDK - no thinking_budget)")
    
    def _call_flash_maxed(self, prompt, max_tokens=8192, temp=0.7):
        """
        Call Flash with MAXIMIZED settings for OLD SDK!
        NO thinking_budget (not supported in OLD SDK)
        Instead: optimize temp, tokens, top_p, top_k
        """
        print(f"🔮 Flash (temp={temp}, tokens={max_tokens})")
        
        model = genai.GenerativeModel(self.model_name)
        
        # MAXIMIZED config WITHOUT thinking_budget!
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': temp,
                'max_output_tokens': max_tokens,
                'top_p': 0.95,
                'top_k': 64
                # NO thinking_budget - not in OLD SDK!
            },
            safety_settings=self.safety_settings
        )
        
        # Flash works with direct text access
        text = response.text
        print(f"✅ Flash: {len(text)} chars")
        return text
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse quiz responses."""
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            print(f"\n📝 Parsing: {question[:50]}...")
            # Moderate temp for consistent parsing
            text = self._call_flash_maxed(prompt, max_tokens=4096, temp=0.6)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Parsed\n")
            return result
        except Exception as e:
            print(f"❌ {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, visual_details, hla_details) -> dict:
        """Generate COMPREHENSIVE report - maximized for quality!"""
        
        print(f"\n🔮 REPORT: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        # COMPREHENSIVE prompt requesting DETAILED analysis
        prompt = f"""Generate COMPREHENSIVE compatibility analysis with MAXIMUM DEPTH AND DETAIL.

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual Chemistry: {visual_score}%
Genetic Harmony: {hla_score}%

Generate the MOST DETAILED analysis possible. Return ONLY JSON:
{{
  "themes": ["detailed theme 1", "detailed theme 2", "detailed theme 3"],
  "deep_analysis": "COMPREHENSIVE multi-paragraph analysis (200-300 words). Be DETAILED, SPECIFIC, and INSIGHTFUL about personality dynamics, compatibility patterns, relationship potential, complementary traits, growth areas, and overall synergy.",
  "perceived_similarity": "DETAILED analysis (150-200 words) of mutual perception, understanding, how they see each other, common ground, and areas of difference.",
  "compatibility_verdict": "CONCLUSIVE assessment (100-150 words) with specific reasoning, evidence, and clear conclusions about relationship viability.",
  "ui_cards": {{
    "vibe_check": "DETAILED connection quality description (100-150 words). Be specific about energy, dynamics, mutual respect.",
    "first_impression": "DETAILED first impression analysis (80-120 words). What would they notice first? How would initial interactions feel?",
    "long_term_key": "DETAILED long-term factors (80-120 words). What makes or breaks sustained compatibility?",
    "green_flag": "SPECIFIC strength with concrete examples (60-80 words). What's genuinely positive?",
    "red_flag": "SPECIFIC growth area with constructive framing (60-80 words). What needs attention?"
  }}
}}

Use ALL available context. Be COMPREHENSIVE, DETAILED, SPECIFIC, and INSIGHTFUL. Generate the HIGHEST QUALITY analysis possible."""

        try:
            # HIGH temp + MAX tokens for comprehensive analysis
            text = self._call_flash_maxed(prompt, max_tokens=8192, temp=0.8)
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Report (COMPREHENSIVE!)\n")
            return result
        except Exception as e:
            print(f"❌ {e}")
            return {
                "themes": ["Complementary Dynamics", "Shared Growth Potential", "Balanced Energy"],
                "deep_analysis": f"{profile_a['name']} and {profile_b['name']} demonstrate compatibility across multiple dimensions of personality and values.",
                "perceived_similarity": "Both individuals show thoughtful approaches to life and relationships.",
                "compatibility_verdict": "Moderate to strong compatibility with clear potential for meaningful connection.",
                "ui_cards": {
                    "vibe_check": "Balanced connection with authentic mutual respect.",
                    "first_impression": "Natural chemistry balanced with intellectual alignment.",
                    "long_term_key": "Strong communication foundation and shared values.",
                    "green_flag": "Emotional maturity and genuine openness to growth.",
                    "red_flag": "Different communication styles that require awareness."
                }
            }
