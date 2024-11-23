from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def create_pdf_with_rich_media_annotations():
    pdf_path = "./tmp/layers_transparency_rich_media.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    # Register a TrueType font
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
    c.setFillAlpha(0.5)
    c.setFillColor(blue)
    c.setFont("Vera", 20)
    c.drawString(160, 700, "Hello, Transparent World!")
    
    c.setFillAlpha(1.0)  # Reset transparency for future operations
    
    # Rich Media Annotations
    # Note: ReportLab itself does not directly support embedding rich media annotations.
    # This example provides a placeholder approach. In practice, embedding rich media 
    # might require post-processing with a tool that supports this feature or a different library.
    
    c.drawString(100, 500, "Placeholder for Rich Media Annotation")
    c.drawString(100, 480, "Embed rich media here using an external tool.")
    
    c.save()
    
    # Incremental update: Adding a new page with annotations
    c = canvas.Canvas(pdf_path, pagesize=letter, invariant=1)
    c.setFont("Vera", 12)
    c.drawString(100, 100, "This is an incremental update.")
    c.save()

# Ensure the necessary font file is available
font_path = 'Vera.ttf'
if not os.path.exists(font_path):
    # Code to download or locate the font file should be added here
    pass

create_pdf_with_rich_media_annotations()