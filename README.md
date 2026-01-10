# 💜 Harmonia Synthesis

AI-powered relationship compatibility analysis using Visual, Personality (Seven Deadly Sins), and Genetic (HLA) factors.

## 🚀 Deployment Options

### ⭐ Browser-Only Deployment (No Command Line Required!)

**Perfect for:** Google work laptops, Chromebooks, or anyone without terminal access

**🎯 Not sure which to choose?** Check the [Platform Comparison Guide](DEPLOYMENT_COMPARISON.md)

#### Option 1: Railway (Recommended for Always-On Apps)

**✨ Features:**
- ✅ Deploy entirely from your browser
- ✅ Automatic updates from GitHub
- ✅ Always-on (no sleeping)
- ✅ $5/month free credits
- ✅ Custom domain support
- ✅ Mobile app for monitoring

**📖 Full Guide:** [Railway Deployment Guide](DEPLOYMENT_RAILWAY.md)

**⏱️ Time:** 15-20 minutes | **💰 Cost:** Free tier ($5 credits/month)

---

#### Option 2: Render (Best for Free Hosting)

**✨ Features:**
- ✅ Deploy entirely from your browser
- ✅ Automatic updates from GitHub
- ✅ Completely free forever
- ✅ Custom domain support
- ✅ No credit card required

**📖 Full Guide:** [Render Deployment Guide](DEPLOYMENT_RENDER.md)

**⏱️ Time:** 15-20 minutes | **💰 Cost:** Free forever

**Note:** Free tier apps sleep after 15 min of inactivity (30-second wake time)

---

### 🔧 Advanced: Server Deployment (Cloudflare + Contabo + Zoho Mail)

**For advanced users who need full control and have terminal/SSH access**

**Complete Beginner?** Start here:
- 📖 [**Complete Beginner's Guide**](DEPLOYMENT_BEGINNER.md) - Step-by-step with screenshot explanations (3-4 hours)
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
- ✅ Full server control

**⏱️ Time:** 3-4 hours (beginner) or 1 hour (experienced) | **💰 Cost:** ~$10-20/month (VPS + domain)

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
