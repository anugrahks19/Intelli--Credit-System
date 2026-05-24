import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_groq():
    api_key = os.getenv("GROQ_API_KEY")
    print(f"Testing Groq with key: {api_key[:5]}...")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": "say hi"}]
    }
    resp = requests.post(url, json=payload, timeout=15)
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")

if __name__ == "__main__":
    test_groq()
