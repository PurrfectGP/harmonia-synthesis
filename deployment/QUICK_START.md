# Harmonia - Quick Start Guide

Fast deployment guide for experienced users. For detailed instructions, see [DEPLOYMENT.md](../DEPLOYMENT.md).

## Prerequisites

- Contabo VPS (4GB+ RAM)
- Domain on Cloudflare
- Zoho Mail account
- Gemini API key

## 1. Server Setup (10 minutes)

```bash
# SSH into server
ssh root@your-server-ip

# Install Docker
curl -fsSL https://get.docker.com | sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Nginx
sudo apt update && sudo apt install -y nginx git

# Configure firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
```

## 2. Clone Application (2 minutes)

```bash
# Create directory
sudo mkdir -p /opt/harmonia
cd /opt/harmonia

# Clone repository
git clone https://github.com/yourusername/harmonia-synthesis.git .
```

## 3. Configure Environment (5 minutes)

```bash
# Copy example
cp .env.example .env

# Edit variables
nano .env
```

**Required variables:**
```bash
GEMINI_API_KEY=your-gemini-key
DOMAIN=yourdomain.com
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your-zoho-app-password
```

## 4. Configure Cloudflare (10 minutes)

1. Add domain to Cloudflare
2. Update nameservers at registrar
3. Add DNS records:
   ```
   A    @    YOUR_SERVER_IP    Proxied
   A    www  YOUR_SERVER_IP    Proxied
   ```
4. Set SSL/TLS to "Full"
5. Enable "Always Use HTTPS"

## 5. Configure Zoho Mail (15 minutes)

1. Add domain to Zoho Mail
2. Add MX records in Cloudflare:
   ```
   MX  @  mx.zoho.com  10
   MX  @  mx2.zoho.com 20
   MX  @  mx3.zoho.com 50
   ```
3. Add SPF record:
   ```
   TXT  @  v=spf1 include:zoho.com ~all
   ```
4. Create `noreply@yourdomain.com` account
5. Generate app-specific password

## 6. Deploy Application (5 minutes)

```bash
# Build and start
docker-compose build
docker-compose up -d

# Check logs
docker-compose logs -f
```

## 7. Configure Nginx (5 minutes)

```bash
# Copy config
sudo cp deployment/nginx.conf /etc/nginx/sites-available/harmonia

# Edit domain
sudo nano /etc/nginx/sites-available/harmonia
# Replace "yourdomain.com" with your domain

# Enable site
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/harmonia /etc/nginx/sites-enabled/

# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

## 8. Test (5 minutes)

```bash
# Test health endpoint
curl https://yourdomain.com/api/health

# Check logs
docker-compose logs -f | grep -i error

# Test email (optional)
docker-compose exec harmonia python -c "
from services.email_service import EmailService
s = EmailService()
print('Email enabled:', s.enabled)
"
```

## 9. Set Up Auto-Start (2 minutes)

```bash
# Copy service file
sudo cp deployment/harmonia.service /etc/systemd/system/

# Enable service
sudo systemctl daemon-reload
sudo systemctl enable harmonia
sudo systemctl start harmonia
```

## Verification Checklist

- [ ] Domain resolves to Cloudflare
- [ ] HTTPS works (green padlock)
- [ ] API health check returns 200
- [ ] Docker containers running
- [ ] Nginx running without errors
- [ ] Email service enabled
- [ ] Logs show no critical errors

## Common Issues

**Can't connect to domain:**
```bash
# Check DNS
dig yourdomain.com

# Check firewall
sudo ufw status

# Check Nginx
sudo nginx -t && sudo systemctl status nginx
```

**Email not working:**
- Use app-specific password (not main password)
- Verify MX records: `dig MX yourdomain.com`
- Check SMTP settings in `.env`

**Docker errors:**
```bash
# Rebuild
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Maintenance Commands

```bash
# View logs
docker-compose logs -f

# Restart application
docker-compose restart

# Update application
git pull
docker-compose build
docker-compose up -d

# Backup data
tar -czf backup-$(date +%Y%m%d).tar.gz uploads/ harmonia_outputs/

# Check disk space
df -h

# Update system
sudo apt update && sudo apt upgrade -y
```

## Environment Variables Quick Reference

```bash
# Required
GEMINI_API_KEY=          # From https://aistudio.google.com/apikey
DOMAIN=                  # Your domain
SMTP_USER=               # Zoho email
SMTP_PASSWORD=           # Zoho app password

# Optional but recommended
GEMINI_MODEL=gemini-3-pro-preview
EMAIL_ENABLED=true
CLOUDFLARE_ENABLED=true
```

## Next Steps

1. Review full [DEPLOYMENT.md](../DEPLOYMENT.md) for details
2. Set up monitoring
3. Configure backups
4. Test all features
5. Set up staging environment

## Support

- Full Docs: [DEPLOYMENT.md](../DEPLOYMENT.md)
- Cloudflare Guide: [CLOUDFLARE_SETUP.md](./CLOUDFLARE_SETUP.md)
- GitHub Issues: [Issues](https://github.com/yourusername/harmonia-synthesis/issues)

**Total Setup Time: ~1 hour** ⏱️

**You're ready to go! 🚀**
