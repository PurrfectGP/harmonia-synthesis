# Cloudflare Setup Guide for Harmonia

Complete guide to configure Cloudflare for optimal performance, security, and reliability.

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [DNS Configuration](#dns-configuration)
3. [SSL/TLS Settings](#ssltls-settings)
4. [Security Settings](#security-settings)
5. [Performance Optimization](#performance-optimization)
6. [Analytics & Monitoring](#analytics--monitoring)
7. [Advanced Configuration](#advanced-configuration)

---

## Initial Setup

### Step 1: Add Your Domain

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Click **"Add a Site"**
3. Enter your domain name (e.g., `yourdomain.com`)
4. Select the **Free plan** (perfect for getting started!)
5. Click **"Continue"**

### Step 2: Review DNS Records

Cloudflare will automatically scan and import your existing DNS records.

**Review imported records:**
- Verify all records are correct
- Note any records that weren't imported
- Keep a backup of your original DNS settings

### Step 3: Update Nameservers

Cloudflare will provide two nameservers:
```
Example:
bob.ns.cloudflare.com
jane.ns.cloudflare.com
```

**Update at your domain registrar:**
1. Go to your domain registrar's website
2. Find DNS/Nameserver settings
3. Replace existing nameservers with Cloudflare's nameservers
4. Save changes

**Verification:**
- Wait 5-60 minutes for propagation
- Cloudflare will email you when domain is active
- You can check status in Cloudflare dashboard

---

## DNS Configuration

### Required DNS Records

Add these records in **DNS** section:

#### 1. Main Domain (A Record)
```
Type: A
Name: @
IPv4 address: YOUR_CONTABO_SERVER_IP
Proxy status: Proxied (Orange Cloud ☁️ ON)
TTL: Auto
```

#### 2. WWW Subdomain (A Record)
```
Type: A
Name: www
IPv4 address: YOUR_CONTABO_SERVER_IP
Proxy status: Proxied (Orange Cloud ☁️ ON)
TTL: Auto
```

#### 3. Email Records (For Zoho Mail)

**MX Records:**
```
Type: MX
Name: @
Mail server: mx.zoho.com
Priority: 10
TTL: Auto

Type: MX
Name: @
Mail server: mx2.zoho.com
Priority: 20
TTL: Auto

Type: MX
Name: @
Mail server: mx3.zoho.com
Priority: 50
TTL: Auto
```

**SPF Record:**
```
Type: TXT
Name: @
Content: v=spf1 include:zoho.com ~all
TTL: Auto
```

**DKIM Record** (get from Zoho dashboard):
```
Type: TXT
Name: zoho._domainkey
Content: v=DKIM1; k=rsa; p=YOUR_DKIM_KEY_FROM_ZOHO
TTL: Auto
```

**DMARC Record:**
```
Type: TXT
Name: _dmarc
Content: v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
TTL: Auto
```

**Zoho Verification TXT:**
```
Type: TXT
Name: @
Content: zoho-verification=zb123456789.zmverify.zoho.com
TTL: Auto
```

### Proxy Status Explained

**Proxied (Orange Cloud ☁️):**
- Traffic goes through Cloudflare
- DDoS protection enabled
- CDN caching enabled
- Your server IP is hidden
- **Use for:** Web traffic (A, AAAA, CNAME records)

**DNS Only (Gray Cloud ☁️):**
- Direct connection to your server
- No Cloudflare protection
- Your server IP is visible
- **Use for:** Email (MX), FTP, SSH, or when you need direct access

---

## SSL/TLS Settings

### Step 1: Choose SSL/TLS Encryption Mode

Go to **SSL/TLS** → **Overview**

**Select: Full (strict)** ⭐ Recommended

Encryption modes explained:
- **Off**: No encryption (never use!)
- **Flexible**: Cloudflare ↔ User encrypted, Cloudflare ↔ Server unencrypted
- **Full**: End-to-end encryption, accepts self-signed certs
- **Full (strict)**: End-to-end encryption, requires valid cert ⭐

### Step 2: Enable Edge Certificates

Go to **SSL/TLS** → **Edge Certificates**

Enable these settings:

✅ **Always Use HTTPS**
- Automatically redirects HTTP to HTTPS

✅ **HTTP Strict Transport Security (HSTS)**
- Settings:
  - Max Age: 6 months
  - Include subdomains: Yes
  - Preload: No (unless you're sure!)

✅ **Minimum TLS Version: 1.2**
- Disables older, insecure protocols

✅ **Opportunistic Encryption**
- Enables HTTP/2 server push

✅ **TLS 1.3**
- Faster, more secure protocol

✅ **Automatic HTTPS Rewrites**
- Fixes mixed content issues

### Step 3: Origin Server Certificate (Optional but Recommended)

Go to **SSL/TLS** → **Origin Server**

1. Click **"Create Certificate"**
2. Choose:
   - Private key type: RSA (2048)
   - Hostnames: `yourdomain.com, *.yourdomain.com`
   - Certificate validity: 15 years
3. Click **"Create"**
4. **Save both certificate and private key** (you'll need these!)

**Install on your server:**
```bash
# Create certificate directory
sudo mkdir -p /etc/ssl/cloudflare

# Save certificate
sudo nano /etc/ssl/cloudflare/cert.pem
# Paste the certificate

# Save private key
sudo nano /etc/ssl/cloudflare/key.pem
# Paste the private key

# Set permissions
sudo chmod 600 /etc/ssl/cloudflare/key.pem
sudo chmod 644 /etc/ssl/cloudflare/cert.pem
```

**Update Nginx config:**
```nginx
ssl_certificate /etc/ssl/cloudflare/cert.pem;
ssl_certificate_key /etc/ssl/cloudflare/key.pem;
```

---

## Security Settings

### Step 1: Security Level

Go to **Security** → **Settings**

**Set to: Medium** (recommended for most sites)

Security levels:
- **Essentially Off**: Minimal security
- **Low**: Challenges only most threatening
- **Medium**: Challenges moderately threatening ⭐
- **High**: Challenges all but most trusted visitors
- **I'm Under Attack**: Maximum security mode

### Step 2: WAF (Web Application Firewall)

Go to **Security** → **WAF**

**Enable Managed Rules:**

Free plan includes:
- Cloudflare Managed Ruleset
- Cloudflare OWASP Core Ruleset

**Bot Fight Mode:**
- Enable "Bot Fight Mode" (free plan)
- Helps prevent bot attacks

### Step 3: Rate Limiting (Pro plan and above)

If you have Pro plan or higher:

Create rule:
```
If:
  - Incoming requests match: (http.request.uri.path contains "/api/")
Then:
  - Limit to: 60 requests per minute
```

### Step 4: Firewall Rules (Free Plan Limited)

Go to **Security** → **WAF** → **Custom rules**

**Example rule - Block bad bots:**
```
Expression: (cf.bot_management.score lt 30)
Action: Block
```

**Example rule - Geo-blocking (optional):**
```
Expression: (ip.geoip.country in {"XX" "YY"})
Action: Block
```

### Step 5: DDoS Protection

Go to **Security** → **DDoS**

**Settings:**
- DDoS Protection: On (automatic, always enabled)
- HTTP DDoS Attack Protection: On
- Network-layer DDoS Attack Protection: On

No configuration needed - Cloudflare handles this automatically!

---

## Performance Optimization

### Step 1: Speed Settings

Go to **Speed** → **Optimization**

**Auto Minify:**
✅ JavaScript
✅ CSS
✅ HTML

**Brotli:**
✅ Enable (better compression than gzip)

**Early Hints:**
✅ Enable (faster page loads)

**Rocket Loader:**
⚠️ Test before enabling (can break some sites)

**HTTP/2:**
✅ Enabled by default

**HTTP/3 (with QUIC):**
✅ Enable (faster, more reliable)

### Step 2: Caching

Go to **Caching** → **Configuration**

**Caching Level:**
- Set to: **Standard** ⭐

**Browser Cache TTL:**
- Set to: **4 hours** or **Respect Existing Headers** ⭐

**Always Online:**
✅ Enable
- Serves cached version if your server is down

**Development Mode:**
- Use this when testing (disables caching for 3 hours)

### Step 3: Page Rules (Free: 3 rules)

Go to **Rules** → **Page Rules**

**Rule 1: Cache Everything for Static Assets**
```
URL: yourdomain.com/static/*
Settings:
  - Cache Level: Cache Everything
  - Edge Cache TTL: 1 month
  - Browser Cache TTL: 1 month
```

**Rule 2: Bypass Cache for API**
```
URL: yourdomain.com/api/*
Settings:
  - Cache Level: Bypass
```

**Rule 3: Redirect WWW to non-WWW (or vice versa)**
```
URL: www.yourdomain.com/*
Settings:
  - Forwarding URL: 301 Redirect
  - Destination: https://yourdomain.com/$1
```

### Step 4: Argo Smart Routing (Paid Feature)

If you have a paid plan:
- Enable Argo for 30% faster load times
- Cost: $5/month + $0.10/GB

---

## Analytics & Monitoring

### Step 1: Web Analytics

Go to **Analytics & Logs** → **Web Analytics**

View:
- Traffic over time
- Requests by country
- Top pages
- Bandwidth usage
- Security threats blocked

### Step 2: Security Analytics

Go to **Security** → **Analytics**

Monitor:
- Threats blocked
- Attack types
- Bot traffic
- Rate limiting

### Step 3: Performance Insights

Go to **Speed** → **Performance**

Check:
- Core Web Vitals
- Load time by location
- Cache hit rate
- Bandwidth saved

### Step 4: Email Alerts

Go to **Notifications**

Set up alerts for:
- DDoS attacks
- SSL certificate expiration
- High error rates
- Traffic spikes

---

## Advanced Configuration

### Custom Error Pages

Go to **Custom Pages**

Customize:
- 500 errors (Server Error)
- 1000 errors (DNS resolution error)
- Always Online page

### Workers (Advanced)

Go to **Workers & Pages**

Use Workers for:
- Custom logic at edge
- A/B testing
- Personalization
- API modifications

### Load Balancing (Pro plan and above)

Go to **Traffic** → **Load Balancing**

Set up for:
- High availability
- Geographic routing
- Failover

### Transform Rules

Go to **Rules** → **Transform Rules**

**HTTP Request Header Modification:**
Add custom headers:
```
Add:
  X-Forwarded-Proto: https
  X-Real-IP: $client_ip
```

---

## API Configuration

### Get Your API Credentials

1. Go to **My Profile** → **API Tokens**
2. Create token with permissions:
   - Zone:Zone:Read
   - Zone:DNS:Edit
   - Zone:Analytics:Read

**Save these:**
- Zone ID: Found on Overview page
- API Token: From token creation

**Add to .env:**
```bash
CLOUDFLARE_ENABLED=true
CLOUDFLARE_ZONE_ID=your-zone-id-here
CLOUDFLARE_API_TOKEN=your-api-token-here
```

---

## Testing Your Setup

### 1. Test DNS Propagation

```bash
# Check from multiple locations
dig yourdomain.com
dig www.yourdomain.com

# Check MX records
dig MX yourdomain.com

# Check TXT records (SPF, DKIM)
dig TXT yourdomain.com
```

### 2. Test SSL/TLS

```bash
# Test HTTPS
curl -I https://yourdomain.com

# Check SSL grade
# Visit: https://www.ssllabs.com/ssltest/
```

### 3. Test Performance

Tools:
- [GTmetrix](https://gtmetrix.com/)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [WebPageTest](https://www.webpagetest.org/)

### 4. Test Security

- [Security Headers](https://securityheaders.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)

### 5. Test Email

```bash
# Test SPF
dig TXT yourdomain.com

# Test DKIM
dig TXT zoho._domainkey.yourdomain.com

# Send test email via your app
```

---

## Troubleshooting

### Issue: Site not loading

**Check:**
1. DNS records point to correct IP
2. Orange cloud is enabled
3. Firewall rules aren't blocking traffic

**Solution:**
```bash
# Check DNS
dig yourdomain.com

# Temporarily disable Cloudflare proxy (gray cloud)
# If it works, issue is with Cloudflare config
```

### Issue: SSL errors

**Check:**
1. SSL mode is set to "Full" or "Full (strict)"
2. Your server has valid SSL certificate
3. Port 443 is open on your server

**Solution:**
- Change SSL mode to "Full" (not "Full strict")
- Verify server SSL certificate

### Issue: Email not working

**Check:**
1. MX records are correct
2. MX records are **not** proxied (gray cloud)
3. SPF, DKIM, DMARC records are correct

**Solution:**
```bash
# Verify MX records
dig MX yourdomain.com

# MX records should show Zoho servers
```

### Issue: Slow performance

**Check:**
1. Caching is enabled
2. Minification is on
3. Compression is enabled

**Solution:**
- Enable Argo (paid feature)
- Check page rules
- Review cache analytics

---

## Best Practices

1. ✅ **Always use orange cloud** for web traffic
2. ✅ **Use gray cloud** for email (MX) records
3. ✅ **Enable HSTS** after testing
4. ✅ **Set up alerts** for security events
5. ✅ **Review analytics** regularly
6. ✅ **Keep API tokens** secure
7. ✅ **Test changes** in development mode
8. ✅ **Document custom** rules and settings

---

## Quick Reference

### Essential URLs
- Dashboard: https://dash.cloudflare.com/
- API Docs: https://developers.cloudflare.com/api/
- Community: https://community.cloudflare.com/
- Status: https://www.cloudflarestatus.com/

### Support
- Free plan: Community forums
- Paid plans: Email support
- Enterprise: 24/7 phone support

---

## Security Checklist

- [ ] SSL/TLS mode set to "Full (strict)"
- [ ] HSTS enabled
- [ ] TLS 1.3 enabled
- [ ] Bot Fight Mode enabled
- [ ] Security level: Medium or higher
- [ ] WAF managed rules enabled
- [ ] DDoS protection active
- [ ] Firewall rules configured
- [ ] Rate limiting set up (if available)
- [ ] Email alerts configured

## Performance Checklist

- [ ] Auto Minify enabled (JS, CSS, HTML)
- [ ] Brotli compression enabled
- [ ] HTTP/3 enabled
- [ ] Caching configured
- [ ] Page rules optimized
- [ ] Always Online enabled
- [ ] Early Hints enabled
- [ ] CDN properly configured

**Your Cloudflare setup is complete! 🎉**
