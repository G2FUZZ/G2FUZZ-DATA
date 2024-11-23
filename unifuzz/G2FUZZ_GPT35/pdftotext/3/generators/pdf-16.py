from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def add_watermark(c, text):
    c.saveState()
    c.setFont("Arial", 40)
    c.setFillAlpha(0.5)
    c.translate(300, 400)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()

try:
    c = canvas.Canvas("./tmp/bookmarks_with_watermark.pdf", pagesize=letter)

    font_path = "path/to/Arial.ttf"  # Provide the correct path to the Arial.ttf font file
    pdfmetrics.registerFont(TTFont('Arial', font_path))
    c.setFont("Arial", 12)

    c.setViewerPreference('/PageMode', '/UseOutlines')

    c.bookmarkPage('Page 1', fit='/Fit')
    c.drawString(100, 700, "This is Page 1")
    add_watermark(c, "Confidential")

    c.showPage()

    c.bookmarkPage('Page 2', fit='/Fit')
    c.drawString(100, 700, "This is Page 2")
    add_watermark(c, "Draft")

    c.showPage()

    c.save()
except Exception as e:
    print(f"Error: {e}")