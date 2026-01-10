# Deploy Harmonia via Railway (No Command Line Required!)

**Perfect for:** Google work laptops, Chromebooks, or any computer without terminal access

**What you get:**
- ✅ Deploy from your browser
- ✅ Automatic updates from GitHub
- ✅ Free hosting ($5 credit/month)
- ✅ Custom domain support
- ✅ Environment variables via web
- ✅ No command line needed!

**Total Time:** 15-20 minutes

---

## What is Railway?

Railway is a platform that lets you deploy websites directly from GitHub:
- Push code to GitHub → Railway automatically deploys it
- Updates happen automatically
- Manage everything from your browser
- No terminal/command line needed!

---

## Step 1: Create a GitHub Account (If You Don't Have One)

### 1.1 Go to GitHub

1. Open your browser
2. Go to: https://github.com/signup
3. You'll see the signup page

### 1.2 Sign Up

Fill in the form:
- **Email address:** Your personal or work email
- **Password:** Create a strong password (write it down!)
- **Username:** Choose a username (like `yourname123`)
- **Email preferences:** Check or uncheck (your choice)

Click **"Continue"**

### 1.3 Verify Your Account

1. Check your email
2. Find email from GitHub
3. Click the verification link
4. Complete the puzzle/verification

**🎉 You have a GitHub account!**

---

## Step 2: Upload Harmonia to Your GitHub

### 2.1 Create a New Repository

1. Go to: https://github.com/new
2. You'll see "Create a new repository"

**Fill in:**
- **Repository name:** Type `harmonia-app` (or any name you like)
- **Description:** Type `My Harmonia compatibility app` (optional)
- **Public or Private:** Choose **Public** (Railway free tier works best with public repos)
- **Add README:** Leave unchecked
- **Add .gitignore:** Leave as "None"
- **Choose a license:** Leave as "None"

Click **"Create repository"**

### 2.2 Upload Your Code

You'll see a page with several options. We'll use the web upload:

1. Click **"uploading an existing file"** link (in the middle of the page)
2. You'll see "Drag files here to add them to your repository"

**Option A: Drag and Drop**
1. On your computer, open the folder with Harmonia code
2. Select ALL files and folders
3. Drag them into the GitHub page
4. Wait for upload to complete

**Option B: Choose Files**
1. Click **"choose your files"**
2. Navigate to Harmonia folder
3. Select all files
4. Click "Open"
5. Wait for upload

### 2.3 Commit the Upload

