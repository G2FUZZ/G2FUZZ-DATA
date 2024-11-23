from reportlab.pdfgen import canvas

# Create a PDF file with Multimedia Integration
pdf_path = './tmp/annotations_multimedia_example.pdf'
c = canvas.Canvas(pdf_path)

# Add annotations
c.drawString(100, 700, "This is a comment.")
c.drawString(100, 650, "This is a note.")
c.setFillColorRGB(1, 0, 0)
c.drawString(100, 600, "This text is highlighted.")

# Add Multimedia Integration
c.drawString(100, 550, "Multimedia Integration:")
c.drawString(100, 530, "1. Add audio and video elements for enhanced user engagement.")

c.save()