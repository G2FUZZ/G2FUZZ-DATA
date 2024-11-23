from reportlab.pdfgen import canvas

# Create a PDF file with annotations
c = canvas.Canvas("./tmp/annotations.pdf")
c.drawString(100, 700, "PDF with Annotations")
c.drawString(100, 650, "Annotations: Highlighting, Comments, Sticky Notes")
c.showPage()
c.save()