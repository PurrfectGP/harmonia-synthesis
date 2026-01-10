# Zoho Mail Setup Guide for Complete Beginners

## What is Zoho Mail?

Zoho Mail lets you have professional email addresses using YOUR domain name:

**Instead of:**
- ❌ `yourname123@gmail.com`
- ❌ `business.email@yahoo.com`

**You get:**
- ✅ `hello@yourdomain.com`
- ✅ `support@yourdomain.com`
- ✅ `noreply@yourdomain.com`

**Why is this good?**
- Looks professional
- Builds trust
- FREE for up to 5 email addresses!

---

## What You'll Need

- ✅ Your domain name already registered
- ✅ Access to Cloudflare (where your DNS is)
- ✅ 30-45 minutes
- ✅ An existing personal email (Gmail, Yahoo, etc.)

---

## Part 1: Create Zoho Mail Account

### Step 1.1: Go to Zoho Mail

1. Open your web browser
2. Go to: https://www.zoho.com/mail/
3. You'll see the Zoho Mail homepage

### Step 1.2: Start Sign Up

1. Look for a button that says **"Sign Up"** or **"Get Started"**
2. Click it
3. Or go directly to: https://www.zoho.com/mail/zohomail-pricing.html
4. Click **"Get started for Free"** under the FREE plan

### Step 1.3: Fill in Sign Up Form

You'll see a form asking for:

**Your Email Address:**
- Use your personal email (Gmail, Yahoo, etc.)
- Example: `yourpersonal@gmail.com`
- **This is NOT the email you're creating!**
- This is just for logging into Zoho

**Create a Password:**
- At least 8 characters
- Mix of letters, numbers, symbols
- Example: `ZohoPass123!`
- **⚠️ Write this down!**

**Your Name:**
- First name
- Last name

**Country:**
- Select your country from dropdown

**Phone Number:**
- Your real phone number
- They might send you a verification code

### Step 1.4: Complete Verification

1. Click **"Sign Up"** or **"Get Started"**
2. **Check your email** (the personal one you used)
3. You'll get an email from Zoho
4. **Click the verification link** in the email
5. Your browser will open and say "Verified!"

**🎉 You now have a Zoho account!**

---

## Part 2: Add Your Domain to Zoho

### Step 2.1: Access Zoho Mail Control Panel

After verification, you should be in the Zoho Mail dashboard.

**If not:**
1. Go to: https://mailadmin.zoho.com
2. Log in with your Zoho account

### Step 2.2: Add Domain

1. Look for **"Add Domain"** or **"Get Started"**
2. Click it
3. You'll see a form

### Step 2.3: Enter Your Domain

1. In the text box, type your domain name
   - Example: `myawesomeapp.com`
   - **Just the domain! No `https://` or `www.`**
2. Click **"Add Domain"** or **"Continue"**

### Step 2.4: Choose Domain Purpose

Zoho asks: "How do you plan to use this domain?"

Options:
- **For business communication** ✅ **← Choose this**
- For personal use
- For education

Click your choice, then click **"Proceed"** or **"Continue"**

### Step 2.5: Accept Terms

1. Read the terms (or just scroll down 😉)
2. Check the box: "I agree to terms"
3. Click **"Proceed"**

**🎉 Domain added to Zoho!**

---

## Part 3: Verify You Own the Domain

### Why Do This?

Zoho needs proof that you actually own the domain. Anyone could try to add `google.com` to their Zoho account, so they need verification!

### Step 3.1: Get Verification Code

You'll see a screen that says "Verify Domain Ownership"

It will show you a code that looks like this:
```
zoho-verification=zb1234567890.zmverify.zoho.com
```

**⚠️ IMPORTANT:**
- **Copy this entire code**
- **OR keep this browser tab open**
- You'll need it in the next step!

### Step 3.2: Add Verification Code to Cloudflare

Now we need to add this code to your Cloudflare DNS settings.

**Open a new browser tab:**
1. Go to: https://dash.cloudflare.com
2. Log in to Cloudflare
3. Click on your domain name
4. Click **"DNS"** in the left sidebar

