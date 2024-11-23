from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF file
output_file_path = './tmp/simple_pdf_with_text.pdf'
c = canvas.Canvas(output_file_path, pagesize=letter)  # Corrected variable name
c.drawString(100, 750, "This is a simple PDF file.")

# Normally, here you would have code to embed a 3D model if it was supported.

c.save()