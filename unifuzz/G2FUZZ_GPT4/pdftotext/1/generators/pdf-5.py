from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, white  # Import predefined colors

def create_pdf_with_form(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 750, "Interactive Form Example")
    
    # Create form fields
    form = c.acroForm
    
    # Text field
    c.drawString(50, 700, "Name:")
    form.textfield(name='name', tooltip='Name', x=110, y=685, borderStyle='inset',
                   borderColor=black, fillColor=white, width=300, height=20)
    
    # Checkboxes
    c.drawString(50, 650, "Favourite Colour:")
    form.checkbox(name='colour_blue', tooltip='Blue', x=150, y=635, buttonStyle='check',
                  borderColor=black, fillColor=white, textColor=black, forceBorder=True)
    c.drawString(160, 650, "Blue")
    form.checkbox(name='colour_red', tooltip='Red', x=220, y=635, buttonStyle='check',
                  borderColor=black, fillColor=white, textColor=black, forceBorder=True)
    c.drawString(230, 650, "Red")
    
    c.save()

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate the PDF with form
pdf_path = './tmp/interactive_form.pdf'
create_pdf_with_form(pdf_path)

print(f"PDF with interactive form created at: {pdf_path}")