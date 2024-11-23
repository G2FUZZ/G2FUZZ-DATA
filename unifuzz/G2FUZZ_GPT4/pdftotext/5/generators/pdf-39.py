from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
from PyPDF2 import PdfReader, PdfWriter  # Updated import here

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the PDF file
pdf_path = os.path.join(output_dir, "text_and_fonts.pdf")
extracted_page_path = os.path.join(output_dir, "extracted_page.pdf")

# Create a canvas
c = canvas.Canvas(pdf_path, pagesize=letter)

# Set the font to Helvetica, size 12
c.setFont("Helvetica", 12)

# Add some text
text = "Hello, world! This is a PDF with embedded text in Helvetica font."
c.drawString(72, 728, text)

# Save the PDF
c.save()

# Page Extraction feature
def extract_page(pdf_path, page_number, output_path):
    """
    Extract a page from a PDF and save it as a separate PDF file.
    :param pdf_path: Path to the original PDF file.
    :param page_number: The page number to extract (0-based index).
    :param output_path: Path to save the extracted page as a PDF.
    """
    with open(pdf_path, "rb") as file:  # Use context manager for file handling
        reader = PdfReader(file)
        writer = PdfWriter()
        
        # Ensure the page number is valid
        if page_number < 0 or page_number >= len(reader.pages):
            raise ValueError("Invalid page number.")
        
        writer.add_page(reader.pages[page_number])
        
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)

# Extract the first page as an example
extract_page(pdf_path, 0, extracted_page_path)

print(f"PDF file has been created at {pdf_path}")
print(f"Extracted page has been created at {extracted_page_path}")