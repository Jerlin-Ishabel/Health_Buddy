import speech_recognition as sr
from gtts import gTTS
import pygame
import uuid
import os
import time
import re

# 🎤 Voice Input (supports English & Tamil)
def get_voice_input(language="English"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("🎙 Listening... (up to 10 seconds)")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("✅ Recognizing...")

            lang_code = "ta-IN" if language == "Tamil" else "en-IN"
            text = recognizer.recognize_google(audio, language=lang_code)
            return text.strip()

        except sr.WaitTimeoutError:
            return "❗ Listening timed out. Try again."
        except sr.UnknownValueError:
            return "❗ Could not understand your voice."
        except sr.RequestError:
            return "❗ Speech recognition service failed."
        except Exception as e:
            return f"❗ Voice input error: {str(e)}"

# 🔊 Speak the Answer using gTTS and pygame
def speak_answer(text, language="English"):
    try:
        clean_text = clean_for_speech(text)
        lang_code = "ta" if language == "Tamil" else "en"

        os.makedirs("output", exist_ok=True)
        filename = f"output/speak_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=clean_text, lang=lang_code)
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(filename)

    except Exception as e:
        print(f"❌ Text-to-speech error: {str(e)}")
        if language == "Tamil":
            print("🔁 Retrying with English TTS...")
            speak_answer(text, language="English")

# 🧼 Clean text for speaking (removes Markdown/symbols)
def clean_for_speech(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)   # remove bold
    text = re.sub(r"__([^_]+)__", r"\1", text)     # remove underline
    text = re.sub(r"[_*#>\[\]()~`]", "", text)     # remove markdown/special
    text = re.sub(r"\s+", " ", text)               # normalize spacing
    return text.strip()
