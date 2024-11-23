from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a directory if it doesn't exist
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to save the PDF
file_path = './tmp/digital_print_ready_with_repurposable_content.pdf'

# Create a canvas
c = canvas.Canvas(file_path, pagesize=letter)
width, height = letter  # Get the default letter size

# Text to add to the PDF
text_content = """
Digital Print-Ready: PDFs can be optimized for printing, ensuring that the printed document matches the on-screen version
in terms of layout, colors, and fonts, making it ideal for professional print production.

Repurposable Content: PDF files can be structured to enable content reflow and repurposing, making it easier to adapt content for different screen sizes and devices, enhancing accessibility.
"""

# Add the text
c.drawString(72, height-72, text_content)  # 72 points = 1 inch from the border

# Save the PDF
c.save()

print(f"PDF file has been saved to: {file_path}")