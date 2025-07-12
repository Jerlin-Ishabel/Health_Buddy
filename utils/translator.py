from deep_translator import GoogleTranslator
from googletrans import Translator

# 🔄 Initialize translator once
translator = Translator()

# 🔁 English → Tamil
def translate_to_tamil(text: str) -> str:
    try:
        translated = translator.translate(text, src='en', dest='ta')
        return translated.text
    except Exception as e:
        return f"❌ Translation to Tamil failed: {str(e)}"

# 🔁 Tamil → English
def translate_to_english(text: str) -> str:
    try:
        translated = translator.translate(text, src='ta', dest='en')
        return translated.text
    except Exception as e:
        return f"❌ Translation to English failed: {str(e)}"