**Add TXT Record:**
1. Click **"Add record"** button
2. Fill in the form:
   - **Type**: Select **"TXT"** from dropdown
   - **Name**: Type **`@`** (just the @ symbol)
   - **Content**: Paste your Zoho verification code
     - Should be: `zoho-verification=zb1234567890.zmverify.zoho.com`
   - **TTL**: Leave as **"Auto"**
3. Click **"Save"**

### Step 3.3: Verify in Zoho

1. Go back to the Zoho tab
2. Click **"Verify"** or **"Verify Now"** button
3. Wait a few seconds...

**Two possible outcomes:**

**✅ If it says "Verified":**
- Great! Continue to next step!

**❌ If it says "Not Verified" or "Failed":**
- Wait 5 minutes
- Click "Verify" again
- Still failing? Double-check you pasted the code correctly in Cloudflare
- Make sure there are no extra spaces

**🎉 Domain verified!**

---

## Part 4: Set Up Email Delivery (MX Records)

### What are MX Records?

MX stands for "Mail Exchange". These records tell the internet:
> "If someone sends an email to me@yourdomain.com, send it to Zoho's servers!"

### Step 4.1: Stay in Cloudflare DNS

Make sure you're still in:
- Cloudflare Dashboard
- Your domain
- DNS section

### Step 4.2: Add First MX Record

1. Click **"Add record"**
2. Fill in:
   - **Type**: Select **"MX"**
   - **Name**: Type **`@`**
   - **Mail server**: Type **`mx.zoho.com`**
     - (Exactly like that - all lowercase!)
   - **Priority**: Type **`10`**
   - **Proxy status**: Make sure the cloud is **GRAY** ☁️ (not orange!)
     - If it's orange, click it to make it gray
   - **TTL**: Leave as **"Auto"**
3. Click **"Save"**

### Step 4.3: Add Second MX Record

1. Click **"Add record"** again
2. Fill in:
   - **Type**: Select **"MX"**
   - **Name**: Type **`@`**
   - **Mail server**: Type **`mx2.zoho.com`**
   - **Priority**: Type **`20`**
   - **Proxy status**: **GRAY** ☁️
   - **TTL**: **"Auto"**
3. Click **"Save"**

### Step 4.4: Add Third MX Record

1. Click **"Add record"** once more
2. Fill in:
   - **Type**: Select **"MX"**
   - **Name**: Type **`@`**
   - **Mail server**: Type **`mx3.zoho.com`**
   - **Priority**: Type **`50`**
   - **Proxy status**: **GRAY** ☁️
   - **TTL**: **"Auto"**
3. Click **"Save"**

### Step 4.5: Verify MX Records in Zoho

1. Go back to Zoho Mail tab
2. Click **"Next"** or **"Continue"**
3. Zoho will check your MX records
4. May take 5-10 minutes

**If verified:** Continue to next step!
**If failed:** Wait 10 minutes and try again

**🎉 Email delivery configured!**

---

## Part 5: Add Email Security (SPF, DKIM, DMARC)

### What is This?

These are security features that:
- Stop spammers from pretending to be you
- Prevent your emails from going to spam
- Protect your domain's reputation

**Don't worry - we'll walk through each one!**

---

### SPF Record (Sender Policy Framework)

**What it does:** Tells email providers "These servers can send email from my domain"

**Add SPF Record:**

1. In Cloudflare DNS, click **"Add record"**
2. Fill in:
   - **Type**: Select **"TXT"**
   - **Name**: Type **`@`**
   - **Content**: Type exactly:
     ```
     v=spf1 include:zoho.com ~all
     ```
     - **Copy and paste this to avoid typos!**
   - **TTL**: **"Auto"**
3. Click **"Save"**

---

### DKIM Record (DomainKeys Identified Mail)

**What it does:** Adds a digital signature to your emails proving they're really from you

**Get DKIM Key from Zoho:**

1. In Zoho Mail dashboard
2. Look for **"Email Configuration"** or **"Domain Settings"**
3. Find **"DKIM"** section
4. You'll see a long code starting with `k=rsa; p=MII...`
5. Click **"Copy"** or manually copy this entire text

**⚠️ This code is very long - make sure you copy ALL of it!**

**Add DKIM Record:**

