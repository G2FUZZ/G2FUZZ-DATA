from reportlab.pdfgen import canvas
import os

def create_pdf(path):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "Hello, I am a PDF.")
    c.drawString(100, 730, "This document is digitally signed.")
    c.save()

# Paths
input_pdf_path = "./tmp/unsigned_document.pdf"

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create the PDF
create_pdf(input_pdf_path)

print("PDF created successfully without signing.")