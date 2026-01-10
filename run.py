#!/usr/bin/env python3
"""Railway startup script with proper PORT handling."""
import os
import sys

if __name__ == "__main__":
    port = os.environ.get("PORT", "8000")
    print(f"🚀 Starting Harmonia on port {port}")

    # Start uvicorn
    os.execvp("uvicorn", [
        "uvicorn",
        "main:app",
        "--host", "0.0.0.0",
        "--port", port,
        "--workers", "1",
        "--timeout-keep-alive", "120"
    ])
