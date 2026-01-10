# 🔧 Railway Deployment Troubleshooting

## ❌ "Service Unavailable" Error - FIXED!

### What Was Wrong:
1. **Health check was too slow** - Was checking "/" which loads static files
2. **Timeout was too short** - 100ms wasn't enough for cold starts
3. **No startup logging** - Couldn't see what was failing

### ✅ What I Fixed:

#### 1. Updated Health Check Path
**Before:** `"healthcheckPath": "/"`
**After:** `"healthcheckPath": "/api/health"`

The `/api/health` endpoint is fast and lightweight - just returns JSON status.

#### 2. Increased Timeout
**Before:** `"healthcheckTimeout": 100`
**After:** `"healthcheckTimeout": 300`

Gives Railway 5 minutes to start the app (enough for cold starts).

#### 3. Added Startup Logging
Now you'll see this in Railway logs:
```
==================================================
🚀 HARMONIA STARTING UP
==================================================
✅ GEMINI_API_KEY found (length: 39)
✅ Data directory exists
✅ Output directory ready
==================================================
✅ HARMONIA READY
==================================================
```

#### 4. Added Keep-Alive Timeout
```
--timeout-keep-alive 120
```
Keeps connections alive for 2 minutes (prevents premature timeouts).

---

## 🚀 How to Deploy (Step-by-Step):

### Step 1: Push Latest Code
```bash
git add .
git commit -m "Fix Railway deployment"
git push origin main
```

### Step 2: Create Railway Project
1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Choose **"Deploy from GitHub repo"**
4. Select `harmonia-synthesis`
5. Railway will auto-detect Python

### Step 3: Add Environment Variable
**CRITICAL:** Railway needs your Gemini API key!

1. In Railway dashboard, click your service
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   ```
   Name: GEMINI_API_KEY
   Value: AIzaSy...your-actual-key
   ```
5. Click **"Add"**

### Step 4: Watch Build Logs
1. Click **"Deployments"** tab
2. Click the latest deployment
3. Click **"View Logs"**

**You should see:**
```
Building...
Installing dependencies from requirements.txt
✅ Services imported
Starting uvicorn...
==================================================
🚀 HARMONIA STARTING UP
==================================================
✅ GEMINI_API_KEY found (length: 39)
✅ Data directory exists
✅ Output directory ready
==================================================
✅ HARMONIA READY
==================================================
Application startup complete.
Uvicorn running on http://0.0.0.0:XXXX
```

### Step 5: Test Health Check
Once deployed, visit:
```
https://your-app.up.railway.app/api/health
```

You should see:
```json
{
  "status": "healthy",
  "service": "harmonia",
  "version": "1.0.0"
}
```

### Step 6: Test Homepage
Visit:
```
https://your-app.up.railway.app/
```

You should see the Harmonia homepage!

---

## ⚠️ Common Issues & Fixes:

### Issue: "GEMINI_API_KEY not set"
**Symptom:** Logs show warning about missing API key
**Fix:** Add `GEMINI_API_KEY` in Railway Variables tab

### Issue: "Build failed: Could not install packages"
**Symptom:** Build fails during dependency installation
**Fix:** Check requirements.txt has all dependencies with versions

### Issue: "Health check timeout"
**Symptom:** Deployment keeps retrying, never goes healthy
**Fix:** Check logs for Python errors. Usually missing environment variable.

### Issue: "No module named 'services'"
**Symptom:** Import errors in logs
**Fix:** Make sure all files are pushed to GitHub (check .gitignore)

### Issue: "Port binding failed"
**Symptom:** Error about port already in use
**Fix:** Railway auto-assigns PORT - this shouldn't happen. Contact Railway support.

---

## 🔍 How to Debug:

### 1. Check Logs
**Railway Dashboard → Deployments → View Logs**

Look for:
- ✅ "HARMONIA READY" = Good!
- ⚠️ "WARNING: GEMINI_API_KEY not set" = Add environment variable
- ❌ Python errors = Check which file/line is failing

### 2. Check Environment Variables
**Railway Dashboard → Variables**

Make sure you have:
- `GEMINI_API_KEY` (required)
- Optionally: `GEMINI_MODEL=gemini-3-flash-preview`

### 3. Check Build Status
**Railway Dashboard → Deployments**

- 🟢 Green = Deployed successfully
- 🟡 Yellow = Building/Deploying
- 🔴 Red = Failed (check logs)

### 4. Test Health Endpoint
```bash
curl https://your-app.up.railway.app/api/health
```

Should return:
```json
{"status":"healthy","service":"harmonia","version":"1.0.0"}
```

---

## 📊 Railway Dashboard Checklist:

Before going live:

- [ ] Repository connected to Railway
- [ ] `GEMINI_API_KEY` added to Variables
- [ ] Build completed successfully (green checkmark)
- [ ] Health check passing (`/api/health` returns 200)
- [ ] Logs show "✅ HARMONIA READY"
- [ ] Homepage loads at Railway URL
- [ ] Can access local network engine
- [ ] Can generate AI responses
- [ ] Can download reports

---

## 🎯 Expected Behavior:

### Healthy Deployment:
```
Build: ✅ Success (2-3 minutes)
Health: ✅ Passing
Status: 🟢 Running
Logs: ✅ "HARMONIA READY"
Response time: <1 second
```

### Unhealthy Deployment:
```
Build: 🔴 Failed OR ✅ Success
Health: ❌ Failing
Status: 🔴 Crashed / ⚠️ Restarting
Logs: ❌ Python errors / warnings
Response time: Timeout
```

---

## 💡 Pro Tips:

1. **Watch the logs during first deploy** - You'll see exactly what's happening
2. **Test `/api/health` first** - If this works, everything else should too
3. **Don't worry about warnings** - As long as you see "HARMONIA READY", you're good
4. **Cold starts take 5-10 seconds** - First request might be slow, then it's fast
5. **Railway auto-deploys on git push** - No need to manually redeploy

---

## ✅ Success Indicators:

You're fully deployed when:
- ✅ Build shows green checkmark
- ✅ Health check passes
- ✅ Logs show "HARMONIA READY"
- ✅ Homepage loads
- ✅ `/api/health` returns healthy status
- ✅ Local network engine works
- ✅ Can upload photos
- ✅ Can take quiz
- ✅ Can download report

---

## 🆘 Still Having Issues?

1. **Check Railway Status:** https://status.railway.app
2. **Railway Discord:** https://discord.gg/railway
3. **Railway Docs:** https://docs.railway.app
4. **GitHub Issues:** Post in your repo's issues

Include in your question:
- Full error from logs
- Screenshot of Railway dashboard
- What you've tried so far

---

## 🎉 You're Live!

Once deployed:
- Your app is at: `https://yourapp.up.railway.app`
- Automatically rebuilds on git push
- Scales automatically
- SSL certificate included
- Ready for users!

**Enjoy! 🚀**