1. In Cloudflare DNS, click **"Add record"**
2. Fill in:
   - **Type**: Select **"TXT"**
   - **Name**: Type **`zoho._domainkey`**
     - (Exactly like that!)
   - **Content**: Paste your entire DKIM key
     - Should start with `k=rsa; p=MII...`
   - **TTL**: **"Auto"**
3. Click **"Save"**

**Verify in Zoho:**
1. Go back to Zoho
2. Click **"Verify DKIM"**
3. Should show "Verified" ✅

---

### DMARC Record (Optional but Recommended)

**What it does:** Tells email providers what to do if someone tries to fake your emails

**Add DMARC Record:**

1. In Cloudflare DNS, click **"Add record"**
2. Fill in:
   - **Type**: Select **"TXT"**
   - **Name**: Type **`_dmarc`**
     - (Starts with underscore!)
   - **Content**: Type exactly:
     ```
     v=DMARC1; p=none; rua=mailto:postmaster@yourdomain.com
     ```
     - **Replace `yourdomain.com` with your actual domain!**
   - **TTL**: **"Auto"**
3. Click **"Save"**

**🎉 Email security configured!**

---

## Part 6: Create Email Accounts

Now let's create your actual email addresses!

### Step 6.1: Access User Management

1. In Zoho Mail dashboard
2. Look for **"Users"** or **"User Details"** in left menu
3. Click it

### Step 6.2: Create First Email Account

Click **"Add User"** or **"Create User"** button

**Fill in the form:**

**Email Address:**
- Type: `noreply`
- This will create: `noreply@yourdomain.com`
- **Why "noreply"?** This is for automated emails from your app

**First Name:**
- Type: `No Reply`

**Last Name:**
- Type: `Harmonia` (or your app name)

**Password:**
- Create a strong password
- Example: `NoReply123!Secure`
- **⚠️ WRITE THIS DOWN!**

**Display Name:**
- Type: `Harmonia` (what people see when they get emails)

Click **"Add"** or **"Create"**

**✅ First email created:** `noreply@yourdomain.com`

### Step 6.3: Create Second Email Account (Support)

Click **"Add User"** again

**Fill in:**

**Email Address:**
- Type: `support`
- Creates: `support@yourdomain.com`
- **Why "support"?** This is where replies go

**First Name:**
- Type: `Support`

**Last Name:**
- Type: `Team`

**Password:**
- Create strong password
- **⚠️ WRITE THIS DOWN!**

**Display Name:**
- Type: `Harmonia Support`

Click **"Add"** or **"Create"**

**✅ Second email created:** `support@yourdomain.com`

### Step 6.4: Create More Emails (Optional)

You can create up to 5 email addresses on the free plan:

**Suggestions:**
- `hello@yourdomain.com` - General inquiries
- `info@yourdomain.com` - Information requests
- `admin@yourdomain.com` - Administrative

---

## Part 7: Generate App-Specific Password

### ⚠️ SUPER IMPORTANT!

**Never use your main Zoho password in applications!**

Instead, create an "app-specific password" - a special password just for your Harmonia app.

**Why?**
- More secure
- If someone steals it, they can't access your Zoho account
- You can delete it anytime without changing your main password

### Step 7.1: Go to Zoho Accounts

1. Open new browser tab
2. Go to: https://accounts.zoho.com/home
3. Log in with your Zoho account

### Step 7.2: Go to Security Settings

1. Click on your profile picture (top right corner)
2. Click **"My Account"** or **"Account"**
3. Look for tabs at the top
4. Click **"Security"** tab

### Step 7.3: Find Application-Specific Passwords

1. Scroll down the Security page
2. Look for section: **"Application-Specific Passwords"**
3. Click **"Generate New Password"** or **"Create"**

### Step 7.4: Generate Password

**Application Name:**
- Type: `Harmonia App`
- This helps you remember what it's for

Click **"Generate"** or **"Create"**

### Step 7.5: COPY THE PASSWORD!

**⚠️ CRITICAL: You can only see this password ONCE!**

You'll see a password like: `abcd1234efgh5678`

