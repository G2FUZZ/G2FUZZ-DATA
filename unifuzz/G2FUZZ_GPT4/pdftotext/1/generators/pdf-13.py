from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a directory to save the PDF if it doesn't already exist
import os
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# File path
file_path = directory + "page_layout_control.pdf"

# Create a PDF with specific feature description
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLines('''13. Page Layout Control: PDFs offer precise page layout control, maintaining the exact placement of text, images, and other elements, ensuring consistent formatting across different viewing environments.''')
    c.drawText(text)
    c.save()

create_pdf(file_path)