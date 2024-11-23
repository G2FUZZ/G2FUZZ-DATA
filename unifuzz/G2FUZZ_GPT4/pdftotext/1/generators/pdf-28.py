from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple PDF file
c = canvas.Canvas(f"{output_dir}example_with_version_control.pdf", pagesize=letter)

# Add some content
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a simple PDF with Version Control.")

# Adding version control information in the PDF’s metadata
c._doc.info.title = 'PDF with Version Control'
c._doc.info.author = 'Author Name'
c._doc.info.subject = 'Demonstrating Version Control in PDF'
c._doc.info.creator = 'Your Application Name'
c._doc.info.producer = 'Your Company Name'
c._doc.info.creationDate = '20231015'
c._doc.info.modDate = '20231015'
# Custom metadata for version control
c._doc.info.custom_metadata = {'Version': '1.0', 'Revision': 'Initial Release'}

# Normally, here we would define layers (OCGs), but as an illustrative example,
# we will just add more content that could hypothetically be on another layer.
c.setFillColor(blue)  # Using the blue color for distinct visual representation
c.drawString(100, 710, "This text represents 'layered' content.")

# Save the PDF
c.save()

print("PDF created successfully with Version Control metadata.")