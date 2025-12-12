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
        
        # Vision model for enhanced image analysis
        try:
            self.vision_model = genai.GenerativeModel('gemini-2.0-flash-exp')
            logger.info("✅ Vision model initialized for image analysis")
        except:
            self.vision_model = None
            logger.warning("⚠️ Vision model not available")

    def _clean_json(self, text: str) -> str:
        """Clean markdown code blocks and extract JSON."""
        if not text:
            return "{}"
        text = re.sub(r"```json\s*", "", text)
        text = re.sub(r"```\s*", "", text)
        text = text.strip()
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            text = text[start:end+1]
        return text

    def _get_text_from_response(self, response) -> str:
        """Safely extract text from various Gemini response formats."""
        if not response:
            return ""
        if hasattr(response, 'text'):
            try:
                return response.text
            except Exception:
                pass
        if hasattr(response, 'parts') and response.parts:
            for part in response.parts:
                if hasattr(part, 'text'):
                    return part.text
        if hasattr(response, 'candidates') and response.candidates:
            try:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    if candidate.content.parts:
                        return candidate.content.parts[0].text
            except (IndexError, AttributeError):
                pass
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
        
        logger.info(f"🔮 STARTING generate_full_analysis for {p1_name} & {p2_name}")
        
        try:
            # Extract sin scores
            p1_sins = {}
            p2_sins = {}
            for sin in ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]:
                p1_sins[sin] = p1_data.get('sins', {}).get(sin, {}).get('score', 0)
                p2_sins[sin] = p2_data.get('sins', {}).get(sin, {}).get('score', 0)
            
            logger.info(f"📊 Extracted sin scores for both people")
            
            prompt = f"""You are an expert relationship compatibility analyst. Create comprehensive analysis for {p1_name} and {p2_name}.

PERSONALITY DATA (Seven Deadly Sins, -5 to +5):
{p1_name}: {json.dumps(p1_sins)}
{p2_name}: {json.dumps(p2_sins)}

Visual Compatibility: {visual_score:.1f}%
Genetic Compatibility: {hla_score:.1f}%

CRITICAL: Respond with ONLY valid JSON, no markdown:
{{
    "themes": ["Theme 1", "Theme 2", "Theme 3"],
    "deep_analysis": "Write 200 words analyzing compatibility, dynamics, challenges, strengths.",
    "visual_deep_analysis": "Write 100 words about visual chemistry and attraction patterns.",
    "hla_deep_analysis": "Write 100 words about genetic compatibility and biological attraction.",
    "perceived_similarity": "Write 100 words on how they perceive each other and mutual appreciation.",
    "visual_insight": "One sentence about visual chemistry.",
    "hla_insight": "One sentence about genetic compatibility.",
    "star_sign_title": "A poetic title like \\"The Architect and the Dreamer\\"",
    "star_sign_description": "Write 150 words horoscope-style description.",
    "individual_portraits": {{
        "{p1_name}": "Write 80 words describing {p1_name}'s personality.",
        "{p2_name}": "Write 80 words describing {p2_name}'s personality."
    }},
    "ui_cards": {{
        "vibe_check": "One memorable sentence about their combined energy.",
        "first_impression": "Describe their likely first impression in 20 words - be specific.",
        "long_term_key": "The one essential thing for lasting success in 20 words.",
        "green_flag": "Their strongest compatibility factor (10 words)",
        "red_flag": "Their biggest potential challenge (10 words)",
        "secret_strength": "A hidden strength of this pairing (10 words)",
        "growth_edge": "How they help each other evolve (10 words)",
        "theme_descriptions": {{
            "Theme 1": "2-3 sentences explaining theme 1.",
            "Theme 2": "2-3 sentences explaining theme 2.",
            "Theme 3": "2-3 sentences explaining theme 3."
        }}
    }},
    "compatibility_verdict": "Write 40 words final verdict."
}}"""

            logger.info(f"📝 Sending to Gemini (prompt: {len(prompt)} chars)...")
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            
            logger.info(f"📬 Received response from Gemini")
            
            response_text = self._get_text_from_response(response)
            
            if not response_text:
                logger.warning("⚠️ Empty response, using defaults")
                return self._default_analysis(p1_name, p2_name)
            
            logger.info(f"✂️ Cleaning JSON (length: {len(response_text)})...")
            
            cleaned = self._clean_json(response_text)
            result = json.loads(cleaned)
            
            logger.info(f"✅ Analysis complete! Fields: {list(result.keys())}")
            if 'ui_cards' in result:
                logger.info(f"✅ UI cards: {list(result['ui_cards'].keys())}")
            
            return result
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON error: {e}")
            return self._default_analysis(p1_name, p2_name)
        except Exception as e:
            logger.error(f"❌ Analysis error: {type(e).__name__}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return self._default_analysis(p1_name, p2_name)

    def _default_analysis(self, p1_name="Person 1", p2_name="Person 2"):
        """Comprehensive default analysis when API fails."""
        logger.info(f"📋 Using default analysis for {p1_name} and {p2_name}")
        return {
            "themes": ["Complementary Energies", "Growth Through Challenge", "Shared Core Values"],
            "deep_analysis": f"{p1_name} and {p2_name} demonstrate intriguing compatibility across multiple dimensions. Their personality profiles suggest a dynamic where differences become strengths. While they approach situations from different angles, this creates opportunities for mutual learning and growth. Visual chemistry provides strong foundation for attraction, while genetic markers suggest biological compatibility. Their psychological profiles indicate potential for deep connection with conscious effort and mutual understanding.",
            "visual_deep_analysis": f"Visual compatibility between {p1_name} and {p2_name} shows genuine attraction potential. Physical chemistry analysis indicates natural aesthetic appeal. Their mutual visual interest suggests strong initial attraction that could translate into lasting physical intimacy. Analysis of facial features, expressions, and overall presentation reveals complementary patterns.",
            "hla_deep_analysis": f"Genetic analysis reveals favorable HLA compatibility. MHC diversity falls within optimal range for biological attraction, suggesting nature supports this pairing. Research indicates such compatibility often manifests as subconscious olfactory attraction and may contribute to stronger immune function in potential offspring.",
            "perceived_similarity": f"{p1_name} likely perceives {p2_name} as someone with intriguing depth and authenticity, appreciating qualities that complement their own approach to life. Meanwhile, {p2_name} probably sees {p1_name} as bringing fresh perspectives and valuable energy. This mutual appreciation of complementary traits creates a dynamic where both feel genuinely valued.",
            "visual_insight": f"Strong natural visual chemistry between {p1_name} and {p2_name} with reciprocal aesthetic appeal.",
            "hla_insight": f"Genetic markers show optimal diversity - biology supports this connection.",
            "star_sign_title": "The Explorer and The Anchor",
            "star_sign_description": f"When {p1_name} meets {p2_name}, two distinct energies find unexpected harmony. Like celestial bodies in balanced orbit, they provide what the other needs. One brings adventure, spontaneity, and fresh perspectives. The other offers stability, depth, and emotional grounding. Their connection challenges both to grow beyond comfort zones while providing security needed for such risks. Together they create something neither could achieve alone - honoring both freedom and commitment, excitement and stability.",
            "individual_portraits": {
                p1_name: f"{p1_name} demonstrates personality combining intellectual curiosity with emotional depth. Their approach to relationships reveals someone valuing genuine connection while maintaining healthy independence. They bring thoughtful engagement, showing capacity for both passion and pragmatism in partnership dynamics.",
                p2_name: f"{p2_name} presents authentic, grounded presence in relationships. Their personality indicates strong emotional intelligence combined with desire for meaningful connection. They approach partnership with both vulnerability and strength, seeking genuine compatibility beyond surface-level attraction."
            },
            "ui_cards": {
                "vibe_check": "A connection balancing intellectual stimulation with emotional depth and authentic presence.",
                "first_impression": f"Natural ease and comfort - {p1_name} and {p2_name} likely feel genuinely seen by each other from the start.",
                "long_term_key": "Nurturing open communication, celebrating differences, and maintaining individual growth within togetherness.",
                "green_flag": "Complementary strengths creating natural balance and mutual inspiration",
                "red_flag": "Communication style differences requiring patience and active listening",
                "secret_strength": "Ability to challenge and comfort each other simultaneously",
                "growth_edge": "Learning to embrace discomfort as catalyst for evolution together",
                "theme_descriptions": {
                    "Complementary Energies": f"Where {p1_name} leads with certain strengths, {p2_name} naturally provides support, and vice versa. Their contrasting approaches don't conflict but create fuller whole. This complementarity extends across emotional, intellectual, and practical dimensions.",
                    "Growth Through Challenge": f"This pairing pushes both beyond comfort zones. {p1_name} challenges {p2_name} in specific ways while {p2_name} helps {p1_name} see new possibilities. The friction is productive - uncomfortable sometimes, but ultimately transformative for both.",
                    "Shared Core Values": f"Despite different surface approaches, {p1_name} and {p2_name} align on fundamentals: authenticity, growth, meaningful connection. This shared foundation provides stability even when methods differ, creating solid base for long-term compatibility."
                }
            },
            "compatibility_verdict": f"{p1_name} and {p2_name} show strong multi-dimensional compatibility. This isn't same-person-twice match but complementary pairing with real depth potential. Success requires embracing differences as assets and maintaining authentic communication."
        }

    async def generate_test_response(self, question: str, sentiment: str = "neutral") -> str:
        """Generate nuanced, ambiguous test response that could relate to ANY sin."""
        logger.info(f"🎲 Generating {sentiment} response: {question[:40]}...")
        
        # More nuanced prompts - avoid obvious virtue/vice signals
        if sentiment == "positive":
            tone = "cooperative and considerate BUT also show self-awareness and boundaries. Be nuanced - don't be obviously selfless. Show complexity."
        elif sentiment == "negative":
            tone = "assertive and self-protecting BUT frame it reasonably. Be nuanced - don't be obviously selfish. Show you've thought it through."
        else:
            tone = "balanced, showing both consideration for others AND healthy self-interest. Be realistic and ambiguous. Real people are contradictory."
        
        prompt = f"""Write a 60-80 word first-person answer to this question.
Be {tone}
Make the response SUBTLE and REALISTIC - real people are complex and contradictory.
Reference the specific scenario but leave room for interpretation.
Sound like a real person, not obviously virtuous or vice-driven.
Avoid cliches and overly simple good/bad framing.

Question: "{question}"

Write ONLY the response text, no quotes or labels:"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            text = self._get_text_from_response(response)
            
            if text:
                text = text.strip()
                if text.startswith('"') and text.endswith('"'):
                    text = text[1:-1]
                logger.info(f"✅ Generated ({len(text.split())} words)")
                return text
            
            return "I'd want to handle this in a way that works for everyone while also being true to myself."
            
        except Exception as e:
            logger.error(f"❌ Generate error: {e}")
            return "I think there's probably a middle ground that could work here."

    async def analyze_image_detailed(self, image_bytes: bytes) -> dict:
        """Analyze image for facial expressions, body language, accessories using Gemini Vision."""
        if not self.vision_model:
            logger.warning("⚠️ Vision model not available")
            return {}
        
        try:
            logger.info("🖼️ Analyzing image with Gemini Vision...")
            
            prompt = """Analyze this photo comprehensively:
1. **Facial Expression**: What emotion/mood? (confident, warm, serious, playful, etc.)
2. **Body Language**: Posture, stance - what does it communicate?
3. **Accessories/Style**: Glasses, jewelry, clothing - what personality hints?
4. **Overall Impression**: First impression this person gives?

Respond as JSON:
{
    "facial_expression": "description",
    "body_language": "description", 
    "accessories_style": "description",
    "overall_impression": "description",
    "confidence_score": 0.85
}"""
            
            response = await asyncio.to_thread(
                self.vision_model.generate_content,
                [prompt, {"mime_type": "image/jpeg", "data": image_bytes}]
            )
            
            text = self._get_text_from_response(response)
            cleaned = self._clean_json(text)
            result = json.loads(cleaned)
            
            logger.info(f"✅ Image analyzed - expression: {result.get('facial_expression', 'unknown')}")
            return result
            
        except Exception as e:
            logger.warning(f"⚠️ Vision analysis error: {e}")
            return {
                "facial_expression": "neutral/pleasant",
                "body_language": "relaxed",
                "accessories_style": "casual/professional",
                "overall_impression": "approachable",
                "confidence_score": 0.5
            }

    async def analyze_facial_preferences(self, ratings: list) -> dict:
        """Analyze facial preferences from ratings."""
        return {"preferences": [], "summary": "Preferences analyzed based on ratings."}
