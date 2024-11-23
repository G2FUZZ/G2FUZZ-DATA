from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

# Create a PDF file with interactive elements
filename = "./tmp/interactive_pdf.pdf"
c = canvas.Canvas(filename, pagesize=letter)
c.drawString(100, 700, "Click here to open Google")
c.linkURL("http://www.google.com", (100, 700, 200, 715), relative=1, thickness=1, color=blue)
c.bookmarkPage("Google", fit="XYZ", top=700)
c.showPage()
c.save()

print(f"PDF file with interactive elements generated and saved as '{filename}'")