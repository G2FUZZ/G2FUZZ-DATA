from PyPDF2 import PdfWriter, PdfReader
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Text content to add to the PDF
content = """
7. Security Features: PDF files offer various security features, including password protection, encryption, digital signatures, and rights management, helping to protect sensitive information and verify document authenticity.
"""

# File paths
output_file_path = os.path.join(output_dir, 'secured_pdf.pdf')

# Create a PDF file with the text content
writer = PdfWriter()

# Specify the page size when adding a blank page
page_width, page_height = letter
writer.add_blank_page(width=page_width, height=page_height)

packet = io.BytesIO()
# Create a new PDF with ReportLab
c = canvas.Canvas(packet, pagesize=letter)
text = c.beginText(40, page_height - 40)
text.setFont("Helvetica", 10)
text.textLines(content)
c.drawText(text)
c.save()

# Move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfReader(packet)
writer.add_page(new_pdf.pages[0])

# Encrypt the PDF file with a password
password = "securepassword"
writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

# Save the PDF file
with open(output_file_path, 'wb') as f_out:
    writer.write(f_out)

print(f"PDF created and saved with encryption at {output_file_path}. Password is '{password}'.")