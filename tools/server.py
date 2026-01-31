
import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Enable CORS (for local development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Placeholder Prompt (User to provide actual one later)
TEST_CASE_TEMPLATE = """
You are an expert QA Automation Engineer.
Your task is to generate comprehensive test cases based on the user's input description.
Output the test cases in a clear Markdown format.
Include:
- Test Case ID
- Description
- Pre-conditions
- Steps
- Expected Result
"""

# --- MODELS ---
class ChatRequest(BaseModel):
    user_query: str

class ChatResponse(BaseModel):
    response: str
    status: str

# --- ENDPOINTS ---

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    full_prompt = f"{TEST_CASE_TEMPLATE}\n\nUser Input:\n{request.user_query}"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        print(f"Sending request to Ollama ({MODEL_NAME})...")
        resp = requests.post(OLLAMA_URL, json=payload)
        
        if resp.status_code == 200:
            data = resp.json()
            generated_text = data.get("response", "")
            return ChatResponse(response=generated_text, status="success")
        else:
            print(f"Ollama Error: {resp.text}")
            raise HTTPException(status_code=500, detail=f"Ollama API Error: {resp.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Failed to connect to Ollama.")
        raise HTTPException(status_code=503, detail="Could not connect to Ollama service. Is it running?")
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Mount UI (Static Files)
# We assume the 'ui' directory is in the same folder as the parent of 'tools' or relative path
# Correct path relative to where we run the server
ui_path = os.path.join(os.getcwd(), "ui")
if os.path.exists(ui_path):
    app.mount("/", StaticFiles(directory=ui_path, html=True), name="ui")
else:
    print(f"Warning: UI directory not found at {ui_path}")

if __name__ == "__main__":
    # Ensure ui directory exists
    if not os.path.exists("ui"):
        os.makedirs("ui")
        with open("ui/index.html", "w") as f:
            f.write("<h1>Backend Running - UI not found</h1>")
            
    uvicorn.run(app, host="0.0.0.0", port=8000)
