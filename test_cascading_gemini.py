import os
import requests
import logging
from dotenv import load_dotenv

# Mocking the gateway behavior
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_cascading_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    gemini_models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp", "gemini-pro"]
    
    print("\n--- Testing Gemini Cascading Logic ---")
    for model in gemini_models:
        print(f"\nTrying model: {model}...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": "say hi"}]}]}
        try:
            resp = requests.post(url, json=payload, timeout=15)
            if resp.status_code == 200:
                print(f"✅ SUCCESS with {model}!")
                print(f"Response: {resp.json()['candidates'][0]['content']['parts'][0]['text']}")
                break
            else:
                print(f"❌ FAILED with {model}: {resp.status_code}")
                # print(f"Error: {resp.text}")
        except Exception as e:
            print(f"⚠️ Exception with {model}: {e}")
    else:
        print("\n🚨 ALL GEMINI MODELS FAILED.")

if __name__ == "__main__":
    test_cascading_gemini()
