from reportlab.pdfgen import canvas

# Create a PDF file with annotations
def create_pdf_with_annotations(file_path):
    c = canvas.Canvas(file_path)
    
    # Add annotations
    c.drawString(100, 700, "This is a PDF file with annotations.")
    c.drawString(100, 650, "Annotations can be used to add comments, notes, and other information.")
    
    c.showPage()
    c.save()

# Generate a PDF file with annotations
file_path = "./tmp/pdf_with_annotations.pdf"
create_pdf_with_annotations(file_path)