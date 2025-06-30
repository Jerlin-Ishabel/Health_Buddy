from fpdf import FPDF
import datetime
import os

def generate_pdf(symptoms: str, diagnosis: str, language: str) -> str:
    try:
        pdf = FPDF()
        pdf.add_page()

        # 🧾 Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "🩺 HealthBuddy – AI Diagnosis Report", ln=True, align='C')

        # 🕒 Date & Language
        pdf.set_font("Arial", '', 12)
        pdf.ln(10)
        pdf.cell(200, 10, f"Date: {datetime.date.today()}", ln=True)
        pdf.cell(200, 10, f"Language: {language}", ln=True)

        # 📝 Symptoms Section
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "User Symptoms:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, symptoms)

        # 💡 AI Diagnosis
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "AI Diagnosis / Advice:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, diagnosis)

        # 📁 Save
        pdf_output_path = os.path.join("output", "health_report.pdf")
        os.makedirs("output", exist_ok=True)
        pdf.output(pdf_output_path)

        return pdf_output_path
    except Exception as e:
        return f"PDF generation failed: {e}"
