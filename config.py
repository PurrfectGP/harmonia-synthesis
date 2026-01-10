"""
Configuration - Loads settings from environment variables
Compatible with Cloudflare + Zoho Mail + Contabo deployment
"""

import os

class Config:
    """Configuration class for Harmonia."""

    # ==================== API KEYS ====================
    # Gemini AI Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

    # Verify API key exists
    if not GEMINI_API_KEY:
        print("⚠️  WARNING: GEMINI_API_KEY environment variable not set!")
        print("   Set it via: export GEMINI_API_KEY='your-api-key'")
        print("   Get your key from: https://aistudio.google.com/apikey")
    else:
        # Don't print the full key for security
        masked_key = GEMINI_API_KEY[:8] + "..." + GEMINI_API_KEY[-4:]
        print(f"✅ GEMINI_API_KEY loaded: {masked_key}")

    # ==================== GEMINI MODELS ====================
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

    # ==================== DOMAIN & URL CONFIGURATION ====================
    # Your domain (set via Cloudflare)
    DOMAIN = os.getenv('DOMAIN', 'yourdomain.com')
    # Protocol (https in production with Cloudflare SSL)
    PROTOCOL = os.getenv('PROTOCOL', 'https')
    # Full base URL
    BASE_URL = f"{PROTOCOL}://{DOMAIN}"

    print(f"🌐 Domain: {BASE_URL}")

    # ==================== EMAIL CONFIGURATION (ZOHO MAIL) ====================
    # SMTP Settings for Zoho Mail
    SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.zoho.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '465'))  # 465 for SSL, 587 for TLS
    SMTP_USE_SSL = os.getenv('SMTP_USE_SSL', 'true').lower() == 'true'

    # Email Credentials (use app-specific password from Zoho)
    SMTP_USER = os.getenv('SMTP_USER', '')  # e.g., noreply@yourdomain.com
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')  # Zoho app-specific password

    # Email Display Settings
    FROM_EMAIL = os.getenv('FROM_EMAIL', SMTP_USER)
    FROM_NAME = os.getenv('FROM_NAME', 'Harmonia')
    REPLY_TO_EMAIL = os.getenv('REPLY_TO_EMAIL', 'support@yourdomain.com')

    # Email Feature Flags
    EMAIL_ENABLED = os.getenv('EMAIL_ENABLED', 'true').lower() == 'true' and SMTP_USER and SMTP_PASSWORD
    SEND_WELCOME_EMAIL = os.getenv('SEND_WELCOME_EMAIL', 'true').lower() == 'true'
    SEND_REPORT_EMAIL = os.getenv('SEND_REPORT_EMAIL', 'true').lower() == 'true'

    if EMAIL_ENABLED:
        print(f"📧 Email: Enabled ({SMTP_USER})")
    else:
        print("📧 Email: Disabled (configure SMTP_USER and SMTP_PASSWORD to enable)")

    # ==================== SERVER CONFIGURATION ====================
    # Server settings for Contabo deployment
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '8000'))
    WORKERS = int(os.getenv('WORKERS', '4'))  # Gunicorn workers

    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

    print(f"🖥️  Server: {HOST}:{PORT} ({ENVIRONMENT})")

    # ==================== SECURITY CONFIGURATION ====================
    # CORS Settings (for Cloudflare)
    ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', f'{BASE_URL},https://*.{DOMAIN}').split(',')

    # Rate Limiting
    RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'true').lower() == 'true'
    RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_PER_MINUTE', '60'))

    # API Key Validation (prevent unauthorized access)
    REQUIRE_API_KEY = os.getenv('REQUIRE_API_KEY', 'false').lower() == 'true'
    API_KEYS = os.getenv('API_KEYS', '').split(',') if os.getenv('API_KEYS') else []

    # ==================== STORAGE CONFIGURATION ====================
    # File storage paths
    DATA_DIR = os.getenv('DATA_DIR', './data')
    UPLOAD_DIR = os.getenv('UPLOAD_DIR', './uploads')
    REPORTS_DIR = os.getenv('REPORTS_DIR', './harmonia_outputs')

    # Maximum file sizes (in MB)
    MAX_IMAGE_SIZE_MB = int(os.getenv('MAX_IMAGE_SIZE_MB', '10'))
    MAX_DNA_FILE_SIZE_MB = int(os.getenv('MAX_DNA_FILE_SIZE_MB', '5'))

    # ==================== CLOUDFLARE CONFIGURATION ====================
    # Cloudflare settings (optional but recommended)
    CLOUDFLARE_ENABLED = os.getenv('CLOUDFLARE_ENABLED', 'true').lower() == 'true'
    CLOUDFLARE_ZONE_ID = os.getenv('CLOUDFLARE_ZONE_ID', '')
    CLOUDFLARE_API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN', '')

    # Trust Cloudflare proxy headers
    TRUST_PROXY_HEADERS = os.getenv('TRUST_PROXY_HEADERS', 'true').lower() == 'true'

    if CLOUDFLARE_ENABLED:
        print(f"☁️  Cloudflare: Enabled")

    # ==================== LOGGING CONFIGURATION ====================
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', './logs/harmonia.log')

    print(f"📝 Logging: {LOG_LEVEL} → {LOG_FILE}")

    # ==================== DATABASE CONFIGURATION ====================
    # Optional: Add database configuration if needed in future
    # DATABASE_URL = os.getenv('DATABASE_URL', '')

    print("\n✅ Configuration loaded successfully!\n")
