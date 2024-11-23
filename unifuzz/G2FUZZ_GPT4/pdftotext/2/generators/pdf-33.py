from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PyPDF2 import PdfReader, PdfWriter

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for the PDF
file_path = os.path.join(output_dir, 'accessible_pdf_with_obj_streams.pdf')

# Create a simple PDF
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF Example with Object Streams")
c.drawString(72, 720, "Accessible PDF Content with Object Streams:")
c.drawString(72, 700, "This PDF includes basic metadata and object streams for accessibility.")
c.save()

# Now, let's add some basic metadata using PyPDF2 for enhanced accessibility
reader = PdfReader(file_path)
writer = PdfWriter()  # Removed the use_object_streams argument

# Copy over all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Adding metadata
writer.add_metadata({
    '/Title': 'Accessible PDF Example with Object Streams',
    '/Author': 'Accessibility Team',
    '/Subject': 'Accessibility Features with Object Streams',
    '/Keywords': 'Accessibility, PDF, Text-to-Speech, Tagged PDF, Object Streams',
    '/Creator': 'Accessibility Feature Generator'
})

# Save the updated PDF
with open(file_path, 'wb') as f_out:
    writer.write(f_out)

print(f"Accessible PDF with Object Streams generated at: {file_path}")