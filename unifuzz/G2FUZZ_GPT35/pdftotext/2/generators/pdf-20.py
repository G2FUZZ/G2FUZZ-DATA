from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

def add_watermark(c, text):
    c.saveState()
    c.setFont("Helvetica", 50)
    c.setFillAlpha(0.1)
    c.translate(400, 300)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()

# Create a PDF file with interactive elements, geospatial data feature, and watermarks
filename = "./tmp/pdf_with_watermarks.pdf"
c = canvas.Canvas(filename, pagesize=letter)

# Add Watermark
add_watermark(c, "CONFIDENTIAL")

c.drawString(100, 700, "Click here to open Google")
c.linkURL("http://www.google.com", (100, 700, 200, 715), relative=1, thickness=1, color=blue)
c.bookmarkPage("Google", fit="XYZ", top=700)
c.drawString(100, 600, "Geospatial Data: PDF files can support geospatial data integration for mapping and location-based applications.")
c.showPage()
c.save()

print(f"PDF file with interactive elements, Geospatial Data feature, and Watermarks generated and saved as '{filename}'")