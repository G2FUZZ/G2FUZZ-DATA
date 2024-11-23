from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path
file_path = os.path.join(output_dir, 'accessible_pdf.pdf')

# Create a PDF with reportlab
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF Example")

# Adding some text
text = "Accessibility Features: PDFs support accessibility features such as text-to-speech and the ability to reflow text, making documents more accessible to users with disabilities."
c.drawString(72, 720, text)  # Starting at x=72, y=720

# Save the PDF
c.showPage()
c.save()

print(f'PDF with basic accessibility features created at {file_path}')