from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter  # Correct imports for PyPDF2 version 3.0.0 or later
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a PDF with ReportLab
pdf_path = os.path.join(output_dir, "document_with_bookmarks.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)
c.drawString(100, 750, "Page 1: Introduction")
c.showPage()
c.drawString(100, 750, "Page 2: Table of Contents")
c.showPage()
c.drawString(100, 750, "Page 3: Chapter 1")
c.showPage()
c.drawString(100, 750, "Page 4: Conclusion")
c.save()

# Function to add bookmarks (outline items) to the PDF
def add_bookmarks(input_pdf_path, output_pdf_path):
    # Create a PdfReader object
    input_pdf = PdfReader(open(input_pdf_path, "rb"))

    # Create a PdfWriter object for the output PDF
    output_pdf = PdfWriter()

    # Add pages from the input PDF to the output PDF
    for page in input_pdf.pages:
        output_pdf.add_page(page)

    # Add bookmarks (outline items)
    output_pdf.add_outline_item("Introduction", 0)  # Adding an outline item to the first page
    output_pdf.add_outline_item("Table of Contents", 1)  # Second page
    output_pdf.add_outline_item("Chapter 1", 2)  # Third page
    output_pdf.add_outline_item("Conclusion", 3)  # Fourth page

    # Write the output PDF with bookmarks (outline items)
    with open(output_pdf_path, "wb") as output_file:
        output_pdf.write(output_file)

# Add bookmarks to the PDF
add_bookmarks(pdf_path, os.path.join(output_dir, "document_with_bookmarks_final.pdf"))