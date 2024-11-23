from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# PDF file path
pdf_path = "./tmp/metadata_included_pdf.pdf"

# Create a PDF with ReportLab
c = canvas.Canvas(pdf_path, pagesize=letter)

# Add some content
c.drawString(100, 750, "Hello, this PDF includes metadata!")

# Define metadata for the PDF
metadata = {
    'Title': 'Metadata Example',
    'Author': 'Python Script',
    'Subject': 'Demonstrating PDF Metadata',
    'Keywords': 'PDF, Python, Metadata'
}

# Adding metadata to the PDF
c.setAuthor(metadata['Author'])
c.setTitle(metadata['Title'])
c.setSubject(metadata['Subject'])
c.setKeywords(metadata['Keywords'])

# Save the PDF
c.save()

print("PDF with metadata has been created at './tmp/metadata_included_pdf.pdf'")