from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import re

# 📄 Generate PDF in English Only
def generate_pdf(name, age, gender, symptoms, diagnosis, quote="Stay healthy!"):
    if not os.path.exists("output"):
        os.makedirs("output")

    filename = f"output/HealthBuddy_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    title_font = "Helvetica-Bold"
    body_font = "Helvetica"

    # 🧾 Title
    c.setFont(title_font, 18)
    c.drawString(50, height - 50, "HealthBuddy AI Diagnosis Report")

    # 📅 Date & Language
    c.setFont(body_font, 11)
    c.drawString(50, height - 80, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, height - 100, "Language: English")

    # 👤 Personal Details
    c.setFont(title_font, 13)
    c.drawString(50, height - 130, "Patient Details:")
    c.setFont(body_font, 11)
    c.drawString(60, height - 150, f"Name   : {name}")
    c.drawString(60, height - 165, f"Age    : {age}")
    c.drawString(60, height - 180, f"Gender : {gender}")

    # 🤒 Symptoms
    y = height - 210
    c.setFont(title_font, 13)
    c.drawString(50, y, "Reported Symptoms:")
    y -= 20
    c.setFont(body_font, 11)
    for line in wrap_text(symptoms, 85):
        c.drawString(60, y, line)
        y -= 15

    # 💡 Diagnosis
    y -= 10
    c.setFont(title_font, 13)
    c.drawString(50, y, "AI Diagnosis & Advice:")
    y -= 20
    c.setFont(body_font, 11)

    for point in split_into_points(diagnosis):
        for line in wrap_text(point, 85):
            if y < 80:
                c.showPage()
                y = height - 50
                c.setFont(body_font, 11)
            c.drawString(60, y, line)
            y -= 15
        y -= 5

    # 💬 Health Quote
    y -= 20
    c.setFont(title_font, 13)
    c.drawString(50, y, "💬 HealthBuddy Says:")
    y -= 20
    c.setFont("Helvetica-Oblique", 11)
    for line in wrap_text(f"“{quote}”", 85):
        c.drawString(60, y, line)
        y -= 15

    c.save()
    return filename

# 🧼 Word wrapping
def wrap_text(text, max_chars):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line + word) <= max_chars:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    if line:
        lines.append(line.strip())
    return lines

# 📌 Point splitting
def split_into_points(text):
    clean_text = re.sub(r"\*\*(.*?)\*\*", r"\1", text.strip())
    return [pt.strip() for pt in re.split(r'(?:\n+)|(?:\d+\.\s+)|(?:-\s+)', clean_text) if pt.strip()]
