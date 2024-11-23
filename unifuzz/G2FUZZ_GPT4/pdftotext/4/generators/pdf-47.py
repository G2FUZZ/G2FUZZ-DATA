from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import qrcode
from PyPDF2 import PdfWriter, PdfReader

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to add a QR code to the PDF
def add_qr_code(pdf_path, data, x=100, y=700, size=50):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = output_dir + 'qr_code.png'
    img.save(img_path)
    
    # Add QR code image to the PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawImage(img_path, x, y, width=size, height=size)
    c.save()
    os.remove(img_path)  # Clean up the generated QR code image file

# Create a simple PDF file with a QR code
pdf_path = output_dir + 'secured_document_with_qr.pdf'
add_qr_code(pdf_path, 'https://example.com/secure-data', x=100, y=650, size=100)

# Encrypt the PDF file
password = "password"
reader = PdfReader(pdf_path)
writer = PdfWriter()

# Add all pages to the writer and encrypt
for page in reader.pages:
    writer.add_page(page)
writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

# Save the encrypted PDF
encrypted_pdf_path = output_dir + 'encrypted_document_with_qr.pdf'
with open(encrypted_pdf_path, 'wb') as f_out:
    writer.write(f_out)

print(f"Encrypted PDF with QR code has been saved to: {encrypted_pdf_path}")