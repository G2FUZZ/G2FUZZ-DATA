from reportlab.pdfgen import canvas
from reportlab.lib.colors import red

# Create a PDF file with layers, watermarks, and digital signatures
def create_layered_pdf_with_watermark_and_signature(file_name, watermark_text, signature_text):
    c = canvas.Canvas(f'./tmp/{file_name}.pdf')
    
    # Add a background layer
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.rect(0, 0, 400, 400, fill=1, stroke=0)
    c.drawString(10, 380, "Background Layer")
    
    # Add a foreground layer
    c.setFillColorRGB(0.2, 0.2, 0.2)
    c.rect(50, 50, 300, 300, fill=1, stroke=0)
    c.drawString(60, 320, "Foreground Layer")
    
    # Add watermark
    c.setFont("Helvetica", 36)
    c.setFillAlpha(0.3)
    c.saveState()
    c.rotate(45)
    c.drawString(200, 200, watermark_text)
    c.restoreState()
    
    # Add digital signature
    c.setStrokeColor(red)
    c.setLineWidth(2)
    c.line(100, 100, 300, 100)
    c.drawString(100, 80, f"Digital Signature: {signature_text}")
    
    c.save()

# Create a PDF file with layers, watermarks, and digital signatures
create_layered_pdf_with_watermark_and_signature('layered_pdf_with_watermark_and_signature', 'Confidential', 'John Doe')