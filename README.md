# 🩺 HealthBuddy - AI Symptom Checker

**HealthBuddy** is a Streamlit-based AI-powered web application designed to help users identify possible health conditions based on their symptoms. With support for **English and Tamil**, the app allows users to enter or speak symptoms and receive personalized AI-generated advice.

This smart assistant uses **Google Gemini API** for diagnosis, integrates **voice input/output**, and provides downloadable **PDF and audio reports**, offering a friendly and informative experience.

---

## 🎯 Project Objectives

✅ **Multilingual Support**: Accept and respond in **English** and **Tamil**.

✅ **Smart AI Diagnosis**: Analyze user symptoms and generate meaningful suggestions using **Gemini API**.

✅ **Voice Features**: Enable voice input using speech recognition and speak diagnosis using gTTS.

✅ **Interactive Web UI**: Clean, intuitive design using Streamlit.

✅ **PDF & Audio Reports**: Download personalized reports as PDF or MP3.

✅ **Study Examples & Quotes**: Display example symptom queries and motivational health quotes.

---

## ❗ Problem Statement

People often experience symptoms but hesitate or forget to consult professionals promptly. There is a need for an easy-to-use, multilingual tool to provide preliminary health suggestions and encourage health awareness.

---

## 💡 Proposed Solution

**HealthBuddy** empowers users to self-check their symptoms through a simple interface. It helps by:

- Translating and analyzing input symptoms
- Giving AI-generated suggestions (not medical diagnosis)
- Encouraging healthy habits via quotes and personalized tips
- Supporting both **voice and text interaction**
- Generating downloadable reports for record-keeping

---

## 🔄 Workflow of the Project

1. 📥 **Symptom Input**
   - Text or voice input in English or Tamil
   - Translated automatically to English if needed

2. 🧠 **Diagnosis via Gemini**
   - Uses `gemini-1.5` to understand and provide suggestions

3. 🔊 **Voice Output**
   - Speaks the diagnosis using gTTS and pygame

4. 📄 **Report Generation**
   - PDF report with name, age, gender, symptoms, and AI response
   - Optional MP3 download of the diagnosis

5. 🌐 **Streamlit App Interface**
   - Clean sidebar for input selection
   - Expanders for example symptoms and health quotes

---

## 🔗 Live Demo

[🌐 Launch HealthBuddy](https://healthbuddy-kqpnrbno68rj6vfw8no2iq.streamlit.app/)

---

## 📁 Dataset & API

- No fixed dataset (real-time input from users)
- Uses **Google Gemini API** for diagnosis
- Translation via **Deep Translator**
- Voice via **SpeechRecognition + gTTS**

---

## 🧰 Tech Stack & Tools

| Tool / Library       | Purpose                             |
|----------------------|-------------------------------------|
| Python               | Main programming language           |
| Streamlit            | Web app frontend                    |
| Google Gemini API    | AI-powered symptom analysis         |
| Deep Translator      | English↔Tamil translation           |
| SpeechRecognition    | Voice input                         |
| gTTS + pygame        | Voice output (TTS)                  |
| ReportLab            | PDF report generation               |
| base64, os, time     | File handling & encoding            |

---

## 🔊 Input & Output Details

- **Input Methods**:
  - Text input box
  - Voice input via mic (SpeechRecognition)

- **Output**:
  - AI response in user's chosen language
  - Optional voice playback (gTTS)
  - PDF download of result
  - MP3 download of spoken diagnosis

---

## 📌 Response Labels

This app does not return numeric labels but rather **natural language explanations and suggestions** such as:

- "You may be experiencing seasonal flu..."
- "If you feel breathless with chest pain, consult a doctor immediately."

---

## 📌 Conclusion
HealthBuddy bridges the gap between everyday symptoms and smart insights using AI + voice tech + multilingual support. It encourages timely self-checks and spreads awareness about health in an accessible way.



