
import requests
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.2",
    "prompt": "Test",
    "stream": False
}

print(f"Testing {url} with model 'llama3.2'...")
try:
    response = requests.post(url, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

# Also list models to be sure
print("\nListing models...")
try:
    r = requests.get("http://localhost:11434/api/tags")
    print(json.dumps(r.json(), indent=2))
except Exception as e:
    print(f"Error listing models: {e}")
