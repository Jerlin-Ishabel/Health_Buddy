import os
import uuid
import re
import time
from gtts import gTTS
import tempfile

from utils.env_utils import is_streamlit_cloud

# 🎤 Voice Input (Disabled on Streamlit Cloud)
def get_voice_input(language="English"):
    if is_streamlit_cloud():
        return "❌ Voice input is not supported on Streamlit Cloud. Please use text input."
    
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙 Listening... (up to 10 seconds)")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("✅ Recognizing...")

            lang_code = "ta-IN" if language == "Tamil" else "en-IN"
            text = recognizer.recognize_google(audio, language=lang_code)
            return text.strip()
    except Exception as e:
        return f"❗ Voice input error: {str(e)}"

# 🔊 Speak the Answer using gTTS
def speak_answer(text, language="English"):
    try:
        clean_text = clean_for_speech(text)
        lang_code = "ta" if language == "Tamil" else "en"

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts = gTTS(text=clean_text, lang=lang_code)
            tts.save(tmp_file.name)
            return tmp_file.name, None  # ✅ mp3 path + success
    except Exception as e:
        return None, f"❌ Text-to-speech error: {str(e)}"

# 🧼 Clean markdown/symbols
def clean_for_speech(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)   # remove bold
    text = re.sub(r"__([^_]+)__", r"\1", text)     # remove underline
    text = re.sub(r"[_*#>\[\]()~`]", "", text)     # remove markdown
    text = re.sub(r"\s+", " ", text)               # normalize spacing
    return text.strip()
