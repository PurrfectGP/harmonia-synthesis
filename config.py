"""
Configuration - Loads API keys from environment variables (Render)
"""

import os

class Config:
    """Configuration class for Harmonia."""
    
    # Load from Render environment variable
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    
    # Verify API key exists
    if not GEMINI_API_KEY:
        print("⚠️ WARNING: GEMINI_API_KEY environment variable not set!")
        print("   Set it in Render dashboard: Environment → Add Variable")
        print("   Key: GEMINI_API_KEY")
        print("   Value: Your API key from https://aistudio.google.com/apikey")
    else:
        # Don't print the full key for security
        masked_key = GEMINI_API_KEY[:8] + "..." + GEMINI_API_KEY[-4:]
        print(f"✅ GEMINI_API_KEY loaded from environment: {masked_key}")
    
    # Model configuration with CORRECT fallback order
    # PRIMARY: Gemini 3 Pro (most intelligent!)
    # FALLBACK: Gemini 2.5 Pro (powerful)
    # FAST FALLBACK: Gemini 2.5 Flash (reliable)
    MODELS = {
        'primary': 'gemini-3-pro-preview',      # FIRST - Most intelligent
        'fallback': 'gemini-2.5-pro',           # SECOND - Powerful thinking
        'fast_fallback': 'gemini-2.5-flash'     # THIRD - Fast and reliable
    }
    
    # Timeout settings (prevent timeout errors)
    REQUEST_TIMEOUT = 180  # 3 minutes for complex analysis
    GENERATION_TIMEOUT = 90  # 90 seconds for generation
