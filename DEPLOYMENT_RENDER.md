# Deploy Harmonia on Render (No Command Line - Just Your Browser!)

**Perfect for:** Google work laptops, Chromebooks, or anyone without terminal access

**What you get:**
- ✅ 100% browser-based deployment
- ✅ Free tier available
- ✅ Auto-deploy from GitHub
- ✅ Custom domain support
- ✅ Free SSL (HTTPS)
- ✅ Instant updates when you push to GitHub

**Total Time:** 10-15 minutes

---

## What is Render?

Render is like having a server that watches your GitHub repository. When you update code on GitHub, Render automatically rebuilds and deploys your app - all without touching a command line!

**Perfect for:**
- Work laptops without admin access
- Chromebooks
- Anyone who wants simple deployment
- Automatic GitHub sync

---

## Part 1: Set Up GitHub Repository

### Step 1.1: Create GitHub Account (If Needed)

1. Go to: https://github.com/signup
2. Fill in:
   - **Email:** Your email address
   - **Password:** Strong password (write it down!)
   - **Username:** Pick a username
3. Verify email
4. Complete setup

**Already have GitHub?** Skip to Step 1.2!

### Step 1.2: Fork or Upload Harmonia

**Option A: If Harmonia is already on GitHub**

1. Go to the Harmonia repository
2. Click **"Fork"** button (top right)
3. Select your account
4. Done! You have your own copy

**Option B: Upload Harmonia Yourself**

1. Go to: https://github.com/new
2. **Repository name:** `harmonia-app`
3. **Public** or **Private:** Choose Public (works better with free tier)
4. Click **"Create repository"**
5. Click **"uploading an existing file"**
6. Drag all your Harmonia files into the browser
7. Click **"Commit changes"**

**🎉 Code is on GitHub!**

---

## Part 2: Create Render Account

### Step 2.1: Sign Up

1. Go to: https://render.com
2. Click **"Get Started"** or **"Sign Up"**
3. Choose **"Sign up with GitHub"** (recommended!)
4. Authorize Render to access GitHub
5. You're logged in!

**Free Tier Benefits:**
- 750 hours/month free
- Automatic SSL
- Custom domains
- GitHub integration

### Step 2.2: Connect GitHub

If you didn't sign up with GitHub:
1. Go to **Account Settings**
2. Click **"Connect GitHub"**
3. Authorize Render

---

## Part 3: Deploy Harmonia

### Step 3.1: Create New Web Service

1. In Render dashboard, click **"New +"** (top right)
2. Select **"Web Service"**
3. You'll see "Create a new Web Service"

### Step 3.2: Connect Your Repository

**Option A: Repository Already Connected**
- You'll see a list of your repos
- Find **harmonia-app**
- Click **"Connect"**

**Option B: Need to Connect Repo**
1. Click **"Configure GitHub"** or **"+ Connect GitHub"**
2. Choose which repos to give Render access to:
   - **All repositories** (easiest), OR
   - **Only select repositories** → Choose harmonia-app
3. Click **"Install"**
4. Go back to Render
5. Now you'll see your repo - click **"Connect"**

### Step 3.3: Configure Service

Render will ask for settings:

**Name:**
- Type: `harmonia-app` (or your choice)
- This becomes part of your URL

**Region:**
- Choose closest to you:
  - **Oregon** (US West)
  - **Ohio** (US East)
  - **Frankfurt** (Europe)
  - **Singapore** (Asia)

**Branch:**
- Select: `main` or `master` (whichever your repo uses)
- Render will auto-deploy when this branch updates!

**Root Directory:**
- Leave blank (unless Harmonia is in a subfolder)

**Runtime:**
- Select: **Python 3**

**Build Command:**
- Type: `pip install -r requirements.txt`

**Start Command:**
- Type: `gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`

**Instance Type:**
- Select: **Free** (for testing)
- Or **Starter** ($7/month for better performance)

### Step 3.4: Add Environment Variables

Scroll down to **Environment Variables** section:

Click **"Add Environment Variable"** and add these:

**Required:**
```
GEMINI_API_KEY = [Your Gemini API key]
```
Get key from: https://aistudio.google.com/apikey

**Recommended:**
```
GEMINI_MODEL = gemini-3-pro-preview
PYTHON_VERSION = 3.11.0
```

**For Email (Add later if using Zoho):**
```
SMTP_HOST = smtp.zoho.com
SMTP_PORT = 465
SMTP_USE_SSL = true
SMTP_USER = noreply@yourdomain.com
SMTP_PASSWORD = your-app-password
EMAIL_ENABLED = true
```

**For Custom Domain (Add later):**
```
DOMAIN = yourdomain.com
PROTOCOL = https
```

### Step 3.5: Create Web Service

Click **"Create Web Service"** button at bottom

