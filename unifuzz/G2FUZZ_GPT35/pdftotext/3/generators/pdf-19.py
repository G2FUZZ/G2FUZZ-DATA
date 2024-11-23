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
    c = canvas.Canvas("./tmp/bookmarks_with_watermark_and_fonts.pdf", pagesize=letter, bottomup=0)

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

    # Embedding Fonts
    pdfmetrics.registerFont(TTFont('Arial-Bold', font_path, subfontIndex=0, embed=1))
    pdfmetrics.registerFont(TTFont('Arial-Italic', font_path, subfontIndex=1, embed=1))

    c.save()
except Exception as e:
    print(f"Error: {e}")