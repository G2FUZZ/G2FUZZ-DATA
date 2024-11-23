from reportlab.pdfgen import canvas

# Create a PDF file with layers
def create_layered_pdf(file_path, layers):
    c = canvas.Canvas(file_path)
    
    # Add content to different layers
    for layer_name, content in layers.items():
        c.setFillColorRGB(0, 0, 0)
        c.drawString(100, 700, f"Layer: {layer_name}")
        c.drawString(100, 680, content)
        c.showPage()
    
    c.save()

# Define layers and content
layers = {
    "Layer 1": "This is content for Layer 1",
    "Layer 2": "This is content for Layer 2",
    "Layer 3": "This is content for Layer 3"
}

# Create a PDF file with layers
file_path = './tmp/layered_pdf.pdf'
create_layered_pdf(file_path, layers)