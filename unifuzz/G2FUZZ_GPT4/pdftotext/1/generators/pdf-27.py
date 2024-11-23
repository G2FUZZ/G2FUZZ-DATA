from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import CMYKColor
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os. path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple PDF file with print production features
c = canvas.Canvas(f"{output_dir}example_with_print_production_features.pdf", pagesize=letter)

# Add some content
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a simple PDF with Print Production Features.")

# Print Production Feature: Example of 'layered' content with CMYK color for print production
c.setFillColor(CMYKColor(0, 1, 0, 0))  # Pure Magenta
c.drawString(100, 710, "This text is in CMYK color, suitable for print.")

# Print Production Features: Adding bleed marks (just for illustration, not actual bleed marks)
c.setLineWidth(0.5)
c.setStrokeColorRGB(1, 0, 0)  # Red color to easily see the bleed marks

# Drawing faux bleed marks
bleed_mark_length = 20  # Length of the bleed mark
page_width, page_height = letter
c.line(0, page_height/2, bleed_mark_length, page_height/2)  # left middle
c.line(page_width, page_height/2, page_width-bleed_mark_length, page_height/2)  # right middle
c.line(page_width/2, 0, page_width/2, bleed_mark_length)  # bottom middle
c.line(page_width/2, page_height, page_width/2, page_height-bleed_mark_length)  # top middle

# Saving the PDF with Print Production Features
c.save()

print("PDF with Print Production Features created successfully.")