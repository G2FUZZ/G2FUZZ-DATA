from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Path to the output PDF file
output_file = os.path.join(output_dir, 'sample.pdf')

# Register a TT font (TrueType Font)
# Replace 'Vera.ttf' with the path to a font file you want to embed
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

# Create a canvas to draw on
c = canvas.Canvas(output_file, pagesize=letter)

# Set the font to the registered font and specify the size
c.setFont('Vera', 12)

# Draw some text on the canvas
text = "Hello, World! This is a sample PDF with an embedded font."
c.drawString(72, 720, text)  # Position: 72 points from the left, 720 from the bottom

# Save the PDF file
c.save()