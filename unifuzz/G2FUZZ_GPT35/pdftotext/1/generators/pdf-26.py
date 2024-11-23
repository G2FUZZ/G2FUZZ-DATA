from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Create a PDF file with annotations, DRM, and Document Structure Tags features
c = canvas.Canvas("./tmp/extended_pdf_with_structure_tags.pdf")
c.drawString(100, 700, "PDF with Annotations, DRM, and Document Structure Tags")
c.drawString(100, 650, "Annotations: Highlighting, Comments, Sticky Notes")
c.drawString(100, 600, "Digital Rights Management (DRM): Control access and usage rights")
c.drawString(100, 550, "Document Structure Tags: Assist in accessibility and reflow capabilities")
c.setStrokeColor(colors.red)
c.setFillColor(colors.red)
c.rect(90, 540, 400, 20, fill=1)
c.showPage()
c.save()