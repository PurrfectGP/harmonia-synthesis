# 💜 Harmonia Synthesis

AI-powered relationship compatibility analysis using Visual, Personality (Seven Deadly Sins), and Genetic (HLA) factors.

## 🚀 Deployment Options

### Option 1: Cloudflare + Contabo + Zoho Mail (Recommended)

**For Production Deployment:**

**Complete Beginner?** Start here:
- 📖 [**Complete Beginner's Guide**](DEPLOYMENT_BEGINNER.md) - Step-by-step with screenshots explanations (3-4 hours)
- 📖 [**Cloudflare Setup for Beginners**](deployment/CLOUDFLARE_BEGINNER.md) - Domain, SSL, security
- 📖 [**Zoho Mail Setup for Beginners**](deployment/ZOHO_MAIL_BEGINNER.md) - Professional email addresses

**Experienced User?** Quick guides:
- ⚡ [**Quick Start Guide**](deployment/QUICK_START.md) - Fast deployment (1 hour)
- 📖 [**Full Deployment Guide**](DEPLOYMENT.md) - Complete technical reference
- 📖 [**Cloudflare Advanced Setup**](deployment/CLOUDFLARE_SETUP.md) - DNS, SSL, security optimization

**Features:**
- ✅ Custom domain with HTTPS
- ✅ Professional email (noreply@yourdomain.com)
- ✅ Automatic email notifications
- ✅ CDN & DDoS protection via Cloudflare
- ✅ Production-ready with Docker
- ✅ Auto-start on boot
- ✅ Secure API key management

**Cost:** ~$10-20/month (Contabo + domain)

---

### Option 2: Deploy to Render.com (Simple)

**Quick deployment for testing:**

1. Fork/clone this repository
2. Go to [Render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repo
4. **IMPORTANT: Add your API key securely:**
   - Go to **Environment** tab
   - Click **Add Environment Variable**
   - Key: `GEMINI_API_KEY`
   - Value: Your API key from https://aistudio.google.com/app/apikey
5. Deploy!

**Note:** Render is easier but has limitations (no custom email, basic features)

## ⚠️ Security Note

**NEVER put your API key in code files!**

Your API key should ONLY exist in:
- Render.com's Environment Variables (for production)
- A local `.env` file (for development, which is gitignored)

## 🔑 Getting a Gemini API Key

1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Add it to Render's Environment Variables

## 📁 Project Structure

```
harmonia/
├── main.py              # FastAPI application
├── config.py            # Reads from environment variables
├── services/            # Backend services
├── frontend/            # Web interface
└── requirements.txt     # Dependencies
```

## 🔧 Local Development

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/harmonia-synthesis.git
cd harmonia-synthesis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set your API key (Linux/Mac)
export GEMINI_API_KEY=your_key_here

# Or on Windows PowerShell
$env:GEMINI_API_KEY="your_key_here"

# Run the server
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000 in your browser.

## 📄 License

MIT License