**Render will now:**
1. Clone your GitHub repo
2. Install dependencies (pip install)
3. Build your app
4. Deploy it!

**This takes 3-5 minutes.** Watch the build logs!

---

## Part 4: Access Your App

### Step 4.1: Get Your URL

Once deployment is complete:

1. You'll see **"Live"** status (green dot)
2. At the top, you'll see your URL:
   - Format: `https://harmonia-app.onrender.com`
   - Click it to open your app!

### Step 4.2: Test Your App

**Test Health Endpoint:**
```
https://your-app.onrender.com/api/health
```

Should show:
```json
{"status": "running"}
```

**Test Main Page:**
```
https://your-app.onrender.com
```

Should load Harmonia homepage!

**🎉 Your app is live!**

---

## Part 5: Set Up Auto-Deploy (Already Done!)

**Great news:** It's already working!

### How Auto-Deploy Works:

```
You Edit File on GitHub
         ↓
Click "Commit changes"
         ↓
Render Detects Change (within seconds!)
         ↓
Render Rebuilds App (2-3 minutes)
         ↓
Your Site Updates Automatically
         ↓
🎉 Live!
```

### Test It:

1. **Go to GitHub:** https://github.com/yourusername/harmonia-app
2. **Edit a file:** Click `README.md` → Click pencil ✏️
3. **Make a change:** Add a line
4. **Commit:** Click "Commit changes"
5. **Watch Render:** Go to Render dashboard
6. **See deployment:** You'll see "Deploying..."
7. **Wait 2-3 minutes**
8. **Refresh your site:** Change is live!

**No command line. No manual uploads. Just edit and it deploys!** ✨

---

## Part 6: Managing Your App

### View Logs

1. In Render dashboard, click your service
2. Click **"Logs"** tab
3. See real-time logs
4. Filter by:
   - Deploy logs
   - Runtime logs
   - Error logs

### Manual Deploy

Need to redeploy without code changes?

1. Click **"Manual Deploy"** button
2. Select **"Clear build cache & deploy"** if having issues
3. Or just **"Deploy"** for normal redeploy

### Environment Variables

Change settings anytime:

1. Click **"Environment"** tab
2. Edit any variable
3. Click "Save Changes"
4. App automatically redeploys!

### Metrics

See how your app is doing:

1. Click **"Metrics"** tab
2. View:
   - Memory usage
   - CPU usage
   - Bandwidth
   - Request count
   - Response times

### Restart Service

If app is stuck:

1. Click the **"⋯"** menu (three dots)
2. Click **"Restart Service"**
3. Wait 30 seconds
4. App restarts!

---

## Part 7: Add Custom Domain (Optional)

### Prerequisites:
- You own a domain
- Have access to DNS settings (Cloudflare, etc.)

### Steps:

**On Render:**

1. Click **"Settings"** tab
2. Scroll to **"Custom Domain"**
3. Click **"Add Custom Domain"**
4. Type your domain: `yourdomain.com`
5. Render shows DNS records to add

**On Cloudflare (or your DNS provider):**

1. Log in to Cloudflare
2. Go to **DNS** section
3. Add **CNAME** record:
   - **Name:** `@` or `www`
   - **Target:** `your-app.onrender.com`
   - **Proxy:** Orange cloud (proxied)
4. Save

**Wait 5-60 minutes for DNS propagation**

**Back on Render:**
- Render auto-detects when DNS is ready
- Enables HTTPS automatically
- Your app is now at yourdomain.com!

---

## Part 8: Understanding the Free Tier

### What's Included (Free):

- ✅ 750 hours per month
- ✅ Automatic HTTPS/SSL
- ✅ Custom domains
- ✅ Auto-deploy from GitHub
- ✅ Unlimited collaborators
- ✅ Build time included

### Limitations (Free):

- ⚠️ Apps "spin down" after 15 min of inactivity
  - First visit after idle = 30-60 second delay
  - Then runs normally
- ⚠️ 512 MB RAM
- ⚠️ Shared CPU

### When to Upgrade to Paid ($7/month):

**Upgrade if you need:**
- 🚀 No spin-down (always instant)
- 🚀 More RAM (1 GB+)
- 🚀 Dedicated CPU
- 🚀 Better performance

**For testing/personal use:** Free tier is fine!
**For production/real users:** Upgrade to Starter ($7/month)

### Monitor Usage:

1. Click **"Account Settings"**
2. Click **"Billing"**
3. See your usage
4. Free tier usage is clearly shown

---

## Part 9: Editing Your App (No Command Line!)

### Edit on GitHub Website

**Easy way to update code:**

1. Go to your repo on GitHub
2. Navigate to file (example: `main.py`)
3. Click the file
4. Click **✏️ Edit** (pencil icon)
5. Make your changes
6. Scroll down
7. Write commit message
8. Click **"Commit changes"**
9. Render auto-deploys in 2-3 minutes!

