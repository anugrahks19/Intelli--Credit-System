import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_openrouter():
    api_key = os.getenv("OPENROUTER_API_KEY")
    print(f"Testing OpenRouter with key: {api_key[:5]}...")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "google/gemini-flash-1.5",
        "messages": [{"role": "user", "content": "say hi"}]
    }
    resp = requests.post(url, json=payload, timeout=20)
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")

if __name__ == "__main__":
    test_openrouter()
