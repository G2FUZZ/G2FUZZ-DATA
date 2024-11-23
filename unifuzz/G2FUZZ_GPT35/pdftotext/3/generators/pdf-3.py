from reportlab.pdfgen import canvas

# Create a PDF file with annotations
def create_pdf_with_annotations(file_path):
    c = canvas.Canvas(file_path)
    
    # Adding text annotation
    c.drawString(100, 700, "This is a text annotation")
    
    # Adding highlight annotation
    c.setStrokeColorRGB(1, 0, 0)  # Red color for highlight
    c.rect(100, 600, 200, 50, fill=1)
    
    # Adding sticky note annotation
    c.setStrokeColorRGB(0, 0, 0)  # Black color for sticky note
    c.rect(100, 500, 50, 50)
    c.drawString(160, 510, "Sticky Note")
    
    c.save()

# Generate PDF file with annotations
file_path = './tmp/annotated_pdf.pdf'
create_pdf_with_annotations(file_path)

print(f"PDF file with annotations created at: {file_path}")