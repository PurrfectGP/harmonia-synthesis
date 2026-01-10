# Harmonia - Complete Beginner's Deployment Guide

## 📚 Table of Contents
1. [What You're Going to Do](#what-youre-going-to-do)
2. [What You'll Need](#what-youll-need)
3. [Understanding the Basics](#understanding-the-basics)
4. [Step 1: Buy and Set Up Contabo Server](#step-1-buy-and-set-up-contabo-server)
5. [Step 2: Register Your Domain with Cloudflare](#step-2-register-your-domain-with-cloudflare)
6. [Step 3: Set Up Zoho Mail](#step-3-set-up-zoho-mail)
7. [Step 4: Get Your Gemini API Key](#step-4-get-your-gemini-api-key)
8. [Step 5: Connect to Your Server](#step-5-connect-to-your-server)
9. [Step 6: Install Required Software](#step-6-install-required-software)
10. [Step 7: Upload Harmonia Application](#step-7-upload-harmonia-application)
11. [Step 8: Configure Your Settings](#step-8-configure-your-settings)
12. [Step 9: Start the Application](#step-9-start-the-application)
13. [Step 10: Configure Domain and SSL](#step-10-configure-domain-and-ssl)
14. [Step 11: Test Everything](#step-11-test-everything)
15. [Troubleshooting for Beginners](#troubleshooting-for-beginners)
16. [Daily Maintenance](#daily-maintenance)

---

## What You're Going to Do

Think of this like building a house:
1. **Contabo** = Your land (where your app lives)
2. **Domain** = Your address (yourdomain.com)
3. **Cloudflare** = Your security system + fast delivery service
4. **Zoho Mail** = Your mailbox (for sending emails)
5. **Harmonia** = Your actual house (the application)

By the end, people will type `yourdomain.com` in their browser and see your Harmonia app!

**Total Time**: 3-4 hours (take breaks!)
**Difficulty**: Beginner-friendly (we'll explain everything!)
**Cost**: ~$10-20/month

---

## What You'll Need

### 1. **A Computer** (Windows, Mac, or Linux)
   - You'll use this to control everything
   - Needs internet connection

### 2. **Money for Services** (~$10-20/month)
   - **Contabo Server**: €6-10/month (~$7-12)
   - **Domain Name**: $10-15/year (~$1/month)
   - **Cloudflare**: FREE!
   - **Zoho Mail**: FREE (for up to 5 email addresses)!
   - **Gemini API**: FREE (with limits)!

### 3. **Credit Card or PayPal**
   - For Contabo and domain registration

### 4. **Email Address**
   - For creating accounts

### 5. **About 3-4 Hours**
   - Don't rush! Take your time.

---

## Understanding the Basics

### What is a Server?
A **server** is just a computer that runs 24/7 in a data center. Instead of buying a computer and leaving it on all the time at home, you rent one from Contabo.

### What is a Domain?
A **domain** is your website address (like `google.com` or `facebook.com`). You'll buy one like `yourawesomeapp.com`.

### What is Cloudflare?
**Cloudflare** makes your website:
- **Faster** (they copy your site to servers worldwide)
- **Safer** (they block hackers)
- **Secure** (they give you the padlock 🔒 in the browser)

### What is Zoho Mail?
**Zoho Mail** lets you send emails from your domain (like `hello@yourdomain.com`) instead of `gmail.com`.

### What is SSH?
**SSH** is how you control your server from your computer. Think of it like remote control for your server.

### What is Docker?
**Docker** is like a shipping container for your app - it packages everything together so it works the same everywhere.

---

## Step 1: Buy and Set Up Contabo Server

### What We're Doing:
Renting a computer that runs 24/7 to host your application.

### Instructions:

#### 1.1: Go to Contabo Website
1. Open your browser
2. Go to: https://contabo.com
3. Click **"VPS"** in the top menu

#### 1.2: Choose a VPS Plan
**Recommended: Cloud VPS M**
- 4 vCPU Cores
- 8 GB RAM
- 200 GB SSD
- Price: ~€6.99/month

**Why this plan?**
- Powerful enough for Harmonia
- Not too expensive
- Good for starting out

**Click "Order"**

#### 1.3: Configure Your VPS

You'll see a form with options:

**Region**: Choose closest to you
- USA → United States
- Europe → Germany or UK
- Asia → Singapore

**Period**:
- Choose "1 Month" for now (you can extend later)

**Operating System**:
- **Important!** Choose: **Ubuntu 22.04**
- ❌ Don't choose other versions!

**Storage**:
- Keep default (200 GB is plenty)

**Object Storage**:
- Select "No" (you don't need this)

**Password**:
- Create a strong password
- ⚠️ **WRITE THIS DOWN!** You'll need it to access your server
- Example: `MySecurePassword123!`

#### 1.4: Complete Purchase
1. Click "Continue"
2. Review your order
3. Create a Contabo account (if you don't have one)
4. Enter payment details
5. Agree to terms
6. Click "Order Now"

#### 1.5: Wait for Setup Email
- Contabo will send you an email (usually within 1-2 hours)
- **Subject**: "Your VPS is ready"
- Email contains:
  - **IP Address**: (like `123.456.789.0`)
  - **Username**: `root`
  - **Password**: The one you created

⚠️ **Save this email! You need this information!**

---

## Step 2: Register Your Domain with Cloudflare

### What We're Doing:
Getting your website address (domain name) and setting up security/speed.

### Instructions:

#### 2.1: Choose a Domain Name

Think of a good name for your site:
- Keep it short and memorable
- Use only letters, numbers, and hyphens
- Examples: `harmonia-app.com`, `mycompatibility.com`

**Check if it's available**:
1. Go to https://www.namecheap.com or https://www.godaddy.com
2. Type your desired name in the search box
3. See if it's available
4. If taken, try another name

#### 2.2: Buy the Domain

**Using Namecheap** (recommended):

1. Go to https://www.namecheap.com
2. Search for your domain name
3. Click "Add to Cart" (usually $10-15/year)
4. Click "View Cart"
5. **Don't buy extras!** Uncheck:
   - ❌ WhoisGuard (not needed, Cloudflare provides privacy)
   - ❌ Premium DNS (not needed)
   - ❌ Email (you'll use Zoho)
6. Click "Confirm Order"
7. Create account / Log in
8. Enter payment details
9. Complete purchase

**You now own the domain!** 🎉

#### 2.3: Create Cloudflare Account

1. Go to https://dash.cloudflare.com/sign-up
2. Enter your email address
3. Create a strong password
4. Click "Sign Up"
5. Check your email for verification link
6. Click the verification link

#### 2.4: Add Your Domain to Cloudflare

1. Log in to Cloudflare dashboard
2. Click the **"Add a Site"** button
3. Enter your domain name (example: `yourdomain.com`)
4. Click "Add Site"
5. Select the **FREE** plan
6. Click "Continue"

#### 2.5: Cloudflare Scans Your Domain

- Cloudflare will scan for existing DNS records
- This takes about 1 minute
- Just wait for it to finish
- Click "Continue" when it's done

#### 2.6: Update Nameservers

**This is the most important step!**

Cloudflare will show you two nameservers that look like this:
```
bob.ns.cloudflare.com
jane.ns.cloudflare.com
```

**⚠️ Write these down or keep this tab open!**

Now go back to where you bought your domain:

**If you used Namecheap**:

1. Go to https://ap.www.namecheap.com
2. Log in
3. Click "Domain List" on the left sidebar
4. Find your domain and click "Manage"
5. Find the "Nameservers" section
6. Change from "Namecheap BasicDNS" to "Custom DNS"
7. Enter the two Cloudflare nameservers:
   - Nameserver 1: `bob.ns.cloudflare.com` (use your actual values)
   - Nameserver 2: `jane.ns.cloudflare.com` (use your actual values)
8. Click the green checkmark ✓ to save

**If you used GoDaddy**:

1. Go to https://dcc.godaddy.com/domains
2. Log in
3. Find your domain and click the three dots (⋯)
4. Click "Manage DNS"
5. Scroll down to "Nameservers"
6. Click "Change"
7. Select "Enter my own nameservers (advanced)"
8. Enter the two Cloudflare nameservers
9. Click "Save"

#### 2.7: Wait for Propagation

- DNS changes take time to spread across the internet
- This is called "propagation"
- Usually takes: 5 minutes to 2 hours (sometimes up to 24 hours)
- Cloudflare will email you when it's active

**While you wait**: Go to next steps! You can come back to Cloudflare later.

---

## Step 3: Set Up Zoho Mail

### What We're Doing:
Setting up email so your app can send emails like `noreply@yourdomain.com`.

### Instructions:

#### 3.1: Create Zoho Mail Account

1. Go to https://www.zoho.com/mail/
2. Click "GET STARTED"
3. Click "Get started for Free"
4. Enter your email address (your personal email)
5. Create a password
6. Click "Sign Up"
7. Verify your email (check inbox for verification email)

#### 3.2: Add Your Domain to Zoho Mail

1. After logging in, you'll see "Add your domain"
2. Enter your domain name (example: `yourdomain.com`)
3. Click "Add Domain"
4. Zoho will ask "How do you plan to use this domain?"
5. Select "For business communication"
6. Click "Proceed"

#### 3.3: Verify You Own the Domain

Zoho needs to confirm you own the domain.

**You'll see a verification code that looks like this:**
```
zoho-verification=zb123456789.zmverify.zoho.com
```

**⚠️ Keep this tab open! We'll use it in the next step.**

Now, let's add this to Cloudflare:

1. Go back to Cloudflare dashboard (https://dash.cloudflare.com)
2. Click on your domain
3. Click "DNS" in the left sidebar
4. Click "Add record" button
5. Fill in:
   - **Type**: Select "TXT"
   - **Name**: Type `@`
   - **Content**: Paste the Zoho verification code
   - **TTL**: Leave as "Auto"
6. Click "Save"

**Go back to Zoho and click "Verify"**
- If it says "Verified" → Great! Continue to next step
- If it says "Not Verified Yet" → Wait 5 minutes and try again

#### 3.4: Add Email Records (MX Records)

MX records tell the internet where to send emails for your domain.

**Stay in Cloudflare DNS settings**:

**Add MX Record 1:**
1. Click "Add record"
2. **Type**: Select "MX"
3. **Name**: Type `@`
4. **Mail server**: Type `mx.zoho.com`
5. **Priority**: Type `10`
6. **TTL**: Leave as "Auto"
7. Click "Save"

**Add MX Record 2:**
1. Click "Add record" again
2. **Type**: Select "MX"
3. **Name**: Type `@`
4. **Mail server**: Type `mx2.zoho.com`
5. **Priority**: Type `20`
6. **TTL**: Leave as "Auto"
7. Click "Save"

**Add MX Record 3:**
1. Click "Add record" again
2. **Type**: Select "MX"
3. **Name**: Type `@`
4. **Mail server**: Type `mx3.zoho.com`
5. **Priority**: Type `50`
6. **TTL**: Leave as "Auto"
7. Click "Save"

#### 3.5: Add SPF Record

SPF helps prevent your emails from going to spam.

**In Cloudflare DNS:**
1. Click "Add record"
2. **Type**: Select "TXT"
3. **Name**: Type `@`
4. **Content**: Type exactly: `v=spf1 include:zoho.com ~all`
5. **TTL**: Leave as "Auto"
6. Click "Save"

#### 3.6: Add DKIM Record (Advanced Security)

**Go back to Zoho Mail:**
1. Look for "Email Configuration" or "DKIM"
2. You'll see a DKIM key (long text starting with `k=rsa; p=...`)
3. **Copy this entire key**

**In Cloudflare DNS:**
1. Click "Add record"
2. **Type**: Select "TXT"
3. **Name**: Type `zoho._domainkey`
4. **Content**: Paste the DKIM key from Zoho
5. **TTL**: Leave as "Auto"
6. Click "Save"

**Go back to Zoho and verify DKIM**

#### 3.7: Create Email Accounts

**In Zoho Mail Control Panel:**

1. Click "Users" or "User Details"
2. Click "Add User"

**Create first account:**
- **Email**: `noreply`
- This creates: `noreply@yourdomain.com`
- **First Name**: `No Reply`
- **Last Name**: `Harmonia`
- **Password**: Create a strong password and **write it down!**
- Click "Add"

**Create second account:**
- **Email**: `support`
- This creates: `support@yourdomain.com`
- **First Name**: `Support`
- **Last Name**: `Harmonia`
- **Password**: Create a strong password and **write it down!**
- Click "Add"

#### 3.8: Generate App-Specific Password

**⚠️ IMPORTANT**: Don't use your main Zoho password in the app!

1. Go to Zoho Accounts: https://accounts.zoho.com/home
2. Click on your profile picture (top right)
3. Click "My Account"
4. Click "Security" tab
5. Scroll to "Application-Specific Passwords"
6. Click "Generate New Password"
7. Name it: `Harmonia App`
8. Click "Generate"
9. **⚠️ COPY THIS PASSWORD AND SAVE IT SOMEWHERE SAFE!**
   - You can only see it once!
   - This is what you'll use in your `.env` file
   - Example: `abcd1234efgh5678`

**You're done with Zoho Mail setup!** 🎉

---

## Step 4: Get Your Gemini API Key

### What We're Doing:
Getting a free API key from Google so Harmonia can use AI features.

### Instructions:

#### 4.1: Go to Google AI Studio

1. Open your browser
2. Go to: https://aistudio.google.com/apikey
3. Sign in with your Google account (Gmail)

#### 4.2: Create API Key

1. You'll see "Get API key" button
2. Click "Create API key"
3. Select "Create API key in new project"
4. Click "Create"

#### 4.3: Save Your API Key

You'll see a key that looks like this:
```
AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX
```

**⚠️ CRITICAL: Copy this key and save it somewhere safe!**
- Write it in a note on your phone
- Save it in a password manager
- Put it in a text file on your computer
- **Never share this key with anyone!**

**You're done getting your API key!** 🎉

---

## Step 5: Connect to Your Server

### What We're Doing:
Using SSH to connect to your Contabo server so you can control it.

### Instructions:

#### For Windows Users:

**5.1: Download PuTTY** (Free SSH program)

1. Go to: https://www.putty.org/
2. Click "Download PuTTY"
3. Download "putty.exe"
4. Run the installer
5. Follow the installation wizard (click "Next" until done)

**5.2: Connect to Your Server**

1. Open PuTTY (search for it in Windows Start menu)
2. You'll see a configuration window
3. In "Host Name" box, type your server IP address
   - Get this from the Contabo email
   - Example: `123.456.789.0`
4. Leave "Port" as `22`
5. Leave "Connection type" as `SSH`
6. Click "Open" button at the bottom

**5.3: Accept Security Alert**

- First time you'll see a security warning
- Click "Yes" or "Accept"
- This is normal!

**5.4: Log In**

You'll see a black terminal window:

```
login as:
```

Type: `root` and press Enter

```
password:
```

Type your Contabo password (you won't see it being typed - this is normal!)
Press Enter

**If you're connected, you'll see something like:**
```
Welcome to Ubuntu 22.04
root@vps-123456:~#
```

**🎉 You're connected to your server!**

#### For Mac Users:

**5.1: Open Terminal**

1. Press `Cmd + Space` to open Spotlight
2. Type `Terminal`
3. Press Enter

**5.2: Connect to Your Server**

Type this command (replace with your actual IP):
```bash
ssh root@123.456.789.0
```

Press Enter

**5.3: Accept Fingerprint**

You'll see a message like:
```
Are you sure you want to continue connecting (yes/no)?
```

Type: `yes` and press Enter

**5.4: Enter Password**

```
password:
```

Type your Contabo password (you won't see it - this is normal!)
Press Enter

**If successful, you'll see:**
```
Welcome to Ubuntu 22.04
root@vps-123456:~#
```

**🎉 You're connected!**

---

## Step 6: Install Required Software

### What We're Doing:
Installing Docker, Docker Compose, Nginx, and other tools your app needs.

**⚠️ Important**: Copy and paste these commands one at a time!

### Instructions:

#### 6.1: Update Your Server

First, let's make sure everything is up to date:

```bash
apt update && apt upgrade -y
```

**What this does**: Updates the list of available software

**Press Enter and wait** (may take 2-5 minutes)

You'll see a lot of text scrolling. That's normal!

#### 6.2: Install Docker

Docker is like a container for your app.

**Copy and paste this command:**

```bash
curl -fsSL https://get.docker.com | sh
```

**Press Enter and wait** (may take 3-5 minutes)

**How to know it worked**: You'll see "Docker installed successfully"

#### 6.3: Install Docker Compose

This helps manage Docker containers.

```bash
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Press Enter, then:

```bash
chmod +x /usr/local/bin/docker-compose
```

Press Enter

**Verify it worked:**
```bash
docker-compose --version
```

You should see something like: `docker-compose version 2.x.x`

#### 6.4: Install Nginx

Nginx is like a traffic controller for your website.

```bash
apt install -y nginx
```

Press Enter and wait (1-2 minutes)

#### 6.5: Install Git

Git helps us download the Harmonia code.

```bash
apt install -y git
```

Press Enter

#### 6.6: Set Up Firewall

A firewall blocks bad guys from accessing your server.

**Allow SSH** (so you can still connect):
```bash
ufw allow 22/tcp
```

**Allow HTTP** (for websites):
```bash
ufw allow 80/tcp
```

**Allow HTTPS** (for secure websites):
```bash
ufw allow 443/tcp
```

**Turn on the firewall:**
```bash
ufw --force enable
```

**Check it's working:**
```bash
ufw status
```

You should see:
```
Status: active
22/tcp    ALLOW    Anywhere
80/tcp    ALLOW    Anywhere
443/tcp   ALLOW    Anywhere
```

**🎉 All software installed!**

---

## Step 7: Upload Harmonia Application

### What We're Doing:
Getting the Harmonia code onto your server.

### Instructions:

#### 7.1: Create Application Folder

```bash
mkdir -p /opt/harmonia
```

Press Enter

This creates a folder to store your app.

#### 7.2: Go to That Folder

```bash
cd /opt/harmonia
```

Press Enter

Now you're "inside" that folder.

#### 7.3: Download Harmonia Code

**If your code is on GitHub:**

```bash
git clone https://github.com/YourUsername/harmonia-synthesis.git .
```

**Replace `YourUsername` with your actual GitHub username!**

Press Enter and wait (1-2 minutes)

**If you don't have it on GitHub yet:**

We'll upload it manually:

1. On your computer, find your Harmonia folder
2. Compress it into a ZIP file
3. Use a program like WinSCP (Windows) or Cyberduck (Mac) to upload
4. Extract the ZIP on the server

**For beginners, I recommend:**
1. Create a GitHub account (https://github.com)
2. Upload your code there
3. Then use the git clone command above

**🎉 Code is on your server!**

---

## Step 8: Configure Your Settings

### What We're Doing:
Creating a file with all your passwords and settings.

### Instructions:

#### 8.1: Copy the Example File

```bash
cp .env.example .env
```

Press Enter

This creates a copy of the example file.

#### 8.2: Edit the File

```bash
nano .env
```

Press Enter

You'll see a text editor with lots of settings.

#### 8.3: Fill in Your Information

**Use arrow keys to move around**

Find these lines and change them:

**1. Gemini API Key:**
```bash
GEMINI_API_KEY=AIzaSy...your-actual-key-here
```
Replace with your actual Gemini API key (from Step 4)

**2. Your Domain:**
```bash
DOMAIN=yourdomain.com
```
Replace with your actual domain (like `myapp.com`)

**3. Zoho Email:**
```bash
SMTP_USER=noreply@yourdomain.com
```
Replace `yourdomain.com` with your actual domain

**4. Zoho Password:**
```bash
SMTP_PASSWORD=your-zoho-app-specific-password-here
```
Replace with the app-specific password from Step 3.8

**5. From Email:**
```bash
FROM_EMAIL=noreply@yourdomain.com
REPLY_TO_EMAIL=support@yourdomain.com
```
Replace `yourdomain.com` with your actual domain

**6. Check Other Settings:**

These should already be correct, but verify:
```bash
SMTP_HOST=smtp.zoho.com
SMTP_PORT=465
SMTP_USE_SSL=true
PROTOCOL=https
GEMINI_MODEL=gemini-3-pro-preview
```

#### 8.4: Save the File

1. Press `Ctrl + X` (this means "exit")
2. It will ask: "Save modified buffer?"
3. Press `Y` (yes)
4. Press `Enter` to confirm the filename

**🎉 Configuration complete!**

---

## Step 9: Start the Application

### What We're Doing:
Building and starting your Harmonia app.

### Instructions:

#### 9.1: Build the Application

```bash
docker-compose build
```

Press Enter and wait (this takes 5-10 minutes!)

You'll see lots of text - this is normal!

**You'll know it's done when you see:**
```
Successfully built xxxxx
Successfully tagged harmonia:latest
```

#### 9.2: Start the Application

```bash
docker-compose up -d
```

Press Enter

The `-d` means "detached" - it runs in the background.

**You'll see:**
```
Creating harmonia-app ... done
```

#### 9.3: Check If It's Running

```bash
docker ps
```

Press Enter

You should see a table with your running container:
```
CONTAINER ID   IMAGE       STATUS
abc123def      harmonia    Up 2 minutes
```

**If you see "Up X minutes" - it's working!** ✅

#### 9.4: Check the Logs

Let's make sure there are no errors:

```bash
docker-compose logs
```

Press Enter

You'll see a lot of text. Look for:
- ✅ "Gemini 3 Pro initialized"
- ✅ "Email: Enabled"
- ✅ "Application startup complete"

**If you see lots of red text or "ERROR"** - something went wrong. Check Step 8 again.

**🎉 Application is running!**

---

## Step 10: Configure Domain and SSL

### What We're Doing:
Connecting your domain to your server and making it secure (HTTPS with padlock 🔒).

### Instructions:

#### 10.1: Add DNS Records in Cloudflare

Go back to Cloudflare dashboard:

1. Go to https://dash.cloudflare.com
2. Click on your domain
3. Click "DNS" in left sidebar

**Add Main Domain Record:**
1. Click "Add record"
2. **Type**: Select "A"
3. **Name**: Type `@`
4. **IPv4 address**: Type your Contabo server IP (from email)
   - Example: `123.456.789.0`
5. **Proxy status**: Make sure the cloud is **ORANGE** ☁️ (click to toggle)
6. **TTL**: Leave as "Auto"
7. Click "Save"

**Add WWW Record:**
1. Click "Add record" again
2. **Type**: Select "A"
3. **Name**: Type `www`
4. **IPv4 address**: Type your Contabo server IP again
5. **Proxy status**: Make sure the cloud is **ORANGE** ☁️
6. **TTL**: Leave as "Auto"
7. Click "Save"

**Wait 5 minutes for DNS to update**

#### 10.2: Configure Cloudflare SSL

Still in Cloudflare:

1. Click "SSL/TLS" in left sidebar
2. Select "Full" mode
   - Click on "Full" option
   - **Don't choose "Strict" yet**
3. Scroll down and turn ON:
   - ✅ Always Use HTTPS
   - ✅ HTTP Strict Transport Security (HSTS)
   - ✅ Minimum TLS Version 1.2

#### 10.3: Set Up Nginx on Server

Back in your SSH terminal:

```bash
cp deployment/nginx.conf /etc/nginx/sites-available/harmonia
```

Press Enter

Now edit it with your domain:

```bash
nano /etc/nginx/sites-available/harmonia
```

Press Enter

**Find and replace** (use arrow keys and backspace):

Find this line (appears multiple times):
```
server_name yourdomain.com www.yourdomain.com;
```

Replace `yourdomain.com` with your actual domain!

**For example, if your domain is `myapp.com`:**
```
server_name myapp.com www.myapp.com;
```

**Do this for ALL occurrences** (there are 2-3 of them)

**Save**: Press `Ctrl + X`, then `Y`, then `Enter`

#### 10.4: Enable the Site

```bash
rm /etc/nginx/sites-enabled/default
```

This removes the default site.

```bash
ln -s /etc/nginx/sites-available/harmonia /etc/nginx/sites-enabled/
```

This activates your Harmonia site.

#### 10.5: Test Nginx Configuration

```bash
nginx -t
```

You should see:
```
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**If you see "test failed"**: You made a typo. Go back to 10.3 and fix it.

#### 10.6: Restart Nginx

```bash
systemctl restart nginx
```

Press Enter

Check if it's running:
```bash
systemctl status nginx
```

You should see:
```
Active: active (running)
```

Press `q` to exit

**🎉 Domain and SSL configured!**

---

## Step 11: Test Everything

### What We're Doing:
Making sure your website works!

### Instructions:

#### 11.1: Test Domain Resolution

On your computer (not the server), open Command Prompt (Windows) or Terminal (Mac):

**Windows:**
1. Press `Windows + R`
2. Type `cmd`
3. Press Enter

**Mac:**
1. Press `Cmd + Space`
2. Type `Terminal`
3. Press Enter

**Type this command:**
```bash
ping yourdomain.com
```

Replace `yourdomain.com` with your actual domain!

**You should see:**
```
Reply from 123.456.789.0: bytes=32 time=50ms
```

**If you see "Request timed out"** - DNS hasn't propagated yet. Wait 30 minutes and try again.

Press `Ctrl + C` to stop the ping.

#### 11.2: Test HTTPS in Browser

1. Open your browser (Chrome, Firefox, Safari, etc.)
2. Type in address bar: `https://yourdomain.com` (use your actual domain!)
3. Press Enter

**What you should see:**
- 🔒 Green padlock in address bar
- Your Harmonia website loads!

**If you see "Not Secure" warning:**
- Wait 5-10 minutes for SSL to activate
- Make sure you set Cloudflare SSL to "Full"

#### 11.3: Test Health Endpoint

In your browser, go to:
```
https://yourdomain.com/api/health
```

You should see:
```json
{"status": "running"}
```

**If you see this, your app is working!** ✅

#### 11.4: Test Email Functionality

Back in your SSH terminal:

```bash
docker-compose exec harmonia python -c "from services.email_service import EmailService; s = EmailService(); print('Email enabled:', s.enabled)"
```

Press Enter

You should see:
```
Email enabled: True
```

**If you see "False":**
- Check your `.env` file (Step 8)
- Make sure you used the app-specific password
- Verify SMTP settings

#### 11.5: Test the Full Website

In your browser:
1. Go to `https://yourdomain.com`
2. Click around
3. Try to create a profile
4. Upload a test image
5. Generate a test report

**Everything working?** 🎉 **You're done!**

---

## Troubleshooting for Beginners

### Problem: Can't connect via SSH

**Solution:**
1. Double-check your server IP address
2. Make sure you're using `root` as username
3. Check your password (copy-paste it from Contabo email)
4. Wait a few hours - server might still be setting up

### Problem: "Permission denied" errors

**Solution:**
Make sure you're logged in as `root`:
```bash
whoami
```

Should say `root`. If not, type:
```bash
su root
```

### Problem: Website shows "502 Bad Gateway"

**Solution:**
1. Check if Docker is running:
   ```bash
   docker ps
   ```
2. Restart the app:
   ```bash
   docker-compose restart
   ```
3. Check logs for errors:
   ```bash
   docker-compose logs
   ```

### Problem: Domain doesn't work

**Solution:**
1. Check DNS propagation: https://dnschecker.org
2. Enter your domain and check if it shows your server IP
3. If not, wait longer (can take 24 hours)
4. Verify Cloudflare nameservers are set correctly

### Problem: "Connection refused" or can't access website

**Solution:**
1. Check firewall:
   ```bash
   ufw status
   ```
2. Make sure ports 80 and 443 are allowed
3. Check Nginx is running:
   ```bash
   systemctl status nginx
   ```

### Problem: Emails not sending

**Solution:**
1. Verify MX records in Cloudflare
2. Use `dig MX yourdomain.com` to check
3. Make sure you're using **app-specific password** not main password
4. Check email settings in `.env` file
5. Restart application:
   ```bash
   docker-compose restart
   ```

### Problem: "Out of space" errors

**Solution:**
1. Check disk space:
   ```bash
   df -h
   ```
2. Clean up Docker:
   ```bash
   docker system prune -a
   ```
3. Type `y` when prompted

### Problem: Forgot my password

**Which password?**

- **Contabo**: Reset through Contabo control panel
- **SSH**: Contact Contabo support
- **Zoho**: Reset at https://accounts.zoho.com
- **Cloudflare**: Reset at login page

---

## Daily Maintenance

### Every Day (5 minutes):

#### Check if everything is running:

```bash
cd /opt/harmonia
docker ps
```

You should see your container with "Up X hours"

#### Check for errors:

```bash
docker-compose logs --tail=50
```

Look for red text or "ERROR"

### Every Week (10 minutes):

#### Update your system:

```bash
apt update && apt upgrade -y
```

#### Check disk space:

```bash
df -h
```

If "Use%" is over 80%, you need to clean up:
```bash
docker system prune -a
```

#### Backup your data:

```bash
cd /opt/harmonia
tar -czf backup-$(date +%Y%m%d).tar.gz uploads/ harmonia_outputs/
```

Download this backup file to your computer!

### Every Month:

1. Review Cloudflare analytics
2. Check for any security alerts
3. Review application logs
4. Test email functionality
5. Update Harmonia if there's a new version

---

## Getting Help

### Where to Ask:

1. **GitHub Issues**: https://github.com/yourusername/harmonia-synthesis/issues
2. **Contabo Support**: support@contabo.com
3. **Cloudflare Community**: https://community.cloudflare.com
4. **Zoho Support**: https://help.zoho.com

### Before Asking:

1. Check this guide again
2. Check logs: `docker-compose logs`
3. Google the error message
4. Take screenshots of errors

### Information to Provide:

- What step you're on
- What you were trying to do
- The exact error message
- Screenshots
- Your setup (Windows/Mac, domain provider, etc.)

---

## Congratulations! 🎉

You've successfully deployed Harmonia!

You now have:
- ✅ A running server on Contabo
- ✅ A custom domain with HTTPS
- ✅ Email functionality through Zoho
- ✅ Fast delivery through Cloudflare
- ✅ A professional web application

**You did it, even with no experience!** 🚀

### What's Next?

1. Share your website with friends
2. Monitor it daily
3. Keep learning about web hosting
4. Consider adding more features
5. Set up automatic backups

### Bookmark These Pages:

- Your Cloudflare Dashboard: https://dash.cloudflare.com
- Your Zoho Mail: https://mail.zoho.com
- Contabo Control Panel: https://my.contabo.com
- Google AI Studio: https://aistudio.google.com

**Welcome to the world of web hosting!** 🌐
