
import requests
import sys

def check_ollama():
    try:
        # Check if Ollama is running
        print("Checking Ollama connection...")
        response = requests.get("http://localhost:11434/")
        if response.status_code == 200:
            print("✅ Ollama is online.")
        else:
            print(f"❌ Ollama returned status code: {response.status_code}")
            return False

        # Check for model
        required_model = "llama3.2:3b"
        print(f"Checking for model: {required_model}...")
        
        # List local models
        models_resp = requests.get("http://localhost:11434/api/tags")
        if models_resp.status_code == 200:
            models = models_resp.json().get('models', [])
            model_names = [m['name'] for m in models]
            
            # Flexible matching (e.g. 'llama3.2:latest' matches 'llama3.2')
            found = any(required_model in m for m in model_names)
            
            if found:
                print(f"✅ Model '{required_model}' found.")
                return True
            else:
                print(f"❌ Model '{required_model}' NOT found.")
                print(f"   Available models: {model_names}")
                print(f"   Run 'ollama pull {required_model}' to fix this.")
                return False
        else:
            print("❌ Failed to list models.")
            return False

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. Is it running? (Try 'ollama serve')")
        return False
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False

if __name__ == "__main__":
    if check_ollama():
        sys.exit(0)
    else:
        sys.exit(1)
