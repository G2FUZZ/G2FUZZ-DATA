from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PyPDF2 import PdfWriter, PdfReader

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple PDF file
pdf_path = output_dir + 'secured_document.pdf'
c = canvas.Canvas(pdf_path, pagesize=letter)
c.drawString(100, 750, "This is a secure document.")
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
encrypted_pdf_path = output_dir + 'encrypted_document.pdf'
with open(encrypted_pdf_path, 'wb') as f_out:
    writer.write(f_out)

print(f"Encrypted PDF has been saved to: {encrypted_pdf_path}")