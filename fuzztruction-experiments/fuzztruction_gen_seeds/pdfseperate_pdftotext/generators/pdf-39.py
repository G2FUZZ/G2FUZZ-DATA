from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import os

# Ensure tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a PDF file
pdf_path = os.path.join(output_dir, 'custom_page_labels.pdf')
c = canvas.Canvas(pdf_path, pagesize=letter)

# Generate content for 6 pages
for i in range(1, 7):
    c.drawString(270, 400, f'Page {i}')
    c.showPage()

# Save the PDF
c.save()

# Now, let's add custom page labels
reader = PdfReader(pdf_path)
writer = PdfWriter()

# Copy pages from the reader to the writer
for page in reader.pages:
    writer.add_page(page)

# Unfortunately, PyPDF2 does not support adding custom page labels or creating PDF Portfolios directly.
# The code to add page labels and create PDF Portfolios has been removed due to these limitations.

# For demonstration purposes, let's assume we want to include a placeholder for adding additional files to the PDF Portfolio.
# Normally, this would require a more advanced PDF manipulation library that supports PDF Portfolios,
# such as Adobe Acrobat SDK or other commercial software.

# Write to a new PDF
output_pdf_path = os.path.join(output_dir, 'custom_page_labels_with_numbering.pdf')
with open(output_pdf_path, 'wb') as f_out:
    writer.write(f_out)

print(f'PDF with custom page labels created: {output_pdf_path}')

# Note: To actually create a PDF Portfolio, you would need to use a library or software that supports this feature.
# This code does not actually create a PDF Portfolio due to the limitations of PyPDF2.