**Immediately:**
1. **Copy this password**
2. **Paste it somewhere safe:**
   - Notes app on your phone
   - Password manager
   - Text file on your computer
3. **Label it:** "Zoho App-Specific Password for Harmonia"

**Once you close this window, you can NEVER see it again!**

If you lose it, you'll have to delete it and create a new one.

Click **"Done"** or **"Close"**

**🎉 App-specific password created!**

---

## Part 8: Test Your Email Setup

### Test 8.1: Check MX Records

**On your computer** (not server), open Command Prompt (Windows) or Terminal (Mac):

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
nslookup -type=mx yourdomain.com
```

**(Replace `yourdomain.com` with your actual domain!)**

Press Enter

**You should see:**
```
yourdomain.com  mail exchanger = 10 mx.zoho.com
yourdomain.com  mail exchanger = 20 mx2.zoho.com
yourdomain.com  mail exchanger = 50 mx3.zoho.com
```

**If you see this** ✅ - MX records are working!

### Test 8.2: Send a Test Email

1. Go to Zoho Mail: https://mail.zoho.com
2. Log in with your Zoho account
3. You'll see your inbox
4. Click **"Compose"** or **"New Message"**
5. Send yourself an email:
   - **To:** Your personal email (Gmail, etc.)
   - **From:** Select `noreply@yourdomain.com`
   - **Subject:** `Test Email`
   - **Message:** `Testing my new professional email!`
6. Click **"Send"**

**Check your personal email:**
- You should receive the email
- Check the sender - should show `noreply@yourdomain.com`

**If you received it** ✅ - Email sending works!

### Test 8.3: Reply to Test

1. Reply to the test email you just sent
2. Send the reply
3. Go back to Zoho Mail
4. Check `support@yourdomain.com` inbox
5. You should see the reply

**If you received reply** ✅ - Email receiving works!

---

## Part 9: Summary - What to Use in Your App

### For Your `.env` File

When you set up Harmonia, you'll need these values:

```bash
# Zoho Mail SMTP Settings
SMTP_HOST=smtp.zoho.com
SMTP_PORT=465
SMTP_USE_SSL=true

# Your Email Address
SMTP_USER=noreply@yourdomain.com

# App-Specific Password (NOT your main password!)
SMTP_PASSWORD=abcd1234efgh5678

