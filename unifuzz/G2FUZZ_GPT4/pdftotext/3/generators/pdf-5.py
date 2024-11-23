from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Step 1: Create a PDF with ReportLab
pdf_file_path = './tmp/secure_document.pdf'
c = canvas.Canvas(pdf_file_path, pagesize=letter)
c.drawString(100, 750, "5. Security Features:")
c.drawString(100, 735, "PDF files offer several security features, including")
c.drawString(100, 720, "password protection, encryption, digital signatures,")
c.drawString(100, 705, "and watermarks, to protect sensitive information and")
c.drawString(100, 690, "verify document authenticity.")
c.save()

# Step 2: Add a simple text watermark
watermark_text = "CONFIDENTIAL"
watermark_pdf_path = './tmp/watermark.pdf'
watermark_c = canvas.Canvas(watermark_pdf_path, pagesize=letter)
watermark_c.setFillAlpha(0.3)  # Make the watermark text semi-transparent
watermark_c.setFont("Helvetica", 60)
watermark_c.saveState()
watermark_c.translate(500, 100)
watermark_c.rotate(45)
watermark_c.drawString(-150, 0, watermark_text)
watermark_c.restoreState()
watermark_c.save()

# Step 3: Merge original PDF with watermark
reader_original = PdfReader(pdf_file_path)
reader_watermark = PdfReader(watermark_pdf_path)
writer = PdfWriter()

# Add watermark to all pages
for page in reader_original.pages:
    page.merge_page(reader_watermark.pages[0])
    writer.add_page(page)

# Add password protection (encryption)
password = "secret"
writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

# Save the watermarked and encrypted PDF
watermarked_encrypted_pdf_path = './tmp/secure_document_watermarked_encrypted.pdf'
with open(watermarked_encrypted_pdf_path, 'wb') as f_out:
    writer.write(f_out)

# Cleanup: Remove the intermediate files
os.remove(pdf_file_path)
os.remove(watermark_pdf_path)

print("PDF generated with watermark and encryption.")