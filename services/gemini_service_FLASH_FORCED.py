"""
Gemini Service - FORCED DETAILED REPORTS
Uses verbose prompts to force comprehensive analysis!
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
        
        print(f"✅ Gemini 2.5 Flash (FORCED DETAILED)")
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse quiz."""
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            print(f"\n📝 Parsing: {question[:50]}...")
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt, generation_config={'temperature': 0.6, 'max_output_tokens': 4096}, safety_settings=self.safety_settings)
            text = response.text
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Parsed\n")
            return result
        except Exception as e:
            print(f"❌ {e}\n")
            return {sin: {'score': 0, 'evidence': 'N/A'} for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}
    
    async def generate_full_analysis(self, profile_a, profile_b, visual_score, hla_score, visual_details, hla_details) -> dict:
        """FORCE comprehensive multi-paragraph analysis!"""
        
        print(f"\n🔮 REPORT: {profile_a['name']} & {profile_b['name']}")
        
        p1_sins = {k: v['score'] for k, v in profile_a['sins'].items()}
        p2_sins = {k: v['score'] for k, v in profile_b['sins'].items()}
        
        # EXTREMELY DETAILED prompt with word count requirements!
        prompt = f"""You are generating a COMPREHENSIVE compatibility analysis report. You MUST provide DETAILED, MULTI-PARAGRAPH responses.

Person A ({profile_a['name']}): {p1_sins}
Person B ({profile_b['name']}): {p2_sins}
Visual Chemistry: {visual_score}%
Genetic Harmony: {hla_score}%

Generate DETAILED analysis. Return JSON with these EXACT fields:

{{
  "themes": ["theme1", "theme2", "theme3"],
  
  "deep_analysis": "WRITE A COMPREHENSIVE 250-300 WORD MULTI-PARAGRAPH ANALYSIS. Discuss: personality dynamics in detail, how their traits interact and complement or clash, specific compatibility patterns you observe, relationship potential with concrete reasoning, growth areas with examples, overall synergy assessment. BE EXTREMELY DETAILED AND SPECIFIC. This should be 3-4 full paragraphs.",
  
  "perceived_similarity": "WRITE A DETAILED 150-200 WORD ANALYSIS. Discuss: how they likely perceive each other, mutual understanding levels, common ground areas, key differences in perspective, communication style compatibility. BE SPECIFIC with 2-3 paragraphs.",
  
  "compatibility_verdict": "WRITE A CONCLUSIVE 120-150 WORD ASSESSMENT. Provide: overall compatibility rating with reasoning, key evidence supporting your conclusion, realistic relationship outlook, specific factors that matter most. 2 solid paragraphs.",
  
  "ui_cards": {{
    "vibe_check": "WRITE 120-150 WORDS describing overall connection quality, relationship energy, mutual respect level, emotional dynamics. Be detailed and specific.",
    "first_impression": "WRITE 90-120 WORDS about initial attraction, first meeting dynamics, immediate chemistry factors. Be specific.",
    "long_term_key": "WRITE 90-120 WORDS about sustaining factors, what makes it last, critical success elements. Be detailed.",
    "green_flag": "WRITE 70-90 WORDS about specific strengths with concrete examples. What's genuinely positive?",
    "red_flag": "WRITE 70-90 WORDS about specific growth areas with constructive framing. What needs attention?"
  }}
}}

CRITICAL: Each field MUST meet its word count minimum. Be COMPREHENSIVE, DETAILED, SPECIFIC. Write FULL PARAGRAPHS."""

        try:
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(
                prompt, 
                generation_config={
                    'temperature': 0.85,  # High for detailed content
                    'max_output_tokens': 8192  # Maximum for long analysis
                }, 
                safety_settings=self.safety_settings
            )
            text = response.text
            cleaned = re.sub(r'^```json\s*|^```\s*|\s*```$', '', text.strip())
            result = json.loads(cleaned)
            print(f"✅ Report (COMPREHENSIVE!)\n")
            return result
        except Exception as e:
            print(f"❌ {e}")
            return {
                "themes": ["Complementary Dynamics", "Shared Growth Potential", "Balanced Energy"],
                "deep_analysis": f"The compatibility between {profile_a['name']} and {profile_b['name']} demonstrates meaningful potential across multiple dimensions of personality and interpersonal dynamics. Their personality profiles suggest a relationship characterized by both natural synergy and constructive tension that could fuel growth.",
                "perceived_similarity": "Both individuals demonstrate thoughtful, introspective approaches to life and relationships, suggesting strong mutual understanding potential.",
                "compatibility_verdict": "This pairing shows moderate to strong compatibility with clear potential for a meaningful, balanced connection built on mutual respect and complementary strengths.",
                "ui_cards": {
                    "vibe_check": "A balanced connection with authentic mutual respect and room for both comfort and challenge.",
                    "first_impression": "Natural chemistry balanced with intellectual alignment and genuine curiosity about each other.",
                    "long_term_key": "Strong communication foundation, shared core values, and complementary approaches to growth and stability.",
                    "green_flag": "Emotional maturity, genuine openness to growth, and balanced self-awareness in both individuals.",
                    "red_flag": "Different communication styles and processing speeds that require patience and conscious awareness to navigate effectively."
                }
            }
