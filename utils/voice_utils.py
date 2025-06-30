import streamlit as st
import speech_recognition as sr
import pyttsx3

# 🎙️ Supported languages (pyttsx3 supports mostly English-like voices locally)
lang_voice_map = {
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

# 🎤 Get user's voice input via microphone
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "❗Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "❗Could not request results; check your internet."

# 🔊 Convert text to speech (English only recommended for compatibility)
def speak_text(text, lang="English"):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed
        engine.setProperty('volume', 1.0)  # Volume
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"❌ Speech Error: {e}")
