import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")  # Make sure to define this in your .env file

# Gemini Flash API Endpoint
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

def get_health_advice(symptoms: str) -> str:
    if not symptoms.strip():
        return "❗ Please describe your symptoms."

    prompt = f"""
    You are HealthBuddy, a kind and friendly virtual health assistant.
    A person reports: "{symptoms}"

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
            return result['candidates'][0]['content']['parts'][0]['text'].strip()

        elif response.status_code == 403:
            return "🚫 Access Denied: Your API key may be invalid or missing permissions."
        elif response.status_code == 401:
            return "🔐 Unauthorized: Check your API key in the .env file."
        else:
            return f"❌ Gemini API Error {response.status_code}:\n{response.text}"

    except Exception as e:
        return f"⚠️ Exception while calling Gemini API:\n{str(e)}"
