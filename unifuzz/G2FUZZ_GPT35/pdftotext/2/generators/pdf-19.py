from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

# Create a PDF file with interactive elements and geospatial data feature
filename = "./tmp/interactive_pdf_with_geospatial_data.pdf"
c = canvas.Canvas(filename, pagesize=letter)
c.drawString(100, 700, "Click here to open Google")
c.linkURL("http://www.google.com", (100, 700, 200, 715), relative=1, thickness=1, color=blue)
c.bookmarkPage("Google", fit="XYZ", top=700)
c.drawString(100, 600, "Geospatial Data: PDF files can support geospatial data integration for mapping and location-based applications.")
c.showPage()
c.save()

print(f"PDF file with interactive elements and Geospatial Data feature generated and saved as '{filename}'")