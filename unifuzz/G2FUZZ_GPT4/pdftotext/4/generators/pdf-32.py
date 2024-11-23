from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfReader, PdfWriter
import io
import os
from datetime import datetime

# Create a temporary directory to store files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)  # Corrected line here

# Create an example file to embed
embedded_file_path = os.path.join(tmp_dir, 'example.txt')
with open(embedded_file_path, 'w') as f:
    f.write("This is an example file to be embedded into a PDF.")

# Define the path for the PDF with time stamp
pdf_with_timestamp_path = os.path.join(tmp_dir, 'pdf_with_timestamp.pdf')
compressed_pdf_with_timestamp_path = os.path.join(tmp_dir, 'compressed_pdf_with_timestamp.pdf')
redacted_pdf_path = os.path.join(tmp_dir, 'redacted_pdf_with_timestamp.pdf')

# Create a simple PDF with ReportLab and include a time stamp
c = canvas.Canvas(pdf_with_timestamp_path, pagesize=A4)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time_stamp_string = f"Document created on: {current_time}"

c.drawString(100, 750, "This is a PDF containing an embedded file.")
c.drawString(100, 730, "It includes advanced compression techniques.")
c.drawString(100, 710, time_stamp_string)  # Adding time stamp to the document
# Add a placeholder for redaction (in real scenarios, redaction would require identifying and removing sensitive information)
c.setFillColorRGB(1, 0, 0)  # Set color to red for visibility
c.rect(100, 690, 200, 20, stroke=1, fill=1)
c.setFillColorRGB(0, 0, 0)  # Reset color to black
c.drawString(100, 670, "[REDACTED AREA]")  # Indicate redacted area
c.save()

# Function to apply compression, embed a file, include a time stamp, and handle redaction
def compress_embed_and_timestamp_pdf(input_pdf_path, output_pdf_path, embedded_file_path):
    # First, read the PDF we just created
    existing_pdf = PdfReader(input_pdf_path)

    num_pages = len(existing_pdf.pages)

    # Prepare to write to a new PDF with compression options
    output_pdf = PdfWriter()

    # Copy existing PDF pages to the new PDF
    for i in range(num_pages):
        page = existing_pdf.pages[i]
        output_pdf.add_page(page)

    # Prepare the file to be embedded
    with open(embedded_file_path, "rb") as ef:
        ef_data = ef.read()

    # Add the embedded file
    output_pdf.add_attachment("example.txt", ef_data)

    # Finally, write the output PDF with the embedded file, time stamp, and redacted content
    with open(output_pdf_path, "wb") as out_f:
        output_pdf.write(out_f)

# Apply compression, embed the file, include a time stamp, and handle redaction
compress_embed_and_timestamp_pdf(pdf_with_timestamp_path, redacted_pdf_path, embedded_file_path)

print(f"Redacted PDF with an embedded file and time stamp has been created at {redacted_pdf_path}")