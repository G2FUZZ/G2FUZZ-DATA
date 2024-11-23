from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io
import os

# Create a temporary directory to store files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Create an example file to embed
embedded_file_path = os.path.join(tmp_dir, 'example.txt')
with open(embedded_file_path, 'w') as f:
    f.write("This is an example file to be embedded into a PDF.")

# Create a simple PDF with ReportLab
pdf_path = os.path.join(tmp_dir, 'example_pdf.pdf')
c = canvas.Canvas(pdf_path)
c.drawString(100, 750, "This is a PDF containing an embedded file.")
# Include a marker for repurposable content
c.drawString(100, 730, "Repurposable Content: Enabled")
c.save()

# Embed a file into the PDF
output_pdf_path = os.path.join(tmp_dir, 'pdf_with_embedded_file.pdf')

# First, read the PDF we just created
existing_pdf = PdfReader(pdf_path)
num_pages = len(existing_pdf.pages)

# Prepare to write to a new PDF
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

# Add custom metadata to indicate the presence of repurposable content
output_pdf.add_metadata({
    '/Custom': 'Repurposable Content Enabled'
})

# Finally, write the output PDF with the embedded file
with open(output_pdf_path, "wb") as out_f:
    output_pdf.write(out_f)

print(f"PDF with an embedded file and repurposable content has been created at {output_pdf_path}")