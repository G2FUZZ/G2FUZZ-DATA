from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

# Create a PDF file
c = canvas.Canvas("./tmp/metadata_pdf.pdf")

# Set metadata
c.setAuthor("John Doe")
c.setTitle("Sample PDF with Metadata")
c.setKeywords("report, metadata, python, pdf")

# Set content
c.setFont("Helvetica", 12)
c.drawString(100, 700, "PDF file with metadata")

# Save the PDF file
c.save()