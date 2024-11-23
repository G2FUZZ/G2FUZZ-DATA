from reportlab.pdfgen import canvas

# Create a PDF file with annotations
def create_pdf_with_annotations(file_path):
    c = canvas.Canvas(file_path)
    c.drawString(100, 700, "This is a PDF file with annotations.")
    c.drawString(100, 600, "Users can add comments, highlights, and annotations to this document.")
    c.drawString(100, 500, "Enjoy annotating!")
    c.showPage()
    c.save()

# Save the PDF file with annotations
file_name = "./tmp/pdf_with_annotations.pdf"
create_pdf_with_annotations(file_name)