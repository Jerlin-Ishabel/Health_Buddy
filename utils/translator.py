from deep_translator import GoogleTranslator

# 🔁 English → Tamil
def translate_to_tamil(text: str) -> str:
    try:
        return GoogleTranslator(source='auto', target='ta').translate(text)
    except Exception as e:
        return f"❌ Translation to Tamil failed: {str(e)}"

# 🔁 Tamil → English
def translate_to_english(text: str) -> str:
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        return f"❌ Translation to English failed: {str(e)}"
