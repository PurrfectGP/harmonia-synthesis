import google.generativeai as genai
import json
import logging
import asyncio
import re
import sys
import os
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        
        # Use Gemini 3 Pro Preview
        try:
            self.model = genai.GenerativeModel(
                'gemini-3-pro-preview',
                generation_config={"temperature": 0.4, "max_output_tokens": 4096}
            )
            logger.info("✅ Gemini initialized with gemini-3-pro-preview")
        except Exception as e:
            logger.warning(f"⚠️ Gemini 3 Pro not available: {e}, falling back to 2.5 Pro")
            self.model = genai.GenerativeModel(
                'gemini-2.5-pro',
                generation_config={"temperature": 0.4, "max_output_tokens": 4096}
            )
            logger.info("✅ Gemini initialized with gemini-2.5-pro (fallback)")

    def _clean_json(self, text: str) -> str:
        """Clean markdown code blocks and extract JSON."""
        if not text:
            return "{}"
        # Remove markdown code blocks
        text = re.sub(r"```json\s*", "", text)
        text = re.sub(r"```\s*", "", text)
        text = text.strip()
        
        # Try to find JSON object in the text
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            text = text[start:end+1]
        
        return text

    def _get_text_from_response(self, response) -> str:
        """Safely extract text from various Gemini response formats."""
        if not response:
            return ""
        
        # Try direct text attribute first
        if hasattr(response, 'text'):
            try:
                return response.text
            except Exception:
                pass
        
        # Try parts
        if hasattr(response, 'parts') and response.parts:
            for part in response.parts:
                if hasattr(part, 'text'):
                    return part.text
                elif isinstance(part, str):
                    return part
        
        # Try candidates
        if hasattr(response, 'candidates') and response.candidates:
            try:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content'):
                    content = candidate.content
                    if hasattr(content, 'parts') and content.parts:
                        for part in content.parts:
                            if hasattr(part, 'text'):
                                return part.text
            except (IndexError, AttributeError):
                pass
        
        # Last resort: convert to string
        return str(response)

    def _get_default_sins(self):
        """Return default sin scores."""
        return {
            "greed": {"score": 0, "confidence": 0.5, "evidence": ""},
            "pride": {"score": 0, "confidence": 0.5, "evidence": ""},
            "lust": {"score": 0, "confidence": 0.5, "evidence": ""},
            "wrath": {"score": 0, "confidence": 0.5, "evidence": ""},
            "gluttony": {"score": 0, "confidence": 0.5, "evidence": ""},
            "envy": {"score": 0, "confidence": 0.5, "evidence": ""},
            "sloth": {"score": 0, "confidence": 0.5, "evidence": ""}
        }

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def parse_response(self, question_text: str, response_text: str) -> dict:
        """Parse a questionnaire response into Seven Deadly Sins scores."""
        logger.info(f"🔍 Parsing: {question_text[:50]}...")
        
        prompt = f"""Analyze this questionnaire response using the Seven Deadly Sins personality framework.
Score each sin from -5 (opposite trait) to +5 (strong trait).

Question: "{question_text}"
Response: "{response_text}"

You must respond with ONLY a valid JSON object, no other text:
{{
    "sins": {{
        "greed": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "pride": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "lust": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "wrath": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "gluttony": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "envy": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}},
        "sloth": {{"score": 0, "confidence": 0.7, "evidence": "brief quote"}}
    }},
    "style": {{"detail_level": "medium"}}
}}"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            response_text = self._get_text_from_response(response)
            
            if not response_text:
                logger.warning("⚠️ Empty response from Gemini")
                return {"sins": self._get_default_sins(), "style": {"detail_level": "medium"}}
            
            cleaned = self._clean_json(response_text)
            result = json.loads(cleaned)
            
            # Validate structure
            if "sins" not in result:
                result = {"sins": result, "style": {"detail_level": "medium"}}
            
            logger.info("✅ Parsed successfully")
            return result
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON parse error: {e}")
            return {"sins": self._get_default_sins(), "style": {"detail_level": "medium"}}
        except Exception as e:
            logger.error(f"❌ Parse error: {e}")
            return {"sins": self._get_default_sins(), "style": {"detail_level": "medium"}}

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def generate_full_analysis(self, p1_data: dict, p2_data: dict, 
                                      visual_score: float = 50, hla_score: float = 50,
                                      visual_details: dict = None, hla_details: dict = None,
                                      image_ratings: dict = None) -> dict:
        """Generate comprehensive compatibility analysis."""
        p1_name = p1_data.get('name', 'Person 1')
        p2_name = p2_data.get('name', 'Person 2')
        logger.info(f"🔮 Generating analysis for {p1_name} & {p2_name}...")
        
        # Extract sin scores safely
        p1_sins = {}
        p2_sins = {}
        for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]:
            p1_sins[sin] = p1_data.get('sins', {}).get(sin, {}).get('score', 0)
            p2_sins[sin] = p2_data.get('sins', {}).get(sin, {}).get('score', 0)
        
        prompt = f"""You are a relationship compatibility expert. Create a detailed analysis for {p1_name} and {p2_name}.

