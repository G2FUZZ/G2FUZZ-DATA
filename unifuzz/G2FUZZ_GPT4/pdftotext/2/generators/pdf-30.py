from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def create_pdf_with_self_containment():
    c = canvas.Canvas("./tmp/layers_transparency_self_containment.pdf", pagesize=letter)
    
    # Register a TrueType font (self-contained in the PDF)
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))  # Ensure 'Vera.ttf' is available in your working directory
    
    # Set up a transparent color
    transparent_blue = Color(0, 0, 1, alpha=0.5)  # Blue with 50% transparency
    
    # Layer 1: A solid rectangle
    c.setFillColor(black)
    c.rect(100, 600, 200, 100, fill=1)
    
    # Layer 2: A transparent rectangle on top of the first one
    c.setFillColor(transparent_blue)
    c.rect(150, 650, 200, 100, fill=1)
    
    # Layer 3: Text with transparency
    c.setFillAlpha(0.5)  # Apply transparency to the text
    c.setFillColor(blue)
    c.setFont("Vera", 20)  # Using the embedded TrueType font
    c.drawString(160, 700, "Hello, Transparent World!")
    
    # Reset transparency for future operations
    c.setFillAlpha(1.0)
    
    c.save()

# Ensure the necessary font file is available
font_path = 'Vera.ttf'
if not os.path.exists(font_path):
    # Code to download or locate the font file should be added here
    # For the sake of this example, we're assuming the file is already available
    pass

create_pdf_with_self_containment()