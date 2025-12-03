import os

class Settings:
    """
    Configuration loaded from ENVIRONMENT VARIABLES only.
    NEVER put API keys in this file!
    
    Set your API key in:
    - Render: Dashboard → Environment → Add Variable
    - Local: export GEMINI_API_KEY=your_key
    """
    
    def __init__(self):
        # Get API key from environment variable ONLY
        self.GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
        
        if not self.GEMINI_API_KEY:
            raise ValueError(
                "\n\n"
                "❌ GEMINI_API_KEY environment variable not set!\n\n"
                "To fix this:\n"
                "  Render.com: Dashboard → Your Service → Environment → Add Environment Variable\n"
                "  Local dev:  export GEMINI_API_KEY=your_key_here\n"
            )
        
        # Weights (defaults provided)
        self.VISUAL_WEIGHT = int(os.environ.get("VISUAL_WEIGHT", "50"))
        self.PERSONALITY_WEIGHT = int(os.environ.get("PERSONALITY_WEIGHT", "35"))
        self.HLA_WEIGHT = int(os.environ.get("HLA_WEIGHT", "15"))
        self.MIN_WORDS = int(os.environ.get("MIN_WORDS", "25"))
        self.MAX_WORDS = int(os.environ.get("MAX_WORDS", "150"))
