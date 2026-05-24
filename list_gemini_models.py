import os
import requests
from dotenv import load_dotenv

load_dotenv()

def list_gemini_models():
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Listing models for key: {api_key[:5]}...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    resp = requests.get(url)
    if resp.status_code == 200:
        models = resp.json().get('models', [])
        for model in models:
            print(f"- {model['name']} ({model['displayName']})")
    else:
        print(f"Error {resp.status_code}: {resp.text}")

if __name__ == "__main__":
    list_gemini_models()
