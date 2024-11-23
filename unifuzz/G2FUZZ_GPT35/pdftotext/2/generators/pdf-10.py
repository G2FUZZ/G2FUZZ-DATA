from reportlab.pdfgen import canvas

# Create a PDF file with layers
def create_pdf_with_layers(file_name):
    c = canvas.Canvas(file_name)
    
    # Create a base layer
    c.drawString(50, 800, "Base Layer Content")
    
    # Create a new layer
    c.saveState()
    c.drawString(50, 780, "New Layer Content")
    c.restoreState()
    
    c.save()

# Save the PDF file with layers
file_name = "./tmp/pdf_with_layers.pdf"
create_pdf_with_layers(file_name)
print(f"PDF file with layers created: {file_name}")