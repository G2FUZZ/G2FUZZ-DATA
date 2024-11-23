from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the PDF file
pdf_path = os.path.join(output_dir, "text_and_fonts.pdf")

# Create a canvas
c = canvas.Canvas(pdf_path, pagesize=letter)

# Register a TTFont (TrueType Font) - this is optional if you're using standard fonts
# For custom fonts, uncomment and set the correct font name and path
# pdfmetrics.registerFont(TTFont('YourFontName', 'Path/To/YourFontFile.ttf'))

# Set the font to Helvetica, size 12
c.setFont("Helvetica", 12)

# Add some text
text = "Hello, world! This is a PDF with embedded text in Helvetica font."
c.drawString(72, 728, text)

# Save the PDF
c.save()

print(f"PDF file has been created at {pdf_path}")