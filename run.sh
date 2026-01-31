#!/bin/bash

# 1. Setup Environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install fastapi uvicorn requests ollama
else
    source venv/bin/activate
fi

# 2. Verify Connections
echo "🔍 Verifying Ollama..."
python3 tools/verify_ollama.py
if [ $? -ne 0 ]; then
    echo "❌ Ollama check failed."
    echo "👉 Please ensure Ollama is installed and running ('ollama serve')."
    echo "👉 Ensure the model is available: 'ollama pull llama3.2'"
    exit 1
fi

# 3. Launch
echo "🚀 Starting Test Genie..."
echo "🌍 Open http://127.0.0.1:8000 in your browser"
echo "------------------------------------------------"
python3 tools/server.py
