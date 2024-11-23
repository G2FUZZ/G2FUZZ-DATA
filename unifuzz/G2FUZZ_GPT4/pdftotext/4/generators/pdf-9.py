from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def add_text_to_pdf(text, filename, compression=True):
    """
    Add text to a PDF file with an option for compression.
    """
    c = canvas.Canvas(filename, pagesize=A4)
    if compression:
        c.setPageCompression(1)
    c.drawString(100, 800, text)
    c.save()

# Directory to save the PDF
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Filename for the PDF
pdf_filename = os.path.join(output_dir, 'compressed_pdf.pdf')

# Text to add to the PDF
text_content = "This PDF demonstrates efficient compression of document content."

# Generate the PDF with text compression
add_text_to_pdf(text_content, pdf_filename)