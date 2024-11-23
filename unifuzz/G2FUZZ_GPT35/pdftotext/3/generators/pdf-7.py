from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Create a canvas object
c = canvas.Canvas("./tmp/bookmarks.pdf", pagesize=letter)

# Set up a custom font for bookmarks
font_path = "path/to/Arial.ttf"  # Provide the correct path to the Arial.ttf font file
try:
    pdfmetrics.registerFont(TTFont('Arial', font_path))
    c.setFont("Arial", 12)

    # Add bookmarks
    c.setViewerPreference('/PageMode', '/UseOutlines')
    c.bookmarkPage('Page 1', fit='/Fit')
    c.drawString(100, 700, "This is Page 1")
    c.showPage()

    c.bookmarkPage('Page 2', fit='/Fit')
    c.drawString(100, 700, "This is Page 2")
    c.showPage()

    # Save the PDF file
    c.save()
except Exception as e:
    print(f"Error: {e}")