# 🚀 Railway Deployment Guide (Hobby Plan) - FIXED

## ✅ ISSUES FIXED:

1. **Fixed API endpoint crash** - Updated `/api/analyze` to use neutral trait keys instead of old sin-based keys
2. **Added python-dotenv** to requirements.txt
3. **Added version specifications** to all dependencies for stability
4. **Created runtime.txt** to specify Python 3.11.7
5. **Created nixpacks.toml** for optimized Railway builds
6. **Created .railwayignore** to exclude unnecessary files
7. **Updated railway.json** with health checks
8. **Fixed chart labels** to show neutral trait names (Drive, Confidence, etc.)

---

## 📋 REQUIRED ENVIRONMENT VARIABLES

Set these in Railway Dashboard → Variables:

### Essential (Minimum):
```
GEMINI_API_KEY=your-gemini-api-key-here
```

### Recommended (Optional):
```
GEMINI_MODEL=gemini-3-flash-preview
```

---

## 🚀 DEPLOYMENT STEPS:

### Step 1: Connect to Railway

1. Go to [railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click **"New Project"**
4. Choose **"Deploy from GitHub repo"**
5. Select your `harmonia-synthesis` repository
6. Railway will auto-detect Python and start building

### Step 2: Configure Environment Variables

1. In Railway dashboard, click on your service
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   ```
   GEMINI_API_KEY=AIzaSy...your-actual-key
   ```
5. Click **"Add"**
6. Optional: Add `GEMINI_MODEL=gemini-3-flash-preview`

### Step 3: Wait for Build & Deploy

- Railway will automatically:
  1. Install Python 3.11.7
  2. Install dependencies from requirements.txt
  3. Create necessary directories
  4. Start the server with uvicorn
  5. Assign a public URL

**Build time:** ~2-3 minutes

### Step 4: Test Your Deployment

1. Click **"View Logs"** in Railway dashboard
2. Look for: `✅ Application startup complete`
3. Click the generated URL (e.g., `yourapp.up.railway.app`)
4. You should see the Harmonia homepage!

### Step 5: Add Custom Domain (Optional)

1. In Railway dashboard, go to **Settings → Domains**
2. Click **"Generate Domain"** or **"Custom Domain"**
3. For custom domain:
   - Click **"Custom Domain"**
   - Enter: `harmonia.yourdomain.com`
   - Add CNAME record in Cloudflare:
     - Name: `harmonia` (or `@` for root)
     - Target: Copy from Railway
   - Wait 5-10 minutes for verification

---

## 💰 Railway Hobby Plan Details:

**Cost:** $5/month

**Includes:**
- ✅ $5 execution time credits
- ✅ 512MB RAM per service
- ✅ 1GB Disk space
- ✅ Automatic SSL certificates
- ✅ Custom domains
- ✅ Automatic deployments
- ⚠️ No guaranteed uptime (may sleep after inactivity)

**Perfect for:**
- Beta testing
- Small user base (<100 users/day)
- Development/staging environments

**Limitations:**
- May sleep after 30 min inactivity (wakes up in ~1 second on first request)
- Limited to $5 execution credits per month
- No priority support

---

## 🔧 TROUBLESHOOTING:

### Build Fails:

**Error:** `Could not install packages`
- **Fix:** Check requirements.txt has all dependencies with versions

**Error:** `No module named 'dotenv'`
- **Fix:** Already fixed! python-dotenv is now in requirements.txt

**Error:** `Port already in use`
- **Fix:** Railway auto-assigns PORT, no action needed

### Runtime Errors:

**Error:** `KeyError: 'greed'` or similar
- **Fix:** Already fixed! Now uses neutral trait keys

**Error:** `GEMINI_API_KEY not found`
- **Fix:** Add GEMINI_API_KEY to Railway Variables

**Error:** `Safety filters blocking responses`
- **Fix:** Already fixed! Now uses neutral language throughout

### App Won't Start:

**Check logs for:**
```bash
# In Railway dashboard → Deployments → View Logs
```

**Common issues:**
- Missing environment variables → Add in Variables tab
- Import errors → Check all files uploaded
- Port binding issues → Railway handles this automatically

---

## 📊 MONITORING:

### Check Application Health:

1. **Logs:**
   - Railway Dashboard → Deployments → View Logs
   - Watch for errors or warnings

2. **Metrics:**
   - Railway Dashboard → Metrics
   - Monitor CPU, Memory, Network usage

3. **Cost:**
   - Railway Dashboard → Usage
   - Track execution time credits

**Alert:** If you're using >$4/month, upgrade to Pro before running out!

---

## 🎯 UPGRADING TO PRO:

When you're ready for production (>100 users/day):

**Railway Pro:** $20/month
- ✅ $20 execution time credits
- ✅ 8GB RAM per service
- ✅ 100GB Disk space
- ✅ Priority support
- ✅ **Never sleeps!**
- ✅ Higher resource limits
- ✅ Team collaboration

**Upgrade:**
1. Railway Dashboard → Settings
2. Click **"Upgrade to Pro"**
3. Add payment method
4. Automatic migration (no downtime!)

---

## ✅ DEPLOYMENT CHECKLIST:

Before going live:

- [ ] Railway project created
- [ ] Repository connected
- [ ] GEMINI_API_KEY added to Variables
- [ ] Build successful (check logs)
- [ ] App accessible at Railway URL
- [ ] Test local network engine (upload photos, take quiz, get results)
- [ ] Test report download (DOCX file)
- [ ] Custom domain configured (optional)
- [ ] SSL certificate active (automatic)

---

## 🆘 GET HELP:

**Railway Issues:**
- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app

**Harmonia Issues:**
- Check logs first
- Verify environment variables
- Test locally with `uvicorn main:app --reload`

---

## 🎉 YOU'RE LIVE!

Your Harmonia app is now deployed on Railway! 🚀

**Next Steps:**
1. Share your Railway URL
2. Monitor usage in Railway dashboard
3. Upgrade to Pro when ready for production
4. Add custom domain for professional look

**Your app is ready to match soulmates!** ❤️
