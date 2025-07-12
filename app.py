import streamlit as st
import base64
import random

from utils.voice_utils import get_voice_input, speak_answer
from utils.translator import translate_to_english, translate_to_tamil
from utils.pdf_generator import generate_pdf
from gemini_api import get_health_advice  # Gemini API handler

# -------------------------------
# 🎨 Page Setup and Styling
# -------------------------------
st.set_page_config(page_title="HealthBuddy - Symptom Checker", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #F5F5F5;
    }
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        border-radius: 8px;
    }
    .stTextInput>div>input {
        background-color: #2b2b2b;
        color: white;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏥 Header
# -------------------------------
try:
    st.image("assets/logo.png", width=100)
except:
    st.warning("⚠️ Logo not found! Add your logo to 'assets/logo.png'")

st.title("🩺 HealthBuddy")
st.markdown("#### Your Friendly AI Symptom Checker")

# -------------------------------
# ⬅️ Sidebar for Language & Input Method
# -------------------------------
with st.sidebar:
    lang = st.selectbox("🌍 Select Language", ["English", "Tamil"])
    input_method = st.radio("🎙 Choose Input Method", ["📝 Type", "🎤 Speak"])

# -------------------------------
# 👤 User Details
# -------------------------------
st.markdown("### 👤 Your Details")
name = st.text_input("Name")
age = st.text_input("Age")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# -------------------------------
# 🤒 Symptom Input Area
# -------------------------------
st.markdown("### 🤒 How are you feeling today?")
user_input = ""

# 🧠 Diagnosis Function
def run_diagnosis(name, age, gender, user_input, lang):
    try:
        st.info("🧠 AI is analyzing your symptoms...")
        symptoms_en = translate_to_english(user_input) if lang == "Tamil" else user_input
        ai_response_en = get_health_advice(symptoms_en)

        if not ai_response_en.strip():
            st.error("⚠️ Diagnosis failed: Empty response from AI.")
            return

        final_response = translate_to_tamil(ai_response_en) if lang == "Tamil" else ai_response_en

        st.markdown("### ✅ AI Suggests:")
        st.success(f"💬 **({lang})**:\n\n{final_response}")

        st.session_state["name"] = name
        st.session_state["age"] = age
        st.session_state["gender"] = gender
        st.session_state["symptoms"] = user_input
        st.session_state["response_en"] = ai_response_en
        st.session_state["response_lang"] = final_response
        st.session_state["lang"] = lang

        st.session_state["quote"] = random.choice([
            "🩺 Health is not valued till sickness comes. – Thomas Fuller",
            "🍏 Take care of your body. It’s the only place you have to live. – Jim Rohn",
            "🧘 A healthy outside starts from the inside. – Robert Urich",
            "🥗 To keep the body in good health is a duty… otherwise we shall not be able to keep our mind strong and clear. – Buddha",
            "💪 Your body deserves the best. Treat it with care and kindness.",
            "🏃‍♀️ Every step you take towards health matters. Keep moving forward!",
            "🌿 Healing is a matter of time, but it is sometimes also a matter of opportunity. – Hippocrates"
        ])
    except Exception as e:
        st.error(f"❌ Error during diagnosis: {str(e)}")

# -------------------------------
# 💬 Text or 🎤 Voice Input
# -------------------------------
if input_method == "📝 Type":
    user_input = st.text_input("Enter your symptom")
    if st.button("🔍 Get Diagnosis"):
        if not name.strip() or not age.strip() or not user_input.strip():
            st.warning("⚠️ Please fill name, age, and symptoms.")
        else:
            run_diagnosis(name, age, gender, user_input, lang)

elif input_method == "🎤 Speak":
    if st.button("🎙 Start Voice Input"):
        spoken_input = get_voice_input(lang)
        if spoken_input.strip() and not spoken_input.startswith("❗"):
            st.success(f"🎧 You said: {spoken_input}")
            if not name.strip() or not age.strip():
                st.warning("⚠️ Please fill name and age.")
            else:
                run_diagnosis(name, age, gender, spoken_input, lang)
        else:
            st.warning(spoken_input or "❗ Voice input failed.")

# -------------------------------
# 💡 Example Symptoms
# -------------------------------
with st.expander("💡 See Example Symptoms"):
    st.markdown("""
    - I have a sore throat and fever  
    - I'm feeling very tired and dizzy  
    - My chest hurts when I breathe  
    - I have rashes on my arms  
    - My joints feel swollen and painful  
    - I'm coughing a lot and feel weak  
    - My stomach is hurting and I feel nauseous  
    - I can't sleep and feel anxious  
    - I feel pain in my lower back  
    - My head is pounding and I feel sensitive to light  
    - I have a runny nose and sneezing frequently  
    - My eyes are red and itchy  
    - I feel a burning sensation while urinating  
    - I’m experiencing shortness of breath  
    - I have muscle cramps and fatigue  
    - My skin feels itchy and dry  
    - I'm feeling unusually cold and shivering  
    - I feel lightheaded after standing up  
    - I have sudden mood swings and irritability  
    - I feel pressure in my ears and can't hear properly
    """)

# -------------------------------
# 🔊 Speak Diagnosis
# -------------------------------
if "response_lang" in st.session_state and st.button("🔊 Speak Out the Diagnosis"):
    speak_answer(st.session_state["response_lang"], st.session_state["lang"])

# -------------------------------
# 📥 Download PDF (English Only)
# -------------------------------
if "response_en" in st.session_state:
    if st.session_state["lang"] == "English":
        if st.button("📥 Download Report as PDF"):
            pdf_path = generate_pdf(
                name=st.session_state["name"],
                age=st.session_state["age"],
                gender=st.session_state["gender"],
                symptoms=st.session_state["symptoms"],
                diagnosis=st.session_state["response_en"]
            )
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                href = f'''
                    <a href="data:application/octet-stream;base64,{base64_pdf}"
                       download="HealthBuddy_Report.pdf">
                       📄 Click here to download your PDF
                    </a>
                '''
                st.markdown(href, unsafe_allow_html=True)
    else:
        st.info("📄 PDF report is available only in English language.")

# -------------------------------
# 💬 HealthBuddy Quote
# -------------------------------
if "quote" in st.session_state:
    st.markdown("### 💬 HealthBuddy Says:")
    st.info(st.session_state["quote"])

# -------------------------------
# 👣 Footer
# -------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; font-size: 0.9em; color: gray'>
Made with ❤️ by Jerlin Ishabel | HealthBuddy 2025
</p>
""", unsafe_allow_html=True)