At the bottom of the page:
- **Commit message:** Already says "Add files via upload" (that's fine!)
- Click **"Commit changes"** button

**Wait 30 seconds for processing**

**🎉 Your code is on GitHub!**

---

## Step 3: Create Railway Account

### 3.1 Go to Railway

1. Open a new browser tab
2. Go to: https://railway.app/

### 3.2 Sign Up with GitHub

1. Click **"Login"** or **"Start a New Project"** button
2. Click **"Login with GitHub"**
3. It will redirect to GitHub
4. Click **"Authorize Railway"** (green button)
5. It will redirect back to Railway

**🎉 You're logged into Railway!**

---

## Step 4: Deploy Harmonia to Railway

### 4.1 Create a New Project

1. You'll see Railway dashboard
2. Click **"New Project"** button (or "+ New Project")
3. You'll see several options

### 4.2 Deploy from GitHub Repo

1. Click **"Deploy from GitHub repo"**
2. You'll see a list of your GitHub repositories
3. **Can't see your repo?**
   - Click **"Configure GitHub App"**
   - Give Railway access to your repositories
   - Come back to Railway

4. Find your **harmonia-app** repository
5. Click on it

### 4.3 Select Deploy Settings

Railway will ask a few questions:

**Deploy type:**
- Select **"Empty Service"** or just click **"Deploy Now"**

Railway will start deploying!

**You'll see:**
- Building...
- Deploying...
- ⚠️ It might fail first time - that's okay!

---

## Step 5: Add Environment Variables

### 5.1 Go to Variables Tab

1. In Railway, you'll see your project
2. Click on your service (the box with your app name)
3. Look for tabs at the top
4. Click **"Variables"** tab

### 5.2 Add Gemini API Key

1. You'll see "Add Environment Variable" section
2. Click **"New Variable"** or **"+ New Variable"**

**Add this variable:**
- **Variable name:** Type `GEMINI_API_KEY`
- **Value:** Paste your Gemini API key
  - (Get it from: https://aistudio.google.com/apikey)

Click **"Add"** or press Enter

### 5.3 Add Other Variables

Add these one by one (click "New Variable" for each):

**For basic setup:**
```
GEMINI_MODEL = gemini-3-pro-preview
DOMAIN = your-app.railway.app
PROTOCOL = https
```

**For email (optional - can add later):**
```
SMTP_HOST = smtp.zoho.com
SMTP_PORT = 465
SMTP_USE_SSL = true
SMTP_USER = noreply@yourdomain.com
SMTP_PASSWORD = your-zoho-app-password
EMAIL_ENABLED = true
```

**(Don't have email setup yet? Just add the basic ones above for now!)**

### 5.4 Save Variables

Railway automatically saves variables!

You'll see them listed in the Variables tab.

---

## Step 6: Add Railway Configuration File

We need to tell Railway how to run your app.

### 6.1 Create Procfile

**On GitHub:**

1. Go to your repository: `https://github.com/yourusername/harmonia-app`
2. Click **"Add file"** → **"Create new file"**
3. File name: Type `Procfile` (exactly like that, capital P, no extension)
4. In the file content box, type:
   ```
   web: gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   ```
5. Scroll down
6. Click **"Commit new file"**

### 6.2 Create nixpacks.toml (Optional but Recommended)

This tells Railway which Python version to use:

1. Still on GitHub, click **"Add file"** → **"Create new file"**
2. File name: Type `nixpacks.toml`
3. In the content box, type:
   ```toml
   [phases.setup]
   nixPkgs = ["python311"]

   [start]
   cmd = "gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT"
   ```
4. Scroll down
5. Click **"Commit new file"**

---

## Step 7: Redeploy on Railway

### 7.1 Trigger New Deployment

**Railway automatically detects your GitHub changes!**

1. Go back to Railway tab
2. You'll see it's already building/deploying
3. **If not:** Click the **"⋮"** menu → **"Redeploy"**

### 7.2 Wait for Deployment

Watch the deployment:
- You'll see logs scrolling
- Look for: "Installing dependencies..."
- Then: "Starting application..."
- Finally: "Deployment successful"

This takes 2-5 minutes.

---

## Step 8: Get Your Website URL

### 8.1 Generate Domain

1. In Railway, click **"Settings"** tab
2. Scroll to **"Domains"** section
3. Click **"Generate Domain"**
4. Railway will create a URL like: `harmonia-app-production.up.railway.app`

**This is your website address!**

### 8.2 Visit Your Website

1. Click on the domain Railway generated
2. Your browser will open your Harmonia app!
3. You should see your application running

**🎉 Your app is live!**

---

## Step 9: Test Everything

### 9.1 Test Health Endpoint

In your browser, go to:
```
https://your-app.up.railway.app/api/health
```

You should see:
```json
{"status": "running"}
```

✅ If you see this, your app is working!

### 9.2 Test Main Page

Go to:
```
https://your-app.up.railway.app
```

You should see your Harmonia homepage!

### 9.3 Test Creating a Profile

1. Try to create a test profile
2. Upload an image
3. Generate a compatibility report

**Everything working?** 🎉 **You're done!**

---

## Step 10: Set Up Automatic Updates

**This is the best part - it's already done!**

### How It Works:

1. **Edit files on GitHub** (through web interface)
2. **Click "Commit changes"**
3. **Railway automatically detects the change**
4. **Railway builds and deploys automatically**
5. **Your site updates in 2-5 minutes!**

### Try It:

1. Go to GitHub repository
2. Click on any file (like `README.md`)
3. Click the pencil icon (✏️ Edit)
4. Make a change
5. Click "Commit changes"
6. Go to Railway - you'll see it deploying!
7. Wait 2-5 minutes
8. Refresh your website - change is live!

**No command line, no uploads - just edit and it updates!** ✨

---

## Manage Your App via Railway Dashboard

### View Logs

1. Click **"Deployments"** tab
2. Click on latest deployment
3. Click **"View Logs"**
4. See what's happening in real-time

### Monitor Usage

1. Click **"Metrics"** tab
2. See:
   - Memory usage
   - CPU usage
   - Network traffic
   - Request count

### Restart App

1. Click **"Settings"** tab
2. Scroll to bottom
3. Click **"Restart Deployment"**

### Change Environment Variables

1. Click **"Variables"** tab
2. Click on any variable to edit
3. Or add new ones
4. App restarts automatically

---

## Adding a Custom Domain (Optional)

### Prerequisites:
- You own a domain
- You have access to DNS settings

### Steps:

1. In Railway, go to **"Settings"** → **"Domains"**
2. Click **"Custom Domain"**
3. Type your domain: `yourdomain.com`
4. Railway shows you DNS records to add
5. Go to your domain provider (Cloudflare, etc.)
6. Add the CNAME record Railway provides
7. Wait 5-60 minutes for DNS propagation
8. Your site will be live at your custom domain!

---

## Understanding Costs

### Free Tier:

Railway gives you:
- **$5 in free credits per month**
- Enough for small apps
- No credit card required to start

**Your usage:**
- Small app like Harmonia: ~$3-5/month
- Should stay within free tier!

### Monitor Credits:

1. Click your profile (top right)
2. Click **"Account Settings"**
3. See your credit usage

**If you run out:**
- Add a credit card
- Costs are very cheap (~$5-10/month)

---

## Troubleshooting

### Problem: "Application Error" on website

**Solution:**
1. Check logs in Railway
2. Look for error messages
3. Make sure all environment variables are set
4. Check GEMINI_API_KEY is correct

### Problem: Deployment keeps failing

**Solutions:**
1. Check you have `Procfile` in repository
2. Check `requirements.txt` is present
3. View build logs for specific error
4. Make sure Python 3.11 is specified

### Problem: Can't see my GitHub repo

**Solution:**
1. Click "Configure GitHub App" in Railway
2. Give Railway access to the repository
3. Go back and try again

### Problem: Changes not deploying

**Solution:**
1. Check Railway is connected to correct branch (usually `main`)
2. Go to Settings → **"Service"** → verify GitHub connection
3. Manually trigger: Click ⋮ menu → "Redeploy"

### Problem: App works but emails don't send

**Solution:**
1. Check email environment variables are set
2. Make sure you're using app-specific password (not main password)
3. Check logs for email errors
4. Verify Zoho Mail is configured correctly

---

## Editing Your App (No Command Line!)

### Edit Code on GitHub:

1. Go to your repository on GitHub
2. Navigate to the file you want to edit
3. Click the file name
4. Click the ✏️ (pencil) icon to edit
5. Make your changes
6. Click "Commit changes"
7. Railway automatically deploys!

### Upload New Files:

1. Go to your repository
2. Click "Add file" → "Upload files"
3. Drag and drop new files
4. Click "Commit changes"
5. Railway automatically deploys!

### Edit Multiple Files (Advanced):

Use **github.dev** (web-based VS Code):

1. Go to your repository on GitHub
2. Press the `.` (period) key on your keyboard
3. GitHub opens a full code editor in your browser!
4. Edit multiple files
5. Commit and push (there's a UI for this)
6. Railway deploys automatically!

---

## Alternative: Edit on Replit (Coming in next guide!)

If you want a full IDE in your browser, check out the Replit guide!

---

## Connecting Email (Later)

Once you have Zoho Mail set up:

1. Go to Railway **"Variables"** tab
2. Add email variables:
   ```
   SMTP_USER=noreply@yourdomain.com
   SMTP_PASSWORD=your-app-password
   SMTP_HOST=smtp.zoho.com
   SMTP_PORT=465
   SMTP_USE_SSL=true
   EMAIL_ENABLED=true
   ```
3. Railway restarts automatically
4. Emails will work!

---

## Best Practices

### ✅ DO:

- Keep your GEMINI_API_KEY secret
- Monitor your Railway credits
- Check logs if something breaks
- Use environment variables for secrets
- Test after every change

### ❌ DON'T:

- Put API keys in code files
- Share your Railway account
- Delete environment variables accidentally
- Deploy without testing locally (if possible)

---

## Quick Command Reference

**No commands needed!** Everything is done through:

- **GitHub Web UI:** Edit code
- **Railway Dashboard:** Deploy & manage
- **Browser:** Access your app

**That's the beauty of this method!** 🎉

---

## Summary: Your Workflow

```
Write/Edit Code on GitHub Web
         ↓
Commit Changes (click button)
         ↓
Railway Detects Changes
         ↓
Railway Builds & Deploys Automatically
         ↓
Your Site Updates (2-5 minutes)
         ↓
Check Your Website
         ↓
🎉 Done!
```

**No terminal. No command line. Just web browsers!**

---

## Next Steps

Now that your app is deployed:

1. ✅ Share your Railway URL with friends
2. ✅ Set up custom domain (optional)
3. ✅ Configure Zoho Mail for emails
4. ✅ Monitor usage in Railway dashboard
5. ✅ Edit code directly on GitHub
6. ✅ Watch automatic deployments!

---

## Important Links

**Your Railway Dashboard:**
→ https://railway.app/dashboard

**Your GitHub Repository:**
→ https://github.com/yourusername/harmonia-app

**Railway Documentation:**
→ https://docs.railway.app/

**Get Help:**
→ https://help.railway.app/

---

## You Did It! 🎉

You've deployed Harmonia without touching a command line!

**What you achieved:**
- ✅ Code hosted on GitHub
- ✅ App deployed on Railway
- ✅ Automatic updates from GitHub
- ✅ Live website with HTTPS
- ✅ No terminal needed!

**Managing your app:**
- Edit on GitHub → Auto-deploys to Railway
- Change settings via Railway dashboard
- View logs in your browser
- Monitor usage visually

**You're a web developer now!** 🚀

---

## Bonus: Railway Mobile App

Railway has a mobile app!

**Download:**
- iOS: Search "Railway" in App Store
- Android: Search "Railway" in Play Store

**Features:**
- View logs on the go
- Monitor deployments
- Restart services
- Check usage

Perfect for checking your app while away from computer!

---

**Congratulations! Your Harmonia app is live!** 🎊
