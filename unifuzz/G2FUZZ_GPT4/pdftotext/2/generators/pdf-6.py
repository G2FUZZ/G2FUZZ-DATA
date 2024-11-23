from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue

def create_pdf_with_layers_and_transparency():
    c = canvas.Canvas("./tmp/layers_and_transparency.pdf", pagesize=letter)
    
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
    c.setFont("Helvetica", 20)
    c.drawString(160, 700, "Hello, Transparent World!")
    
    # Reset transparency for future operations
    c.setFillAlpha(1.0)
    
    c.save()

create_pdf_with_layers_and_transparency()