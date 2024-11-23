from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform

# Create a PDF file with an interactive form
def create_pdf_with_form(file_path):
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, "Please fill out the form below:")
    
    c.drawString(100, 700, "Name:")
    c.rect(x=200, y=700, width=200, height=20)
    
    c.drawString(100, 650, "Email:")
    c.rect(x=200, y=650, width=200, height=20)
    
    c.drawString(100, 600, "Comments:")
    c.rect(x=200, y=600, width=200, height=100)
    
    # Create text fields using pdfform
    form = c.acroForm
    form.textfield(name='name', tooltip='Enter your name here', x=200, y=700, width=200, height=20)
    form.textfield(name='email', tooltip='Enter your email here', x=200, y=650, width=200, height=20)
    form.textfield(name='comments', tooltip='Enter your comments here', x=200, y=600, width=200, height=100)
    
    c.save()

# Generate a PDF file with an interactive form
file_path = './tmp/interactive_form.pdf'
create_pdf_with_form(file_path)