from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color, black

def create_pdf_with_transparency():
    c = canvas.Canvas("./tmp/multidimensional_transparent_pdf.pdf", pagesize=A4)
    
    # Set up a semi-transparent color
    transparent_color = Color(0, 0, 0, alpha=0.5)  # Black with 50% transparency
    
    # Draw some text with transparency
    c.setFillColor(transparent_color)
    c.drawString(100, 800, "This text is semi-transparent.")
    
    # Reset color for opaque text
    c.setFillColor(black)
    c.drawString(100, 780, "Placeholder for 3D Model")
    c.drawString(100, 760, "In practice, 3D content would need to be embedded post creation,")
    c.drawString(100, 740, "using a tool that supports 3D models in PDFs, such as Adobe Acrobat.")
    
    # Draw a semi-transparent rectangle
    c.setFillAlpha(0.5)  # 50% transparency
    c.rect(100, 600, 200, 100, fill=True, stroke=False)
    
    c.save()

create_pdf_with_transparency()