from googletrans import Translator

# Initialize the translator
translator = Translator()

# Language map
lang_code = {
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

# Translate given text to target language
def translate_text(text, target_language):
    try:
        target_code = lang_code.get(target_language, "en")
        translated = translator.translate(text, dest=target_code)
        return translated.text
    except Exception as e:
        return f"⚠️ Translation error: {str(e)}"

