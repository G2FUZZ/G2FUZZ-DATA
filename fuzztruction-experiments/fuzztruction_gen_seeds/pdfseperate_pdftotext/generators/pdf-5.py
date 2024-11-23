import PyPDF2
from PyPDF2 import PdfWriter, PdfReader

# Create a simple PDF using PyPDF2
writer = PdfWriter()

# Specify the page size for the blank page (A4 size in this example)
page_width = 595  # A4 width in points
page_height = 842  # A4 height in points
writer.add_blank_page(width=page_width, height=page_height)

temp_pdf_path = './tmp/simple_pdf.pdf'
with open(temp_pdf_path, 'wb') as f_out:
    writer.write(f_out)

# Open the newly created PDF to apply security features
reader = PdfReader(temp_pdf_path)
writer = PdfWriter()

# Copy pages from the original PDF to the writer
for page in reader.pages:
    writer.add_page(page)

# Set the security settings
user_password = 'user'
owner_password = 'owner'
writer.encrypt(user_pwd=user_password, owner_pwd=owner_password, use_128bit=True)

secure_pdf_path = './tmp/secure_pdf.pdf'
with open(secure_pdf_path, 'wb') as f_out:
    writer.write(f_out)

print(f'Secure PDF created at: {secure_pdf_path}')