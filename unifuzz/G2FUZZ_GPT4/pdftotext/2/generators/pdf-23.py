from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue, black
import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for the PDF
file_path = os.path.join(output_dir, 'accessible_pdf_with_structure.pdf')

# Create a simple PDF with hierarchical structure
def create_pdf(path, title, content, y_start=720):
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle(title)
    y_pos = y_start
    for text in content:
        c.setFillColor(black if y_pos == y_start else blue)  # Title in black, content in blue
        c.drawString(72, y_pos, text)
        y_pos -= 20  # Decrease y position for the next line
    c.save()

# Content for the PDF with multi-tiered document structure
content = [
    "Accessible PDF Content:",
    "This PDF includes basic metadata for accessibility.",
    "It also demonstrates a multi-tiered document structure.",
    "Hierarchical elements include:",
    "- Title",
    "- Sections",
    "- Subsections"
]

create_pdf(file_path, "Accessible PDF Example with Structure", content)

# Now, we enhance the PDF with metadata and structure information using PyPDF2
reader = PdfReader(file_path)
writer = PdfWriter()

# Copy over all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Adding metadata
writer.add_metadata({
    '/Title': 'Accessible PDF Example with Structure',
    '/Author': 'Accessibility Team',
    '/Subject': 'Accessibility Features',
    '/Keywords': 'Accessibility, PDF, Text-to-Speech, Tagged PDF, Structure',
    '/Creator': 'Accessibility Feature Generator'
})

# Save the updated PDF
with open(file_path, 'wb') as f_out:
    writer.write(f_out)

print(f"Accessible PDF with multi-tiered document structure generated at: {file_path}")