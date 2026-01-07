# Harmonia - Complete Deployment Guide

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Part 1: Contabo Server Setup](#part-1-contabo-server-setup)
4. [Part 2: Cloudflare Configuration](#part-2-cloudflare-configuration)
5. [Part 3: Zoho Mail Setup](#part-3-zoho-mail-setup)
6. [Part 4: Application Deployment](#part-4-application-deployment)
7. [Part 5: Nginx Configuration](#part-5-nginx-configuration)
8. [Part 6: SSL/TLS Setup](#part-6-ssltls-setup)
9. [Part 7: Environment Variables](#part-7-environment-variables)
10. [Part 8: Testing](#part-8-testing)
11. [Part 9: Monitoring & Maintenance](#part-9-monitoring--maintenance)
12. [Troubleshooting](#troubleshooting)

---

## Overview

This guide covers deploying Harmonia on:
- **Hosting**: Contabo VPS
- **Domain & CDN**: Cloudflare
- **Email**: Zoho Mail
- **Reverse Proxy**: Nginx
- **Containerization**: Docker + Docker Compose

**Total Setup Time**: 2-3 hours

---

## Prerequisites

### What You Need:
1. **Contabo VPS** (minimum 4GB RAM, 2 CPU cores)
2. **Domain name** registered with Cloudflare
3. **Zoho Mail** account (free or paid)
4. **Gemini API Key** from Google AI Studio
5. **SSH access** to your Contabo server

### Knowledge Required:
- Basic Linux command line
- SSH and terminal usage
- Basic understanding of DNS

---

## Part 1: Contabo Server Setup

### Step 1.1: Initial Server Access

```bash
# SSH into your Contabo server
ssh root@your-server-ip

# Update system packages
apt update && apt upgrade -y

# Set timezone
timedatectl set-timezone UTC
```

### Step 1.2: Create a Non-Root User

```bash
# Create new user
adduser harmonia

# Add to sudo group
usermod -aG sudo harmonia

# Switch to new user
su - harmonia
```

### Step 1.3: Install Docker

```bash
# Install dependencies
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add user to docker group
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker-compose --version

# Log out and log back in for group changes to take effect
exit
su - harmonia
```

### Step 1.4: Install Nginx

```bash
sudo apt install -y nginx

# Start and enable Nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
```

### Step 1.5: Configure Firewall

```bash
# Install UFW (Uncomplicated Firewall)
sudo apt install -y ufw

# Allow SSH (IMPORTANT: do this first!)
sudo ufw allow 22/tcp

# Allow HTTP and HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable firewall
sudo ufw --force enable

# Check status
sudo ufw status
```

---

## Part 2: Cloudflare Configuration

### Step 2.1: Add Domain to Cloudflare

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Click "Add a Site"
3. Enter your domain name
4. Select a plan (Free plan works great!)
5. Cloudflare will scan your DNS records

### Step 2.2: Update Nameservers

1. Cloudflare will provide 2 nameservers (e.g., `bob.ns.cloudflare.com`)
2. Go to your domain registrar
3. Update nameservers to Cloudflare's nameservers
4. Wait for propagation (can take up to 24 hours, usually much faster)

### Step 2.3: Configure DNS Records

In Cloudflare DNS settings, add:

| Type  | Name | Content           | Proxy Status | TTL  |
|-------|------|-------------------|--------------|------|
| A     | @    | YOUR_CONTABO_IP   | Proxied (Orange Cloud) | Auto |
| A     | www  | YOUR_CONTABO_IP   | Proxied (Orange Cloud) | Auto |

**Important**: Enable the orange cloud (Proxied) for Cloudflare's CDN and DDoS protection!

### Step 2.4: SSL/TLS Settings

1. Go to **SSL/TLS** → **Overview**
2. Set encryption mode to **Full (strict)** or **Full**
3. Go to **SSL/TLS** → **Edge Certificates**
4. Enable:
   - ✅ Always Use HTTPS
   - ✅ HTTP Strict Transport Security (HSTS)
   - ✅ Minimum TLS Version: 1.2
   - ✅ Opportunistic Encryption
   - ✅ TLS 1.3

### Step 2.5: Get Cloudflare API Credentials

1. Go to **My Profile** → **API Tokens**
2. Create a new token with permissions:
   - Zone → Zone → Read
   - Zone → DNS → Edit
3. Save your **Zone ID** and **API Token**

### Step 2.6: Configure Security Settings

**Under Security → WAF:**
- Set security level to "Medium" or "High"
- Enable Bot Fight Mode (free plan)

**Under Speed → Optimization:**
- Enable Auto Minify (HTML, CSS, JS)
- Enable Brotli compression
- Enable Early Hints

**Under Caching:**
- Set caching level to "Standard"
- Enable "Always Online"

---

## Part 3: Zoho Mail Setup

### Step 3.1: Add Your Domain to Zoho Mail

1. Go to [Zoho Mail](https://www.zoho.com/mail/)
2. Sign up for an account (Free tier allows 5 users)
3. Go to **Control Panel** → **Domains** → **Add Domain**
4. Enter your domain name
5. Follow verification steps

### Step 3.2: Verify Domain Ownership

Add these DNS records in Cloudflare:

**TXT Record for Verification:**
```
Type: TXT
Name: @
Content: zoho-verification=zb123456789.zmverify.zoho.com
```

**MX Records for Email:**
```
Type: MX  | Name: @  | Content: mx.zoho.com  | Priority: 10
Type: MX  | Name: @  | Content: mx2.zoho.com | Priority: 20
Type: MX  | Name: @  | Content: mx3.zoho.com | Priority: 50
```

**SPF Record:**
```
Type: TXT
Name: @
Content: v=spf1 include:zoho.com ~all
```

**DKIM Record** (get from Zoho Mail dashboard):
```
Type: TXT
Name: zoho._domainkey
Content: v=DKIM1; k=rsa; p=YOUR_PUBLIC_KEY_FROM_ZOHO
```

**DMARC Record:**
```
Type: TXT
Name: _dmarc
Content: v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

### Step 3.3: Create Email Accounts

1. In Zoho Mail Control Panel, create:
   - `noreply@yourdomain.com` (for automated emails)
   - `support@yourdomain.com` (for user replies)

### Step 3.4: Generate App-Specific Password

**IMPORTANT**: Never use your main Zoho password in the application!

1. Go to **Zoho Accounts** → [Security](https://accounts.zoho.com/home#security)
2. Click **Application-Specific Passwords**
3. Create a new password for "Harmonia App"
4. **Save this password** - you'll need it for `SMTP_PASSWORD`

### Step 3.5: Test SMTP Connection

```bash
# Install swaks for testing
sudo apt install -y swaks

# Test email sending
swaks --to test@example.com \
      --from noreply@yourdomain.com \
      --server smtp.zoho.com:465 \
      --auth LOGIN \
      --auth-user noreply@yourdomain.com \
      --auth-password "YOUR_APP_SPECIFIC_PASSWORD" \
      --tls
```

---

## Part 4: Application Deployment

### Step 4.1: Prepare Application Directory

```bash
# Create application directory
sudo mkdir -p /opt/harmonia
sudo chown -R harmonia:harmonia /opt/harmonia
cd /opt/harmonia
```

### Step 4.2: Clone or Upload Your Code

**Option A: Using Git (recommended)**
```bash
# Install git if not already installed
sudo apt install -y git

# Clone your repository
git clone https://github.com/yourusername/harmonia-synthesis.git .

# Or if using a specific branch
git clone -b main https://github.com/yourusername/harmonia-synthesis.git .
```

**Option B: Manual Upload**
```bash
# From your local machine, upload files via SCP
scp -r /path/to/harmonia/* harmonia@your-server-ip:/opt/harmonia/
```

### Step 4.3: Create Environment File

```bash
cd /opt/harmonia

# Copy example file
cp .env.example .env

# Edit with your actual values
nano .env
```

Fill in all required values (see Part 7 for complete reference).

### Step 4.4: Build and Start Docker Containers

```bash
# Build the Docker image
docker-compose build

# Start the containers
docker-compose up -d

# Check logs
docker-compose logs -f

# Verify containers are running
docker ps
```

### Step 4.5: Setup Systemd Service (Optional but Recommended)

```bash
# Copy service file
sudo cp deployment/harmonia.service /etc/systemd/system/

# Edit paths if needed
sudo nano /etc/systemd/system/harmonia.service

# Reload systemd
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable harmonia

# Start service
sudo systemctl start harmonia

# Check status
sudo systemctl status harmonia
```

---

## Part 5: Nginx Configuration

### Step 5.1: Install and Configure Nginx

```bash
# Copy Nginx configuration
sudo cp deployment/nginx.conf /etc/nginx/sites-available/harmonia

# Edit the configuration
sudo nano /etc/nginx/sites-available/harmonia

# Update these values:
# - Replace "yourdomain.com" with your actual domain
# - Update upstream if needed
```

### Step 5.2: Enable Site

```bash
# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Enable Harmonia site
sudo ln -s /etc/nginx/sites-available/harmonia /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# If test passes, reload Nginx
sudo systemctl reload nginx
```

### Step 5.3: Check Nginx Status

```bash
sudo systemctl status nginx

# View logs
sudo tail -f /var/log/nginx/harmonia_access.log
sudo tail -f /var/log/nginx/harmonia_error.log
```

---

## Part 6: SSL/TLS Setup

### Option A: Use Cloudflare SSL (Recommended)

If you're using Cloudflare with "Proxied" DNS records:

1. Cloudflare automatically handles SSL between users and Cloudflare
2. You can use Cloudflare's "Full" or "Full (strict)" SSL mode
3. No additional certificate setup needed on your server!

### Option B: Use Let's Encrypt (If not using Cloudflare proxy)

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Test automatic renewal
sudo certbot renew --dry-run

# Certbot will automatically renew certificates
```

---

## Part 7: Environment Variables

### Complete .env File Reference

```bash
# ============================================================================
# GEMINI AI API (REQUIRED)
# ============================================================================
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXX
GEMINI_MODEL=gemini-3-pro-preview

# ============================================================================
# DOMAIN
# ============================================================================
DOMAIN=yourdomain.com
PROTOCOL=https

# ============================================================================
# ZOHO MAIL (REQUIRED FOR EMAILS)
# ============================================================================
SMTP_HOST=smtp.zoho.com
SMTP_PORT=465
SMTP_USE_SSL=true
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your-app-specific-password-here
FROM_EMAIL=noreply@yourdomain.com
FROM_NAME=Harmonia
REPLY_TO_EMAIL=support@yourdomain.com
EMAIL_ENABLED=true
SEND_WELCOME_EMAIL=true
SEND_REPORT_EMAIL=true

# ============================================================================
# SERVER
# ============================================================================
HOST=0.0.0.0
PORT=8000
WORKERS=4
ENVIRONMENT=production
DEBUG=false

# ============================================================================
# SECURITY
# ============================================================================
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
RATE_LIMIT_ENABLED=true
RATE_LIMIT_PER_MINUTE=60

# ============================================================================
# CLOUDFLARE (OPTIONAL)
# ============================================================================
CLOUDFLARE_ENABLED=true
CLOUDFLARE_ZONE_ID=your-zone-id
CLOUDFLARE_API_TOKEN=your-api-token
TRUST_PROXY_HEADERS=true

# ============================================================================
# STORAGE
# ============================================================================
DATA_DIR=./data
UPLOAD_DIR=./uploads
REPORTS_DIR=./harmonia_outputs
MAX_IMAGE_SIZE_MB=10
MAX_DNA_FILE_SIZE_MB=5

# ============================================================================
# LOGGING
# ============================================================================
LOG_LEVEL=INFO
LOG_FILE=./logs/harmonia.log
```

### Security Best Practices:

1. **Never commit .env to Git**
   ```bash
   # Verify .env is in .gitignore
   cat .gitignore | grep .env
   ```

2. **Use app-specific passwords** for Zoho Mail, not your main password

3. **Rotate secrets regularly** (every 90 days recommended)

4. **Set proper file permissions**
   ```bash
   chmod 600 .env
   chown harmonia:harmonia .env
   ```

---

## Part 8: Testing

### Step 8.1: Test Application Health

```bash
# From server
curl http://localhost:8000/api/health

# From outside (after Nginx is configured)
curl https://yourdomain.com/api/health
```

### Step 8.2: Test Email Functionality

```bash
# Check email service logs
docker-compose logs -f | grep "Email"

# Test welcome email through the API
curl -X POST https://yourdomain.com/api/test-email \
  -H "Content-Type: application/json" \
  -d '{"email": "your-test-email@example.com"}'
```

### Step 8.3: Test Gemini API

```bash
# Check Gemini API is working
docker-compose logs -f | grep "Gemini"

# You should see messages like:
# ✅ Gemini 3 Pro initialized
```

### Step 8.4: Test Complete Workflow

1. Open your browser and navigate to `https://yourdomain.com`
2. Create a test profile
3. Upload a test image
4. Generate a compatibility report
5. Check if email was received

### Step 8.5: Monitor Logs

```bash
# Application logs
docker-compose logs -f

# Nginx logs
sudo tail -f /var/log/nginx/harmonia_access.log
sudo tail -f /var/log/nginx/harmonia_error.log

# System logs
sudo journalctl -u harmonia -f
```

---

## Part 9: Monitoring & Maintenance

### Daily Monitoring

```bash
# Check container status
docker ps

# Check disk space
df -h

# Check memory usage
free -h

# Check logs for errors
docker-compose logs --tail=100 | grep -i error
```

### Weekly Tasks

1. **Review Logs**
   ```bash
   sudo journalctl -u harmonia --since "7 days ago" | grep -i error
   ```

2. **Check SSL Certificate** (if using Let's Encrypt)
   ```bash
   sudo certbot certificates
   ```

3. **Update Docker Images**
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

### Monthly Tasks

1. **System Updates**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Backup Data**
   ```bash
   # Backup uploads and reports
   tar -czf backup-$(date +%Y%m%d).tar.gz \
       uploads/ \
       harmonia_outputs/ \
       data/

   # Upload to remote storage (recommended)
   ```

3. **Review Analytics**
   - Check Cloudflare Analytics
   - Review application logs
   - Monitor error rates

### Automated Monitoring (Recommended)

**Install Monitoring Tools:**
```bash
# Install htop for system monitoring
sudo apt install -y htop

# Install netdata for real-time monitoring
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

**Set up Email Alerts:**
```bash
# Install monit
sudo apt install -y monit

# Configure monit
sudo nano /etc/monit/monitrc
```

---

## Troubleshooting

### Issue: Docker containers won't start

**Solution:**
```bash
# Check logs
docker-compose logs

# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Issue: Can't connect to domain

**Check:**
1. DNS propagation: `dig yourdomain.com`
2. Firewall: `sudo ufw status`
3. Nginx: `sudo nginx -t && sudo systemctl status nginx`

**Solution:**
```bash
# Check if Nginx is listening
sudo netstat -tulpn | grep :80
sudo netstat -tulpn | grep :443

# Restart Nginx
sudo systemctl restart nginx
```

### Issue: Email not sending

**Check:**
1. SMTP credentials in `.env`
2. Zoho app-specific password (not main password!)
3. DNS records (MX, SPF, DKIM)

**Test:**
```bash
# Test SMTP connection
docker-compose exec harmonia python -c "
from services.email_service import EmailService
service = EmailService()
print('Enabled:', service.enabled)
"
```

### Issue: Gemini API errors

**Check:**
1. API key is valid
2. API key has proper permissions
3. Not hitting rate limits

**Solution:**
```bash
# Check environment variable
docker-compose exec harmonia env | grep GEMINI_API_KEY

# Restart with fresh key
nano .env  # Update GEMINI_API_KEY
docker-compose restart
```

### Issue: High memory usage

**Solution:**
```bash
# Check memory
free -h

# Reduce Docker workers
nano .env  # Set WORKERS=2
docker-compose restart

# Clean up Docker
docker system prune -a
```

### Issue: SSL/TLS errors

**If using Cloudflare:**
- Set SSL mode to "Full" (not "Full strict")

**If using Let's Encrypt:**
```bash
# Renew certificates
sudo certbot renew

# Check certificate expiry
sudo certbot certificates
```

---

## Quick Commands Reference

```bash
# Start application
docker-compose up -d

# Stop application
docker-compose down

# Restart application
docker-compose restart

# View logs
docker-compose logs -f

# Update application
git pull
docker-compose build
docker-compose up -d

# Backup data
tar -czf backup-$(date +%Y%m%d).tar.gz uploads/ harmonia_outputs/

# Check disk space
df -h

# Check memory
free -h

# Restart Nginx
sudo systemctl restart nginx

# Check all services
sudo systemctl status harmonia nginx docker
```

---

## Support

If you encounter issues:

1. Check logs: `docker-compose logs -f`
2. Review this guide
3. Check GitHub Issues
4. Contact support

**Important Files:**
- Application: `/opt/harmonia/`
- Logs: `/opt/harmonia/logs/`
- Nginx Config: `/etc/nginx/sites-available/harmonia`
- Environment: `/opt/harmonia/.env`
- Systemd Service: `/etc/systemd/system/harmonia.service`

---

## Next Steps

After successful deployment:

1. ✅ Test all functionality
2. ✅ Set up automated backups
3. ✅ Configure monitoring
4. ✅ Set up staging environment
5. ✅ Document custom configurations
6. ✅ Create update procedures
7. ✅ Set up error tracking (e.g., Sentry)

**Congratulations! Your Harmonia instance is now deployed! 🎉**
