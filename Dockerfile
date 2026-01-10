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

# Copy and setup entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Expose port (Railway provides PORT env var)
EXPOSE 8000

# Use entrypoint script for reliable PORT handling
ENTRYPOINT ["/docker-entrypoint.sh"]
