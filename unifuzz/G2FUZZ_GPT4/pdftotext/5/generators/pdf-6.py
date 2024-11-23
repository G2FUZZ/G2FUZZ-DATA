from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def create_simple_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.setAuthor("Author Name")
    c.setTitle("Simple PDF Example")

    # Drawing some text for demonstration
    c.drawString(100, 750, "This text is visible.")
    c.drawString(100, 730, "This text is also visible.")

    # Add some text outside layers for reference
    c.drawString(100, 710, "This text is not on any layer and always visible.")

    c.save()

create_simple_pdf('./tmp/simple_pdf_example.pdf')