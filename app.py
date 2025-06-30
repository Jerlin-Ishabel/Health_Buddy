import streamlit as st
from utils.gemini_api import get_health_advice
from utils.translator import translate_text
from utils.voice_utils import get_voice_input, speak_text
from utils.pdf_generator import generate_pdf
import base64

# ✅ MUST BE FIRST
st.set_page_config(
    page_title="HealthBuddy - AI Symptom Checker",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://healthbuddy-support.example.com",
        "Report a Bug": "https://github.com/yourrepo/issues",
        "About": "### HealthBuddy\nAI-powered symptom checker built with OpenAI and Streamlit."
    }
)

# ✅ Logo (AFTER set_page_config)
st.image("assets/logo.png", width=100)

# 🌙 Dark Mode toggle
dark_mode = st.toggle("🌙 Dark Mode")

# ✅ Custom Styles for Light/Dark Mode and Text Area
if dark_mode:
    st.markdown("""
    <style>
    body { background-color: #0e1117; color: white; }
    .main-container { background-color: #1a1a1a; color: white; }
    textarea, .stTextArea>div>div>textarea {
        background-color: #1f1f1f !important;
        color: white !important;
        border-radius: 10px;
        border: 1px solid #555;
    }
    .stButton>button { background-color: #5dade2; color: white; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #e9f4fb;
    }
    .main-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .stTextArea>div>div>textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.6em 1.5em;
        border-radius: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #125b8b;
        color: #fff;
    }
    h1 { color: #1f77b4; }
    h3 { color: #0c4c6c; }
    .emoji { font-size: 20px; margin-right: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 💖 Header
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("## 🩺 HealthBuddy")
st.markdown("### 🤖 Your AI-Powered Multilingual Symptom Checker")
st.markdown("Describe your symptoms in any language 🌍")

# 🌍 Language choice
language = st.selectbox("🌐 Choose your language", [
    "English", "Tamil", "Hindi", "Telugu", "Kannada",
    "Malayalam", "Marathi", "Gujarati", "Bengali", "Urdu"
])

# 🎙️ Input method
input_method = st.radio("🛠️ Select Input Method", ["Type", "Speak"])

# 💡 Examples
example = st.selectbox("💡 Try an example", [
    "I have a headache and blurred vision",
    "Chest pain after climbing stairs",
    "Dry cough with fever",
    "Stomach ache after eating spicy food",
    "Sore throat and fatigue"
])
use_example = st.checkbox("✅ Use this example")

# 📝 Input area
symptoms = ""
translated_response = ""

if use_example:
    symptoms = example
else:
    if input_method == "Speak":
        st.info("🎤 Click below to record your symptoms.")
        if st.button("🎙️ Start Voice Input"):
            symptoms = get_voice_input()
            st.write("📝 **Transcribed Symptoms:**", symptoms)
    else:
        symptoms = st.text_area("📝 Type your symptoms below", placeholder="e.g. I have a sore throat and slight fever...")

# 🔍 Get Diagnosis
if st.button("🔍 Get Diagnosis"):
    if not symptoms.strip():
        st.warning("⚠️ Please provide your symptoms first.")
    else:
        st.info("🧠 AI is analyzing your symptoms...")
        response_en = get_health_advice(symptoms)
        translated_response = translate_text(response_en, language)
        st.markdown("### ✅ AI Suggests:")
        st.success(f"💬 **({language})**:\n\n{translated_response}")

# 🔊 Speak Result
if translated_response and st.button("🔊 Speak Out the Diagnosis"):
    speak_text(translated_response, language)

# 📝 Download PDF
if translated_response and st.button("📝 Download Report as PDF"):
    pdf_path = generate_pdf(symptoms, translated_response, language)
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        href = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="HealthBuddy_Report.pdf">📥 Click here to download</a>'
        st.markdown(href, unsafe_allow_html=True)

# ✨ Footer
st.markdown("---")
st.markdown("Made with ❤️ using OpenAI + Streamlit")
st.markdown('</div>', unsafe_allow_html=True)
