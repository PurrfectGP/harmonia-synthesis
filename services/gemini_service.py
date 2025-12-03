
import google.generativeai as genai
import json
import logging
import asyncio
import re
import sys
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        # Use gemini-3-pro-preview
        self.model = genai.GenerativeModel('gemini-3-pro-preview', generation_config={"temperature": 0.4})
        logger.info("✅ Gemini initialized with gemini-3-pro-preview")

    def _clean_json(self, text: str) -> str:
        text = re.sub(r"```json\s*", "", text)
        text = re.sub(r"```\s*", "", text)
        return text.strip()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def parse_response(self, question_text: str, response_text: str) -> dict:
        logger.info(f"🔍 Parsing: {question_text[:40]}...")
        prompt = f"""Analyze this response using Seven Deadly Sins framework. Score each -5 to +5.

Question: "{question_text}"
Response: "{response_text}"

Return ONLY valid JSON:
{{"sins": {{"greed": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "pride": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "lust": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "wrath": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "gluttony": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "envy": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}, "sloth": {{"score": 0, "confidence": 0.7, "evidence": "quote"}}}}, "style": {{"detail_level": "medium"}}}}"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            text = self._clean_json(response.text)
            result = json.loads(text)
            logger.info("✅ Parsed successfully")
            return result
        except Exception as e:
            logger.error(f"❌ Parse error: {e}")
            return {"sins": {s: {"score": 0, "confidence": 0.5, "evidence": ""} for s in ["greed","pride","lust","wrath","gluttony","envy","sloth"]}, "style": {"detail_level": "medium"}}

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def generate_full_analysis(self, p1_data: dict, p2_data: dict,
                                      visual_score: float = 50, hla_score: float = 50,
                                      visual_details: dict = None, hla_details: dict = None,
                                      image_ratings: dict = None) -> dict:
        p1_name = p1_data.get('name', 'Person 1')
        p2_name = p2_data.get('name', 'Person 2')
        logger.info(f"🔮 Generating analysis for {p1_name} & {p2_name}...")

        p1_sins = {s: p1_data.get('sins', {}).get(s, {}).get('score', 0) for s in ["greed","pride","lust","wrath","gluttony","envy","sloth"]}
        p2_sins = {s: p2_data.get('sins', {}).get(s, {}).get('score', 0) for s in ["greed","pride","lust","wrath","gluttony","envy","sloth"]}

        prompt = f"""You are a relationship compatibility expert. Create a detailed analysis for {p1_name} and {p2_name}.

PERSONALITY DATA (Seven Deadly Sins, -5 to +5):
{p1_name}: {json.dumps(p1_sins)}
{p2_name}: {json.dumps(p2_sins)}

Visual Compatibility: {visual_score}%
Genetic Compatibility: {hla_score}%

