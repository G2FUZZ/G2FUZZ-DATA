from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_complex_pdf(file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    
    # Base Layer
    c.setFillColorRGB(0, 0, 1)  # Blue color
    c.drawString(50, 800, "Base Layer Content")
    
    # Layer 1
    c.setFillColorRGB(1, 0, 0)  # Red color
    c.drawString(50, 780, "Layer 1 Content")
    
    # Layer 2
    c.setFillColorRGB(0, 1, 0)  # Green color
    c.drawString(50, 760, "Layer 2 Content")
    
    # Draw a rectangle on a separate layer
    c.setFillColorRGB(0.5, 0.5, 0.5)  # Gray color
    c.saveState()
    c.translate(200, 700)
    c.rotate(45)
    c.rect(0, 0, 100, 50, fill=1)
    c.restoreState()
    
    c.save()

file_name = "./tmp/complex_pdf_file.pdf"
create_complex_pdf(file_name)
print(f"Complex PDF file created: {file_name}")