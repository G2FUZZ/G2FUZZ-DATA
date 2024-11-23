from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_pdf_with_tags_and_transparency():
    # Create a SimpleDocTemplate for logical structure tags
    doc = SimpleDocTemplate("./tmp/layers_tags_transparency.pdf", pagesize=letter)
    
    # Register a TrueType font
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))  # Ensure 'Vera.ttf' is available
    
    styles = getSampleStyleSheet()
    Story = []

    # Layer 1: A solid rectangle (handled differently due to logical structure tags)
    Story.append(Paragraph("This is a solid black rectangle:", styles['Normal']))
    Story.append(Spacer(1, 12))
    
    # Layer 2: A transparent rectangle (description)
    Story.append(Paragraph("This is a blue rectangle with 50% transparency on top of the first one:", styles['Normal']))
    Story.append(Spacer(1, 12))
    
    # Layer 3: Text with transparency (description)
    Story.append(Paragraph("Hello, Transparent World! (with 50% transparency)", styles['Normal']))
    Story.append(Spacer(1, 12))
    
    # Unfortunately, direct drawing with transparency and embedding it into the Platypus flow is not straightforward.
    # The drawing operations below would normally be done directly on a canvas, not within the Platypus story flow.
    # For demonstration purposes, we will create the PDF with tags for the text descriptions above.
    # To incorporate direct drawing (like rectangles or custom text positions) with Platypus, one would typically use a Flowable class or draw directly on the canvas in a later step.
    
    # Finalize the document with logical structure tags
    doc.build(Story)

    # Creating a new canvas for drawing rectangles and text with transparency, which is not directly supported within Platypus
    c = canvas.Canvas("./tmp/layers_tags_transparency_drawings.pdf", pagesize=letter)
    
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

create_pdf_with_tags_and_transparency()