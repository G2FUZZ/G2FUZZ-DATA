from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, white  # Import predefined colors
from PyPDF2 import PdfWriter, PdfReader  # Updated import statement
import io

def create_pdf_with_form(path):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
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
    
    buffer.seek(0)
    new_pdf = PdfReader(buffer)  # Updated class name
    output = PdfWriter()  # Updated class name
    output.add_page(new_pdf.pages[0])  # Updated method name and attribute for accessing pages
    
    # PDF Portfolio feature could be implemented here by adding attachments to the PDF.
    # Note that PyPDF2 does not support adding portfolios directly as of my last update.
    # This step would normally involve using another library or tool that supports PDF Portfolios.
    # As a placeholder, the following comments indicate where this functionality would be integrated.
    # output.addAttachment('file_name.extension', file_data)
    
    with open(path, "wb") as outputStream:
        output.write(outputStream)

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate the PDF with form
pdf_path = './tmp/interactive_form_with_portfolio.pdf'
create_pdf_with_form(pdf_path)

print(f"PDF with interactive form and placeholder for PDF Portfolios feature created at: {pdf_path}")