import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Testing Gemini with key: {api_key[:5]}...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": "say hi"}]}]}
    resp = requests.post(url, json=payload, timeout=15)
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")

if __name__ == "__main__":
    test_gemini()