### Use GitHub's Web Editor (Advanced)

**Full IDE in your browser:**

1. Go to your repo on GitHub
2. Press the **`.`** (period) key
3. GitHub opens **github.dev** (web VS Code!)
4. Edit multiple files
5. Use the Source Control panel (left sidebar)
6. Commit & push
7. Render auto-deploys!

### Upload Files

**Add new files:**

1. Go to your repo
2. Click **"Add file"** → **"Upload files"**
3. Drag files into browser
4. Click **"Commit changes"**
5. Render auto-deploys!

---

## Part 10: Troubleshooting

### Problem: Build Failed

**Check Build Logs:**
1. Click **"Logs"** tab
2. Look for red error messages
3. Common issues:
   - Missing dependency in `requirements.txt`
   - Typo in start command
   - Wrong Python version

**Solutions:**
- Fix the error in GitHub
- Commit changes
- Render rebuilds automatically

### Problem: App Shows "Not Found"

**Solutions:**
1. Check **Start Command** is correct:
   ```
   gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   ```
2. Make sure `main.py` exists in your repo
3. Check logs for errors

### Problem: "Service Unavailable"

**Reasons:**
- App is starting (wait 30-60 seconds)
- App crashed (check logs)
- Free tier spun down (visit site to wake it up)

**Solution:**
1. Check logs for errors
2. Fix error in GitHub
3. Commit and redeploy

### Problem: Environment Variable Not Working

**Solution:**
1. Go to **Environment** tab
2. Check variable name (exact spelling matters!)
3. Check value is correct
4. Click **"Save Changes"**
5. Wait for redeploy

### Problem: Slow First Load

**This is normal on free tier!**

**Why:**
- Free apps sleep after 15 minutes of inactivity
- First visit wakes it up (30-60 seconds)
- Then runs normally

**Solution:**
- Upgrade to Starter plan ($7/month) for instant response
- Or accept the delay (fine for personal projects)

### Problem: GitHub Changes Not Deploying

**Check:**
1. Go to **Settings** tab
2. Scroll to **"Build & Deploy"**
3. Check **"Auto-Deploy"** is **ON**
4. Check correct branch is selected

**Manual Deploy:**
- Click **"Manual Deploy"** button

---

## Part 11: Adding Email Functionality

Once you set up Zoho Mail (see beginner guides), add email to Render:

### Add Email Variables:

1. Go to **Environment** tab
2. Add these variables:

```
SMTP_HOST = smtp.zoho.com
SMTP_PORT = 465
SMTP_USE_SSL = true
SMTP_USER = noreply@yourdomain.com
SMTP_PASSWORD = [Your Zoho app-specific password]
FROM_EMAIL = noreply@yourdomain.com
FROM_NAME = Harmonia
REPLY_TO_EMAIL = support@yourdomain.com
EMAIL_ENABLED = true
SEND_WELCOME_EMAIL = true
SEND_REPORT_EMAIL = true
```

3. Click **"Save Changes"**
4. Wait for redeploy
5. Test email functionality!

---

## Part 12: Best Practices

### ✅ DO:

