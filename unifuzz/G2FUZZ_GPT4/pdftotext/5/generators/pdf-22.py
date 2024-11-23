import os
from PyPDF2 import PdfWriter, PdfReader
import endesive
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

def file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")

def create_standardized_pdf_with_article_threads(output_path):
    """Create a simple PDF file with standardized format and article threads"""
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    Story = []
    
    # Define some content to demonstrate article threads
    for i in range(1, 5):
        text = f'This is paragraph {i} in the document. It demonstrates how we might use article threads in a PDF document.'
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(PageBreak())  # Simulate multi-page for article threads
    
    doc.build(Story)

# Create a standardized PDF file with Article Threads
standard_pdf_path = './tmp/standard_format_with_article_threads.pdf'
os.makedirs(os.path.dirname(standard_pdf_path), exist_ok=True)  # Ensure the directory exists
create_standardized_pdf_with_article_threads(standard_pdf_path)

# Encrypt the PDF file
reader = PdfReader(standard_pdf_path)
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
writer.encrypt(user_pwd="userpassword", owner_pwd="ownerownerpassword")
encrypted_pdf_path = './tmp/encrypted_signed_with_article_threads.pdf'
with open(encrypted_pdf_path, 'wb') as f_out:
    writer.write(f_out)

# Now, sign the encrypted PDF
def sign_pdf(input_pdf, output_pdf, cert_file, key_file, password):
    # Check if the files exist
    file_exists(cert_file)
    file_exists(key_file)
    file_exists(input_pdf)

    dct = {
        "sigflags": 3,
        "sigpage": 0,
        "sigbutton": True,
        "contact": "email@example.com",
        "location": "Location",
        "signingdate": b"20200101000000Z",
        "reason": "Digital Signature",
        "password": password,
    }
    with open(cert_file, "rb") as cf, open(key_file, "rb") as kf, open(input_pdf, "rb") as pf:
        certs = (cf.read(), )
        key = kf.read()
        datau = pf.read()
    datas = endesive.pdf.cms.sign(datau, dct, key, certs, [], 'sha256')
    with open(output_pdf, "wb") as fp:
        fp.write(datau)
        fp.write(datas)

cert_file_path = './path_to_your_certificate.pem'
key_file_path = './path_to_your_private_key.key'
password = 'your_key_password'

# Ensure the paths are correct and the files exist before proceeding
try:
    sign_pdf(encrypted_pdf_path, './tmp/encrypted_signed_final_with_article_threads.pdf', cert_file_path, key_file_path, password)
    print("PDF with Article Threads has been encrypted and signed.")
except FileNotFoundError as e:
    print(e)