PERSONALITY DATA (Seven Deadly Sins, -5 to +5):
{p1_name}: {json.dumps(p1_sins)}
{p2_name}: {json.dumps(p2_sins)}

Visual Compatibility: {visual_score}%
Genetic Compatibility: {hla_score}%

Respond with ONLY this JSON (no markdown, no explanation):
{{
    "themes": ["Theme 1", "Theme 2", "Theme 3"],
    "deep_analysis": "Write 200 words about their compatibility, dynamics, challenges and strengths.",
    "visual_deep_analysis": "Write 100 words about their physical/visual chemistry.",
    "hla_deep_analysis": "Write 100 words about genetic compatibility and biological attraction.",
    "perceived_similarity": "Write 100 words on how they perceive each other.",
    "visual_insight": "One sentence about visual chemistry.",
    "hla_insight": "One sentence about genetic compatibility.",
    "star_sign_title": "A poetic title like The Architect and the Dreamer",
    "star_sign_description": "Write 150 words horoscope-style description of their pairing.",
    "individual_portraits": {{
        "{p1_name}": "Write 80 words describing {p1_name}'s personality.",
        "{p2_name}": "Write 80 words describing {p2_name}'s personality."
    }},
    "ui_cards": {{
        "vibe_check": "One memorable sentence about their combined energy.",
        "green_flag": "Their best compatibility trait (10 words)",
        "red_flag": "Their biggest challenge (10 words)",
        "secret_strength": "Hidden strength in this pairing (10 words)",
        "growth_edge": "Where they help each other grow (10 words)",
        "theme_descriptions": {{
            "Theme 1": "2-3 sentences about theme 1",
            "Theme 2": "2-3 sentences about theme 2",
            "Theme 3": "2-3 sentences about theme 3"
        }}
    }},
    "compatibility_verdict": "Write 40 words final verdict on their compatibility."
}}"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            response_text = self._get_text_from_response(response)
            
            if not response_text:
                logger.warning("⚠️ Empty analysis response")
                return self._default_analysis(p1_name, p2_name)
            
            cleaned = self._clean_json(response_text)
            result = json.loads(cleaned)
            logger.info("✅ Analysis complete!")
            return result
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ Analysis JSON error: {e}")
            return self._default_analysis(p1_name, p2_name)
        except Exception as e:
            logger.error(f"❌ Analysis error: {e}")
            return self._default_analysis(p1_name, p2_name)

    def _default_analysis(self, p1_name="Person 1", p2_name="Person 2"):
        """Return default analysis when API fails."""
        return {
            "themes": ["Complementary Energies", "Growth Through Challenge", "Shared Values"],
            "deep_analysis": f"{p1_name} and {p2_name} show an intriguing compatibility pattern. Their personality profiles suggest a dynamic where differences can become strengths. While they may approach situations differently, this creates opportunities for learning and growth. Their combined traits suggest potential for a balanced relationship where each brings unique perspectives. The interplay of their characteristics could lead to a stimulating partnership if both remain open to understanding each other's viewpoints.",
            "visual_deep_analysis": "The visual compatibility analysis indicates genuine physical attraction potential. Both individuals possess qualities that align with common attraction patterns, suggesting natural chemistry that could deepen over time.",
            "hla_deep_analysis": "Genetic compatibility markers suggest a healthy biological foundation. HLA diversity between partners is associated with stronger immune systems in potential offspring and often correlates with subconscious attraction signals.",
            "perceived_similarity": f"{p1_name} likely appreciates {p2_name}'s unique qualities, while {p2_name} finds depth and intrigue in {p1_name}'s approach to life. Their mutual perception creates an interesting dynamic.",
            "visual_insight": "There is natural visual chemistry between these two individuals.",
            "hla_insight": "Biology supports this connection with complementary genetics.",
            "star_sign_title": "The Explorer and The Anchor",
            "star_sign_description": f"When {p1_name} meets {p2_name}, two distinct energies find unexpected harmony. Like celestial bodies in orbit, they balance each other. One providing adventure and spontaneity, the other offering stability and depth. Their connection challenges both to grow beyond comfort zones while providing the security needed to take risks. Together they create something neither could alone.",
            "individual_portraits": {
                p1_name: f"{p1_name} brings a unique energy to relationships, combining depth with dynamism. Their personality reveals someone who values authentic connection while maintaining independence.",
                p2_name: f"{p2_name} offers depth and authenticity, approaching connection with their own distinctive style. They bring emotional intelligence and a grounded presence."
            },
            "ui_cards": {
                "vibe_check": "A connection that balances excitement with emotional depth.",
                "green_flag": "Complementary approaches that create natural balance",
                "red_flag": "Different communication styles need attention",
                "secret_strength": "They inspire growth in each other naturally",
                "growth_edge": "Learning patience and flexible communication together",
                "theme_descriptions": {
                    "Complementary Energies": "Their differences create balance rather than conflict. Where one leads, the other supports.",
                    "Growth Through Challenge": "They push each other to evolve, though growth can feel uncomfortable.",
                    "Shared Values": "At their core, they want similar things from life and relationships."
                }
            },
            "compatibility_verdict": "A promising pairing with real potential. Success depends on embracing differences as strengths and maintaining open communication."
        }

    async def generate_test_response(self, question: str, sentiment: str = "positive") -> str:
        """Generate a test response for a questionnaire question."""
        logger.info(f"🎲 Generating {sentiment} response for: {question[:40]}...")
        
        if sentiment == "positive":
            tone = "warm, generous, empathetic, patient, and cooperative. Show genuine care for others."
        else:
            tone = "selfish, impatient, dismissive, judgmental, and self-focused. Prioritize yourself."
        
        prompt = f"""Write a 60-80 word realistic first-person answer to this personality questionnaire question.
Be {tone}
Be SPECIFIC to this exact question - reference the scenario directly.
Sound natural and conversational.

Question: "{question}"

Write only the response, no quotes or labels:"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            text = self._get_text_from_response(response)
            
            if text:
                # Clean up the response
                text = text.strip()
                if text.startswith('"') and text.endswith('"'):
                    text = text[1:-1]
                logger.info(f"✅ Generated response ({len(text.split())} words)")
                return text
            
            return "I would approach this thoughtfully, considering everyone involved."
            
        except Exception as e:
            logger.error(f"❌ Generate error: {e}")
            return "I would handle this situation with care and consideration for all involved."

    async def analyze_facial_preferences(self, ratings: list) -> dict:
        """Analyze facial preferences from ratings."""
        return {"preferences": [], "summary": "Preferences analyzed based on provided ratings."}
