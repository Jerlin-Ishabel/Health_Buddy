import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in .env file")

API_URL ="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

def get_health_advice(symptoms: str) -> str:
    if not symptoms.strip():
        return "❗ Please describe your symptoms."

    prompt = f"""
    You are HealthBuddy, a kind and friendly virtual health assistant.
    A person reports: \"{symptoms.strip()}\"

    Provide:
    1. A simple, empathetic explanation of what this may relate to.
    2. General health tips to manage the symptoms.
    Avoid medical terms or diagnosis. Respond like you're helping a friend.
    """

    data = {
        "contents": [
            {
                "parts": [{"text": prompt.strip()}]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)

        if response.status_code == 200:
            result = response.json()
            candidates = result.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts and isinstance(parts, list):
                    return parts[0].get("text", "").strip()
                else:
                    return "⚠️ Gemini response received but empty."
            else:
                return "⚠️ No candidates found in Gemini response."

        elif response.status_code == 401:
            return "🔐 Unauthorized: Check your GEMINI_API_KEY."
        elif response.status_code == 403:
            return "🚫 Forbidden: Your API key lacks permission."
        elif response.status_code == 429:
            return "⏳ Rate limit exceeded. Try later."
        elif response.status_code == 400:
            return "❌ API key expired or bad request."
        else:
            return f"❌ Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"⚠️ Gemini API error:\n{str(e)}"