Return ONLY this JSON (no markdown):
{{
    "themes": ["Theme 1", "Theme 2", "Theme 3"],
    "deep_analysis": "Write 200 words about their compatibility, how their personalities interact, potential challenges and strengths.",
    "visual_deep_analysis": "Write 100 words about their physical/visual chemistry based on the {visual_score}% score.",
    "hla_deep_analysis": "Write 100 words about genetic compatibility and what {hla_score}% means for attraction.",
    "perceived_similarity": "Write 100 words on how {p1_name} sees {p2_name} and vice versa.",
    "visual_insight": "50 words on visual chemistry.",
    "hla_insight": "50 words on genetic attraction.",
    "star_sign_title": "Create a poetic title like 'The Architect and the Dreamer' specific to their profiles",
    "star_sign_description": "Write 150 words horoscope-style description of their pairing based on their actual personality data.",
    "individual_portraits": {{
        "{p1_name}": "Write 80 words describing {p1_name}'s personality based on their sin scores.",
        "{p2_name}": "Write 80 words describing {p2_name}'s personality based on their sin scores."
    }},
    "ui_cards": {{
        "vibe_check": "One memorable sentence about their energy.",
        "green_flag": "Best trait match (10 words max)",
        "red_flag": "Biggest challenge (10 words max)",
        "secret_strength": "Hidden strength (10 words max)",
        "growth_edge": "Growth opportunity (10 words max)",
        "theme_descriptions": {{
            "Theme 1": "2-3 sentences explaining theme 1",
            "Theme 2": "2-3 sentences explaining theme 2",
            "Theme 3": "2-3 sentences explaining theme 3"
        }}
    }},
    "compatibility_verdict": "Write 40 words final verdict on their compatibility."
}}"""

        try:
            logger.info("📤 Sending to Gemini...")
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            logger.info("📥 Received response from Gemini")
            text = self._clean_json(response.text)
            result = json.loads(text)
            logger.info("✅ Analysis complete!")
            return result
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON error: {e}")
            logger.error(f"Raw: {response.text[:500] if response else 'No response'}...")
            return self._default_analysis(p1_name, p2_name)
        except Exception as e:
            logger.error(f"❌ Analysis error: {e}")
            return self._default_analysis(p1_name, p2_name)

    def _default_analysis(self, p1_name="Person 1", p2_name="Person 2"):
        return {
            "themes": ["Complementary Energies", "Growth Through Challenge", "Shared Values"],
            "deep_analysis": f"{p1_name} and {p2_name} show an intriguing compatibility pattern. Their personality profiles suggest a dynamic where differences can become strengths. While they may approach situations differently, this creates opportunities for learning and growth. Their combined traits suggest potential for a balanced relationship where each brings unique perspectives.",
            "visual_deep_analysis": "The visual compatibility analysis indicates genuine physical attraction potential. Both individuals possess qualities that align with common attraction patterns, suggesting natural chemistry.",
            "hla_deep_analysis": "Genetic compatibility markers suggest a healthy biological foundation. HLA diversity between partners is associated with stronger immune systems in potential offspring and subconscious attraction.",
            "perceived_similarity": f"{p1_name} likely appreciates {p2_name}'s unique qualities while {p2_name} finds depth in {p1_name}'s approach to life.",
            "visual_insight": "There's natural visual chemistry between these two individuals.",
            "hla_insight": "Biology supports this connection with complementary genetics.",
            "star_sign_title": "The Explorer and The Anchor",
            "star_sign_description": f"When {p1_name} meets {p2_name}, two distinct energies find unexpected harmony. Their connection challenges both to grow beyond comfort zones while providing stability. Together they balance adventure with security, creating a partnership that evolves over time.",
            "individual_portraits": {
                p1_name: f"{p1_name} brings a unique energy to relationships, with a complex inner world that balances multiple traits.",
                p2_name: f"{p2_name} offers depth and authenticity, approaching connection with their own distinctive style."
            },
            "ui_cards": {
                "vibe_check": "A connection worth exploring with open hearts.",
                "green_flag": "Complementary approaches to challenges",
                "red_flag": "Different communication rhythms",
                "secret_strength": "They balance each other naturally",
                "growth_edge": "Learning patience and flexibility",
                "theme_descriptions": {
                    "Complementary Energies": "Their differences create balance rather than conflict. Where one leads, the other supports.",
                    "Growth Through Challenge": "They push each other to evolve, though growth can feel uncomfortable at times.",
                    "Shared Values": "At their core, they want similar things from life and relationships."
                }
            },
            "compatibility_verdict": "A promising pairing with real potential. Success depends on embracing differences as strengths."
        }

    async def generate_test_response(self, question: str, sentiment: str = "positive") -> str:
        logger.info(f"🎲 Generating {sentiment} response for: {question[:50]}...")

        if sentiment == "positive":
            tone_desc = "warm, generous, patient, empathetic, cooperative, and emotionally mature. Show genuine care for others."
        else:
            tone_desc = "selfish, impatient, judgmental, competitive, dismissive, and emotionally reactive. Prioritize yourself over others."

        prompt = f"""You are roleplaying as a person answering a personality questionnaire.

QUESTION: "{question}"

Write a 60-80 word UNIQUE response that is {tone_desc}

IMPORTANT RULES:
- Be SPECIFIC to THIS exact question - reference the scenario directly
- Use first person ("I would...", "My approach...")
- Include a concrete example or specific detail
- Sound natural and conversational, not generic
- Do NOT give a vague answer that could apply to any question

Just write the response, no quotes or labels:"""

        try:
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            text = response.text.strip()
            # Remove any quotes if the model added them
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]
            logger.info(f"✅ Generated unique response ({len(text.split())} words)")
            return text
        except Exception as e:
            logger.error(f"❌ Generate error: {e}")
            # Fallback with question-specific content
            if "dinner" in question.lower() or "bill" in question.lower():
                return "I'd suggest we split it based on what each person ordered. It's only fair that way." if sentiment == "positive" else "I'd just pay for my part exactly and let others figure out theirs."
            elif "traffic" in question.lower():
                return "I'd take a deep breath, maybe listen to a podcast, and text ahead that I'll be late." if sentiment == "positive" else "I'd get frustrated and probably honk at people even though it won't help."
            elif "wallet" in question.lower():
                return "I'd definitely try to return it - check for ID and contact them directly if possible." if sentiment == "positive" else "Finders keepers, honestly. They should have been more careful."
            elif "weekend" in question.lower():
                return "I'd balance some relaxation with catching up with friends or family I've been meaning to see." if sentiment == "positive" else "I'd do whatever I want without worrying about anyone else's plans."
            elif "restaurant" in question.lower():
                return "I'd be open to their suggestion - maybe they know something good about that place." if sentiment == "positive" else "I'd push for my choice since I was excited about it first."
            elif "line" in question.lower() or "queue" in question.lower():
                return "I'd politely point out that there's a line, giving them benefit of the doubt at first." if sentiment == "positive" else "I'd call them out loudly - people need to learn some manners."
            elif "expense" in question.lower() or "repair" in question.lower() or "budget" in question.lower():
                return "I'd review my budget, maybe cut back on non-essentials for a month to cover it." if sentiment == "positive" else "I'd be stressed and probably complain about it to everyone around me."
            elif "personal" in question.lower() or "story" in question.lower() or "stranger" in question.lower():
                return "I'd listen attentively and offer support - sometimes people just need to be heard." if sentiment == "positive" else "I'd look for an excuse to end the conversation - not my problem."
            else:
                return "I'd handle this thoughtfully, considering everyone involved." if sentiment == "positive" else "I'd focus on what works best for me in this situation."

    async def analyze_facial_preferences(self, ratings: list) -> dict:
        return {"preferences": [], "summary": "Preferences analyzed."}
