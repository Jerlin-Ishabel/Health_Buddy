import streamlit as st  # ✅ Correct: from turtle import st ❌ was wrong
import speech_recognition as sr
from gtts import gTTS
import tempfile
import playsound

# 🎙️ Supported languages for speech
gtts_lang_map = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Urdu": "ur"
}

# 🎤 Get user's voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "❗Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "❗Could not request results; check your internet."

# 🔊 Convert text to speech and play
def speak_text(text, lang="English"):
    lang_code = gtts_lang_map.get(lang, "en")
    try:
        tts = gTTS(text=text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound.playsound(fp.name)
    except Exception as e:
        st.error(f"Speech error: {e}")
