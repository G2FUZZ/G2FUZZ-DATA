from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a PDF with ReportLab
pdf_path = os.path.join(output_dir, "document_with_redaction.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)
c.drawString(100, 750, "Page 1: Introduction")
c.drawString(100, 730, "Sensitive Data: 12345")
c.showPage()
c.drawString(100, 750, "Page 2: Table of Contents")
c.showPage()
c.drawString(100, 750, "Page 3: Chapter 1")
c.showPage()
c.drawString(100, 750, "Page 4: Conclusion")
c.save()

# Function to add bookmarks and apply redaction
def add_bookmarks_and_redact(input_pdf_path, output_pdf_path):
    # Create a PdfReader object
    input_pdf = PdfReader(open(input_pdf_path, "rb"))

    # Create a PdfWriter object for the output PDF
    output_pdf = PdfWriter()

    # Add pages from the input PDF to the output PDF
    for i, page in enumerate(input_pdf.pages):
        output_pdf.add_page(page)

    # Manually draw a black rectangle over the sensitive data on the first page using ReportLab
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.setFillColorRGB(0, 0, 0)  # Set the fill color to black
    c.rect(100, 720, 100, 20, fill=1)  # Draw the rectangle (x, y, width, height)
    c.showPage()
    c.save()

    # Note: This approach does not remove the sensitive text from the PDF's data.
    # It only visually covers it in the rendered output.

# Add bookmarks and redaction to the PDF
add_bookmarks_and_redact(pdf_path, os.path.join(output_dir, "document_with_redaction_final.pdf"))