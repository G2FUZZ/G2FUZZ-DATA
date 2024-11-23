from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfReader, PdfWriter  # Correct import statement
import io
import os

# Create a temporary directory to store files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Create an example file to embed
embedded_file_path = os.path.join(tmp_dir, 'example.txt')
with open(embedded_file_path, 'w') as f:
    f.write("This is an example file to be embedded into a PDF.")

# Define the path for the compressed PDF
pdf_path = os.path.join(tmp_dir, 'example_pdf.pdf')
compressed_pdf_path = os.path.join(tmp_dir, 'compressed_example_pdf.pdf')

# Create a simple PDF with ReportLab
c = canvas.Canvas(pdf_path, pagesize=A4)
c.drawString(100, 750, "This is a PDF containing an embedded file.")
c.drawString(100, 730, "It includes advanced compression techniques.")
c.save()

# Function to apply compression and embed a file
def compress_and_embed_pdf(input_pdf_path, output_pdf_path, embedded_file_path):
    # First, read the PDF we just created
    existing_pdf = PdfReader(input_pdf_path)  # Corrected to use PdfReader directly

    num_pages = len(existing_pdf.pages)  # Correct method to get the number of pages

    # Prepare to write to a new PDF with compression options
    output_pdf = PdfWriter()

    # Copy existing PDF pages to the new PDF
    for i in range(num_pages):
        page = existing_pdf.pages[i]  # Correct method to get a page
        output_pdf.add_page(page)  # Correct method name to add a page

    # Prepare the file to be embedded
    with open(embedded_file_path, "rb") as ef:
        ef_data = ef.read()

    # Add the embedded file
    output_pdf.add_attachment("example.txt", ef_data)  # Correct method name to add an attachment

    # Finally, write the output PDF with the embedded file
    with open(output_pdf_path, "wb") as out_f:
        output_pdf.write(out_f)

# Apply compression and embed the file
compress_and_embed_pdf(pdf_path, compressed_pdf_path, embedded_file_path)

print(f"Compressed PDF with an embedded file has been created at {compressed_pdf_path}")