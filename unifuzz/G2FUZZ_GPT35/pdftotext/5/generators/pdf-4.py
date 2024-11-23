from reportlab.pdfgen import canvas

# Create a PDF file
pdf_path = './tmp/annotations_example.pdf'
c = canvas.Canvas(pdf_path)

# Add annotations
c.drawString(100, 700, "This is a comment.")
c.drawString(100, 650, "This is a note.")
c.setFillColorRGB(1, 0, 0)
c.drawString(100, 600, "This text is highlighted.")

c.save()