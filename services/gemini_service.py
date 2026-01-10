"""
Gemini Service - FORCED DETAILED REPORTS
Uses verbose prompts to force comprehensive analysis!
"""

import google.generativeai as genai
import json
import re
import os

class GeminiService:
    # Available models
    AVAILABLE_MODELS = {
        'gemini-3-pro-preview': 'Gemini 3 Pro',
        'gemini-3-flash-preview': 'Gemini 3 Flash',
        'gemini-2.5-pro': 'Gemini 2.5 Pro',
        'gemini-2.5-flash': 'Gemini 2.5 Flash',
    }

    def __init__(self, model_name: str = None):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("No API key!")

        genai.configure(api_key=api_key)

        # Use environment variable or default to Gemini 3 Pro (most advanced)
        self.model_name = model_name or os.getenv('GEMINI_MODEL', 'gemini-3-pro-preview')

        # Validate model name
        if self.model_name not in self.AVAILABLE_MODELS:
            print(f"⚠️  Unknown model '{self.model_name}', falling back to gemini-3-pro-preview")
            self.model_name = 'gemini-3-pro-preview'

        # Fallback chain: Gemini 3 Pro → 2.5 Pro → 2.5 Flash
        self.fallback_models = ['gemini-2.5-pro', 'gemini-2.5-flash']

        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]

        print(f"✅ {self.AVAILABLE_MODELS[self.model_name]} initialized (fallback: {' → '.join(self.fallback_models)})")

    def _generate_with_fallback(self, prompt, generation_config, images=None):
        """Try to generate content with primary model, fall back to alternatives if needed."""
        models_to_try = [self.model_name] + self.fallback_models

        for model_name in models_to_try:
            try:
                print(f"🔮 Trying {self.AVAILABLE_MODELS.get(model_name, model_name)}...")
                model = genai.GenerativeModel(model_name)

                if images:
                    response = model.generate_content([prompt] + images, generation_config=generation_config, safety_settings=self.safety_settings)
                else:
                    response = model.generate_content(prompt, generation_config=generation_config, safety_settings=self.safety_settings)

                text = self._extract_text_safely(response)
                if text:
                    print(f"✅ Success with {self.AVAILABLE_MODELS.get(model_name, model_name)}")
                    return text

                print(f"⚠️  {self.AVAILABLE_MODELS.get(model_name, model_name)} returned empty, trying next...")

            except Exception as e:
                print(f"⚠️  {self.AVAILABLE_MODELS.get(model_name, model_name)} failed: {e}")
                if model_name == models_to_try[-1]:  # Last model
                    raise
                print(f"   Trying fallback model...")

        return None

    def _extract_text_safely(self, response) -> str:
        """Safely extract text from Gemini response, handling blocked/empty responses."""
        try:
            # Check if response has candidates
            if not response.candidates:
                print("⚠️  No candidates in response")
                return None

            # Check the first candidate
            candidate = response.candidates[0]

            # Check finish reason
            finish_reason = candidate.finish_reason
            if finish_reason == 2:  # SAFETY
                print(f"⚠️  Response blocked by safety filters")
                return None
            elif finish_reason == 3:  # RECITATION
                print(f"⚠️  Response blocked due to recitation")
                return None
            elif finish_reason not in [0, 1]:  # 0=UNSPECIFIED, 1=STOP (normal completion)
                print(f"⚠️  Unexpected finish_reason: {finish_reason}")
                return None

            # Try to get text
            if hasattr(candidate.content, 'parts') and candidate.content.parts:
                text = ''.join(part.text for part in candidate.content.parts if hasattr(part, 'text'))
                if text.strip():
                    return text.strip()

            # Fallback to response.text if available
            if hasattr(response, 'text') and response.text:
                return response.text.strip()

            print("⚠️  Response has no text content")
            return None

        except Exception as e:
            print(f"⚠️  Error extracting text: {e}")
            return None
    
    async def parse_response(self, question: str, answer: str) -> dict:
        """Parse quiz."""
        prompt = f"""Analyze for Seven Deadly Sins. Return ONLY JSON:
{{"greed": {{"score": X, "evidence": "..."}}, "pride": {{"score": X, "evidence": "..."}}, "lust": {{"score": X, "evidence": "..."}}, "wrath": {{"score": X, "evidence": "..."}}, "gluttony": {{"score": X, "evidence": "..."}}, "envy": {{"score": X, "evidence": "..."}}, "sloth": {{"score": X, "evidence": "..."}}}}

Question: {question}
Response: {answer}"""

        try:
            print(f"\n📝 Parsing: {question[:50]}...")

            text = self._generate_with_fallback(
                prompt,
                generation_config={'temperature': 0.6, 'max_output_tokens': 4096}
            )

            if not text:
                print(f"❌ All models returned empty responses\n")
                return {sin: {'score': 0, 'evidence': 'N/A'} for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]}

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
            text = self._generate_with_fallback(
                prompt,
                generation_config={
                    'temperature': 0.85,  # High for detailed content
                    'max_output_tokens': 8192  # Maximum for long analysis
                }
            )

            if not text:
                print(f"❌ All models returned empty responses, using fallback\n")
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
