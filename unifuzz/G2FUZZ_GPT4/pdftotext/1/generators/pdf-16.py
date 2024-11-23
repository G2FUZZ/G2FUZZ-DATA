from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for the PDF to be saved
file_path = os.path.join(output_dir, "enhanced_accessible_pdf.pdf")

# Create a PDF with ReportLab
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF Example")

# Add some content
c.drawString(72, 720, "Accessibility in PDFs")
c.drawString(72, 700, "This document demonstrates features for enhancing accessibility.")
# This is a simplistic way to add content. For real applications, consider using more structured layouts.

# Adding Metadata Storage feature
metadata = {
    'Title': 'Accessible PDF Example',
    'Author': 'Your Name',
    'Subject': 'Demonstration of Accessibility Features in PDFs',
    'Keywords': 'PDF, Accessibility, ReportLab, Python',
    'Creator': 'Your Application Name',
    'Producer': 'Your Company Name',
    'CreationDate': datetime.now(),
    'ModDate': datetime.now()  # for demonstration; typically, this would be set at the time of actual modification
}

c.setAuthor(metadata['Author'])
c.setTitle(metadata['Title'])
c.setSubject(metadata['Subject'])
c.setKeywords(metadata['Keywords'])
c.setCreator(metadata['Creator'])
# Note: ReportLab directly supports setting some metadata fields, but not all (like Producer, CreationDate, ModDate directly)

c.showPage()
c.save()

print(f"PDF with Metadata Storage feature created at: {file_path}")

# Note: While this approach adds basic metadata, creating fully accessible PDF/UA compliant documents may require additional steps or tools.