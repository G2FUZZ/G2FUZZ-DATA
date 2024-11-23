from reportlab.pdfgen import canvas

# Create a PDF file with layers
def create_layered_pdf(file_name):
    c = canvas.Canvas(f'./tmp/{file_name}.pdf')
    
    # Add a background layer
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.rect(0, 0, 400, 400, fill=1, stroke=0)
    c.drawString(10, 380, "Background Layer")
    
    # Add a foreground layer
    c.setFillColorRGB(0.2, 0.2, 0.2)
    c.rect(50, 50, 300, 300, fill=1, stroke=0)
    c.drawString(60, 320, "Foreground Layer")
    
    c.save()

# Create a PDF file with layers
create_layered_pdf('layered_pdf')