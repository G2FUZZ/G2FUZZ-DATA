from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

# Create a PDF file with a signature field
def create_pdf_with_signature():
    c = canvas.Canvas("./tmp/signed_pdf.pdf", pagesize=letter)
    c.drawString(100, 700, "Please sign here:")
    c.rect(100, 650, 200, 50, fill=0)
    c.setFillColor(blue)
    c.drawString(120, 665, "Signature")
    c.save()

create_pdf_with_signature()