# Display Settings
FROM_EMAIL=noreply@yourdomain.com
FROM_NAME=Harmonia
REPLY_TO_EMAIL=support@yourdomain.com
```

**Replace:**
- `yourdomain.com` → Your actual domain
- `abcd1234efgh5678` → Your actual app-specific password

---

## Understanding Zoho Mail Dashboard

### Main Sections

**Inbox:**
- Your received emails
- Like any email client

**Compose:**
- Write new emails

**Users:**
- Manage your email accounts
- Add/remove users
- Reset passwords

**Domain Settings:**
- DNS records
- DKIM/SPF verification
- General domain settings

**Email Migration:**
- Import emails from other services (Gmail, etc.)
- We don't need this for now

---

## Troubleshooting for Beginners

### Problem: Can't verify domain

**Solutions:**
1. Wait 10 minutes (DNS needs time)
2. Check you copied verification code exactly
3. Make sure verification TXT record is in Cloudflare
4. Try verifying again

### Problem: Can't receive emails

**Solutions:**
1. Check MX records are added in Cloudflare
2. Make sure MX records are gray (not orange) in Cloudflare
3. Wait 1 hour for DNS propagation
4. Use `nslookup -type=mx yourdomain.com` to verify

### Problem: Emails going to spam

**Solutions:**
1. Make sure SPF record is added
2. Verify DKIM is configured
3. Add DMARC record
4. Don't send too many emails at once
5. Ask recipients to mark as "Not Spam"

### Problem: Can't send emails from app

**Solutions:**
1. Make sure you're using **app-specific password** (not main password!)
2. Check SMTP settings in `.env` file
3. Verify `SMTP_USER` is correct email address
4. Make sure `SMTP_PORT` is `465`
5. Ensure `SMTP_USE_SSL` is `true`

### Problem: "Authentication failed"

**Solution:**
- You're probably using your main password instead of app-specific password
- Go back to Part 7 and create app-specific password
- Use that password in your app

### Problem: Lost app-specific password

**Solution:**
1. Go to https://accounts.zoho.com/home
2. Click "Security" tab
3. Find your Harmonia app password
4. Click "Delete" or trash icon
5. Create a new one (Part 7)

---

## Zoho Mail Mobile App

### Download

**iOS (iPhone/iPad):**
- Open App Store
- Search "Zoho Mail"
- Install

**Android:**
- Open Google Play Store
- Search "Zoho Mail"
- Install

### Set Up

1. Open Zoho Mail app
2. Sign in with your Zoho account
3. You'll see all your email addresses
4. Now you can check emails on the go!

---

## Managing Your Email Accounts

### Access Zoho Mail

**Web:** https://mail.zoho.com

**Mobile:** Use Zoho Mail app

### Change Password

1. Go to https://mailadmin.zoho.com
2. Click "Users"
3. Find the user
4. Click "Reset Password"
5. Enter new password

### Add More Email Addresses

Remember: Free plan allows 5 total email addresses

1. Go to https://mailadmin.zoho.com
2. Click "Users"
3. Click "Add User"
4. Follow steps from Part 6

### Delete Email Address

1. Go to https://mailadmin.zoho.com
2. Click "Users"
3. Find the user
4. Click "Delete" or trash icon
5. Confirm deletion

---

## Email Best Practices

### DO:

✅ Use app-specific passwords in applications
✅ Enable two-factor authentication
✅ Keep passwords secure
✅ Monitor your email activity
✅ Set up email filters
✅ Check spam folder occasionally

### DON'T:

❌ Share your passwords
❌ Use main password in apps
❌ Send spam
❌ Ignore security warnings
❌ Use simple passwords
❌ Share app-specific password publicly

---

## Zoho Mail Limits (Free Plan)

**Storage:**
- 5 GB per user
- Total 25 GB (5 users × 5 GB)

**Email Accounts:**
- Maximum 5 users

**Attachments:**
- Up to 250 MB per email

**Email Sending:**
- No daily limit (but don't spam!)

**Features:**
- ✅ POP/IMAP access
- ✅ Email forwarding
- ✅ Aliases
- ✅ Mobile access
- ✅ Spam protection

---

## Upgrading to Paid Plan (Optional)

If you need more:

**Mail Lite** - $1/user/month
- 10 GB storage per user
- 25 email aliases

**Mail Premium** - $3/user/month
- 50 GB storage per user
- Unlimited aliases
- Priority support
- Advanced filters

**You don't need these to start!**

The free plan is perfect for Harmonia.

---

## Quick Reference

### Your Email Addresses

```
noreply@yourdomain.com  - For automated emails
support@yourdomain.com  - For support replies
```

### SMTP Settings (for your app)

```
Host: smtp.zoho.com
Port: 465
SSL: Yes (true)
Username: noreply@yourdomain.com
Password: [Your app-specific password]
```

### DNS Records in Cloudflare

```
Type  Name              Content              Priority
MX    @                 mx.zoho.com          10
MX    @                 mx2.zoho.com         20
MX    @                 mx3.zoho.com         50
TXT   @                 v=spf1 include:zoho.com ~all
TXT   zoho._domainkey   [Your DKIM key]
TXT   _dmarc            v=DMARC1; p=none; rua=mailto:postmaster@yourdomain.com
```

### Important Links

**Zoho Mail Login:**
→ https://mail.zoho.com

**Admin Control Panel:**
→ https://mailadmin.zoho.com

**Zoho Accounts (for app passwords):**
→ https://accounts.zoho.com/home

**Zoho Support:**
→ https://help.zoho.com

---

## You Did It! 🎉

Congratulations! You now have:

- ✅ Professional email addresses
- ✅ Email security configured
- ✅ App-specific password for your application
- ✅ Ability to send/receive emails

**Your emails now look professional:**
- `hello@yourdomain.com` instead of `yourname@gmail.com`

**Next Steps:**
1. Use these settings in your Harmonia application
2. Test sending emails from your app
3. Monitor your email reputation

**Bookmark this guide** - you might need it later!

**Well done! 📧✨**
