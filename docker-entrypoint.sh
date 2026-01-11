#!/bin/bash
set -e

# Get PORT from environment or default to 8000
PORT=${PORT:-8000}

echo "=========================================="
echo "🚀 Starting Harmonia on port $PORT"
echo "=========================================="

# Start gunicorn with the PORT
exec gunicorn main:app \
    --workers 1 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind "0.0.0.0:$PORT" \
    --timeout 180 \
    --keep-alive 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
