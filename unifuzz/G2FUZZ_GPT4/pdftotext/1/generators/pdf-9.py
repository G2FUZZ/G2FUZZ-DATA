from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple PDF file
c = canvas.Canvas(f"{output_dir}example_with_layers.pdf", pagesize=letter)

# Add some content
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a simple PDF.")

# Normally, here we would define layers (OCGs), but as an illustrative example,
# we will just add more content that could hypothetically be on another layer.
c.setFillColorRGB(1, 0, 0)
c.drawString(100, 710, "This text represents 'layered' content.")

# Save the PDF
c.save()

print("PDF created successfully.")