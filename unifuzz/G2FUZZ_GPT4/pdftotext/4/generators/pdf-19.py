from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PyPDF2 import PdfWriter, PdfReader
from datetime import datetime

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to add version control text to a document
def add_version_control(c, version):
    version_text = f"Version: {version}, Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    c.drawString(100, 720, version_text)

# Create a simple PDF file with version control
def create_secured_pdf_with_version_control(output_dir, version):
    pdf_path = output_dir + 'secured_document.pdf'
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "This is a secure document.")
    
    # Add version control text
    add_version_control(c, version)
    
    c.save()

    # Encrypt the PDF file
    password = "password"
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Add all pages to the writer and encrypt
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    # Save the encrypted PDF
    encrypted_pdf_path = output_dir + f'encrypted_document_v{version}.pdf'
    with open(encrypted_pdf_path, 'wb') as f_out:
        writer.write(f_out)

    print(f"Encrypted PDF with version control has been saved to: {encrypted_pdf_path}")

# Example usage
version = "1.0"  # Version of the document
create_secured_pdf_with_version_control(output_dir, version)