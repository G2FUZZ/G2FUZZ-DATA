from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Create a PDF file with layers
def create_pdf_with_layers(file_name):
    c = Canvas(file_name, pagesize=letter)
    
    # Add content to different layers
    c.setFillColorRGB(1, 0, 0)  # Red color
    c.drawString(100, 700, "Layer 1 content")
    
    c.saveState()
    c.setFillColorRGB(0, 1, 0)  # Green color
    c.drawString(100, 600, "Layer 2 content")
    c.restoreState()
    
    c.saveState()
    c.setFillColorRGB(0, 0, 1)  # Blue color
    c.drawString(100, 500, "Layer 3 content")
    c.restoreState()
    
    c.save()

# Generate PDF file with layers
file_name = "./tmp/pdf_with_layers.pdf"
create_pdf_with_layers(file_name)