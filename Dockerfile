# Harmonia - Production Dockerfile for Contabo Deployment
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production
RUN pip install --no-cache-dir gunicorn uvicorn[standard]

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data uploads harmonia_outputs logs

# Create non-root user for security
RUN useradd -m -u 1000 harmonia && \
    chown -R harmonia:harmonia /app

# Switch to non-root user
USER harmonia

# Expose port (Railway provides PORT env var)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8000}/api/health || exit 1

# Use shell form to allow environment variable substitution
CMD gunicorn main:app \
     --workers 1 \
     --worker-class uvicorn.workers.UvicornWorker \
     --bind 0.0.0.0:${PORT:-8000} \
     --timeout 180 \
     --keep-alive 120 \
     --access-logfile - \
     --error-logfile - \
     --log-level info
