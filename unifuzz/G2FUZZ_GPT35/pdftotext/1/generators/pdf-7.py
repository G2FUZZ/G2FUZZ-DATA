from reportlab.pdfgen import canvas

# Create a PDF file with layers
def create_pdf_with_layers(file_name):
    c = canvas.Canvas(file_name)

    # Create a layer for elements to be shown
    c.saveState()
    c.drawString(100, 700, "This is a visible element")
    c.restoreState()

    # Create a layer for elements to be hidden
    c.saveState()
    c.drawString(100, 600, "This is a hidden element")
    c.restoreState()

    c.save()

# Generate PDF file with layers
file_name = "./tmp/pdf_with_layers.pdf"
create_pdf_with_layers(file_name)
print(f"PDF file with layers generated: {file_name}")