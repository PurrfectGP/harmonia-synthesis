#!/bin/bash
# Railway start script with proper PORT handling

# Use Railway's PORT or default to 8000
PORT=${PORT:-8000}

echo "Starting uvicorn on port $PORT"
uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1 --timeout-keep-alive 120
