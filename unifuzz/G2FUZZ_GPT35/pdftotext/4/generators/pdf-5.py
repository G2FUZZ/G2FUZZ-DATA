from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfform

# Create a PDF file with interactive form fields
def create_pdf_with_form(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)

    c.drawString(100, 750, "Please fill out the form below:")
    c.drawString(100, 700, "Name:")
    c.drawString(100, 675, "Email:")
    c.drawString(100, 650, "Phone:")

    c.save()

    # Add interactive form fields
    c = Canvas(file_path)
    c.drawString(100, 600, "Name:")
    c.drawString(100, 575, "Email:")
    c.drawString(100, 550, "Phone:")
    
    c.acroForm.textfield(name='name', tooltip='Enter your name', x=200, y=600, borderStyle='solid')
    c.acroForm.textfield(name='email', tooltip='Enter your email', x=200, y=575, borderStyle='solid')
    c.acroForm.textfield(name='phone', tooltip='Enter your phone number', x=200, y=550, borderStyle='solid')

    c.save()

# Generate PDF file with interactive form fields
file_path = "./tmp/interactive_form.pdf"
create_pdf_with_form(file_path)
print(f"PDF file with interactive form fields generated at: {file_path}")