- **Keep secrets in Environment Variables** (not code)
- **Use Auto-Deploy** (it's amazing!)
- **Monitor logs** regularly
- **Test after every change**
- **Use free tier** for testing
- **Upgrade for production** use

### ❌ DON'T:

- **Don't put API keys in code** (use env vars!)
- **Don't commit passwords** to GitHub
- **Don't ignore build failures**
- **Don't edit directly on Render** (edit on GitHub instead)

### Security:

- **Make repo private** if it contains sensitive data
- **Use environment variables** for all secrets
- **Rotate API keys** regularly
- **Enable 2FA** on GitHub

---

## Part 13: Monitoring Your App

### Dashboard Overview

**What you see:**
- 🟢 Green = Live and running
- 🟡 Yellow = Deploying
- 🔴 Red = Failed/Down

### Health Checks

Render automatically checks if your app is responding:
- Pings your app every few minutes
- Restarts if unresponsive
- Shows status in dashboard

### Alerts (Paid Plans)

Upgrade to get:
- Email alerts when app goes down
- Slack notifications
- PagerDuty integration

---

## Part 14: Comparison with Other Platforms

### Render vs Railway

**Render:**
- ✅ More generous free tier
- ✅ Better documentation
- ✅ Easier interface
- ❌ Spin-down on free tier

**Railway:**
- ✅ No spin-down on free tier
- ✅ $5 free credits
- ❌ Runs out faster
- ❌ Harder to understand

**Recommendation:** Start with Render, try Railway later!

### Render vs Heroku

**Render:**
- ✅ Free tier available
- ✅ Modern interface
- ✅ Better performance
- ✅ Auto-deploy easier

**Heroku:**
- ❌ No free tier anymore
- ❌ $5/month minimum
- ✅ More mature
- ✅ Lots of add-ons

**Recommendation:** Use Render (Heroku killed free tier)

---

## Part 15: Scaling Your App

### When to Upgrade

**Signs you need Starter plan ($7/month):**
- ⚠️ People complaining about slow first load
- ⚠️ More than a few users
- ⚠️ Need it to be fast 24/7
- ⚠️ Running out of memory

### Upgrading

1. Click service
2. Click **"Settings"**
3. Scroll to **"Instance Type"**
4. Click **"Change"**
5. Select **"Starter"**
6. Add payment method
7. Confirm

**Instant upgrade - no downtime!**

### Multiple Services

As you grow, you can run:
- **Web service** (Harmonia app)
- **Background workers** (for jobs)
- **Databases** (PostgreSQL, Redis)
- **Cron jobs** (scheduled tasks)

All in the same dashboard!

---

## Part 16: Backing Up Your App

### GitHub = Your Backup!

**Your code is already backed up on GitHub!**

**To save your work:**
1. Edit code
2. Commit to GitHub
3. It's automatically saved!

### Export Environment Variables

**Save your settings:**
1. Go to **Environment** tab
2. Copy all variables
3. Save in a text file
4. Keep it safe (these are secrets!)

### Database Backups

If you add a database later:
- Render has automatic backups (paid plans)
- Or use manual pg_dump (export) regularly

---

## Part 17: Getting Help

### Render Support

**Free Plan:**
- Community forum
- Documentation
- Email support (slower)

**Paid Plans:**
- Priority email support
- Faster response times

### Links:

**Render Docs:**
→ https://render.com/docs

**Community Forum:**
→ https://community.render.com

**Status Page:**
→ https://status.render.com

**Twitter:**
→ @render (for updates)

---

## Quick Reference

### Your URLs:

**Render Dashboard:**
```
https://dashboard.render.com
```

**Your App:**
```
https://your-app-name.onrender.com
```

**GitHub Repo:**
```
https://github.com/yourusername/harmonia-app
```

### Important Commands (No CLI Needed!)

**Deploy:** Commit to GitHub (auto-deploys)
**Redeploy:** Click "Manual Deploy" button
**View Logs:** Click "Logs" tab
**Change Settings:** Click "Environment" tab
**Restart:** Click ⋯ menu → "Restart Service"

### Environment Variables Template:

```bash
# Required
GEMINI_API_KEY=your-key-here

# Recommended
GEMINI_MODEL=gemini-3-pro-preview
PYTHON_VERSION=3.11.0

# For Email (optional)
SMTP_HOST=smtp.zoho.com
SMTP_PORT=465
SMTP_USE_SSL=true
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your-app-password
EMAIL_ENABLED=true

# For Custom Domain (optional)
DOMAIN=yourdomain.com
PROTOCOL=https
```

---

## Success Checklist

- [ ] GitHub account created
- [ ] Harmonia code uploaded to GitHub
- [ ] Render account created
- [ ] Repository connected to Render
- [ ] Service configured
- [ ] Environment variables added
- [ ] App deployed successfully
- [ ] Can access app at .onrender.com URL
- [ ] Health endpoint working
- [ ] Auto-deploy tested (edit→commit→deploys)
- [ ] Logs reviewed (no errors)

---

## You Did It! 🎉

**Congratulations! You've deployed Harmonia without a command line!**

### What You Achieved:

- ✅ App deployed on Render
- ✅ Connected to GitHub
- ✅ Auto-deploys on every commit
- ✅ Live HTTPS website
- ✅ Free tier (or paid if you chose)
- ✅ Monitoring dashboard
- ✅ 100% browser-based workflow

### Your Workflow Now:

```
1. Edit code on GitHub (in browser)
2. Commit changes (click button)
3. Render auto-deploys (2-3 minutes)
4. Site updates automatically
5. Repeat!
```

**No terminal. No command line. Just browsers!**

### What's Next:

1. ✅ Add custom domain (optional)
2. ✅ Set up Zoho Mail for emails
3. ✅ Invite friends to test
4. ✅ Monitor usage
5. ✅ Upgrade when ready
6. ✅ Build more features!

---

## Bonus: Render Mobile App

**Manage your app from your phone!**

**Download:**
- iOS: Search "Render" in App Store
- Android: Search "Render" in Play Store

**Features:**
- View logs
- Manual deploys
- Check status
- Monitor metrics
- Restart services

**Perfect for checking on your app while away from computer!**

---

**You're now a web developer with a live app!** 🚀

**Share your Render URL with friends and start using Harmonia!**

**Questions? Check Render docs or community forum.**

**Happy deploying!** 🎊
