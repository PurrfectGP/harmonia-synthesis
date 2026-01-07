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
    
    # Available Gemini Models (2026)
    AVAILABLE_MODELS = {
        'gemini-3-pro-preview': {
            'name': 'Gemini 3 Pro',
            'description': 'Most advanced model with superior reasoning and multimodal understanding',
            'recommended_for': 'Complex analysis, detailed reports, high-quality responses'
        },
        'gemini-3-flash-preview': {
            'name': 'Gemini 3 Flash',
            'description': 'Fast model with Pro-grade reasoning at Flash speed',
            'recommended_for': 'Quick responses, real-time generation, balanced quality/speed'
        },
        'gemini-2.5-pro': {
            'name': 'Gemini 2.5 Pro',
            'description': 'Powerful model with enhanced reasoning and coding',
            'recommended_for': 'Production workloads, reliable complex tasks'
        },
        'gemini-2.5-flash': {
            'name': 'Gemini 2.5 Flash',
            'description': 'Fast and reliable model for production',
            'recommended_for': 'High-throughput, cost-effective operations'
        }
    }

    # Model selection (set via GEMINI_MODEL environment variable)
    # Default: gemini-3-pro-preview (most advanced model with superior reasoning)
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-3-pro-preview')

    # Model configuration with recommended fallback order
    MODELS = {
        'primary': 'gemini-3-pro-preview',      # Most intelligent
        'fallback': 'gemini-2.5-pro',           # Powerful and reliable
        'fast_fallback': 'gemini-2.5-flash'     # Fast and cost-effective
    }

    print(f"📊 Selected model: {GEMINI_MODEL}")
    if GEMINI_MODEL in AVAILABLE_MODELS:
        print(f"   {AVAILABLE_MODELS[GEMINI_MODEL]['name']} - {AVAILABLE_MODELS[GEMINI_MODEL]['description']}")

    # Timeout settings (prevent timeout errors)
    REQUEST_TIMEOUT = 180  # 3 minutes for complex analysis
    GENERATION_TIMEOUT = 90  # 90 seconds for generation
