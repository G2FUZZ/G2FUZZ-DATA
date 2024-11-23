from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for the PDF
file_path = os.path.join(output_dir, 'accessible_pdf.pdf')

# Create a simple PDF
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF Example")
c.drawString(72, 720, "Accessible PDF Content:")
c.drawString(72, 700, "This PDF includes basic metadata for accessibility.")
c.save()

# Now, let's add some basic metadata using PyPDF2 for enhanced accessibility
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader(file_path)
writer = PdfWriter()

# Copy over all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Adding metadata
writer.add_metadata({
    '/Title': 'Accessible PDF Example',
    '/Author': 'Accessibility Team',
    '/Subject': 'Accessibility Features',
    '/Keywords': 'Accessibility, PDF, Text-to-Speech, Tagged PDF',
    '/Creator': 'Accessibility Feature Generator'
})

# Save the updated PDF
with open(file_path, 'wb') as f_out:
    writer.write(f_out)

print(f"Accessible PDF generated at: {file_path}")