from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def add_layered_graphics_to_pdf(text, filename, compression=True):
    """
    Add text and layered graphics to a PDF file with an option for compression.
    """
    c = canvas.Canvas(filename, pagesize=A4)
    if compression:
        c.setPageCompression(1)
    
    # Text layer
    c.drawString(100, 800, text)
    
    # Starting a new layer for graphics
    c.saveState()
    c.setFillColorRGB(1,0,0) # Red color
    c.rect(100, 600, 100, 100, fill=1)
    c.restoreState()
    
    # Another Layer for different graphics
    c.saveState()
    c.setFillColorRGB(0,1,0) # Green color
    c.circle(150, 550, 50, fill=1)
    c.restoreState()
    
    c.save()

# Directory to save the PDF
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Filename for the PDF
pdf_filename = os.path.join(output_dir, 'layered_graphics_pdf.pdf')

# Text to add to the PDF
text_content = "This PDF demonstrates layered graphics along with text content."

# Generate the PDF with text and layered graphics
add_layered_graphics_to_pdf(text_content, pdf_filename)