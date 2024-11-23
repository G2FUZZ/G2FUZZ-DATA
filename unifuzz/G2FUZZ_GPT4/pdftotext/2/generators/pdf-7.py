from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
   
# Create a PDF file with ReportLab
pdf_path = os.path.join(output_dir, 'document_with_metadata.pdf')
c = canvas.Canvas(pdf_path)
c.drawString(100,750,"Hello, World!")
c.save()

# Now, use PyPDF2 to add metadata to the PDF
metadata = {
    '/Author': 'John Doe',
    '/Title': 'Sample PDF with Metadata',
    '/Subject': 'Demonstration of PDF Metadata',
    '/Keywords': 'Python, PDF, Metadata, ReportLab, PyPDF2'
}

reader = PdfReader(pdf_path)
writer = PdfWriter()

# Copy existing pages to writer
for page in reader.pages:
    writer.add_page(page)

# Add metadata
writer.add_metadata(metadata)

# Write to a new PDF file
with open(os.path.join(output_dir, 'document_with_custom_metadata.pdf'), 'wb') as f_out:
    writer.write(f_out)

# Optionally, remove the initial PDF without metadata if not needed
os.remove(pdf_path)