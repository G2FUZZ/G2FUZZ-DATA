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
    c = canvas.Canvas("./tmp/complex_pdf_file.pdf", pagesize=letter)

    font_path = "path/to/Arial.ttf"  # Provide the correct path to the Arial.ttf font file
    pdfmetrics.registerFont(TTFont('Arial', font_path))
    c.setFont("Arial", 12)

    c.setViewerPreference('/PageMode', '/UseOutlines')

    # Page 1
    c.bookmarkPage('Introduction', fit='/Fit')
    c.drawString(100, 700, "Introduction Page")
    add_watermark(c, "Confidential")
    c.showPage()

    # Page 2
    c.bookmarkPage('Chapter 1', fit='/Fit')
    c.drawString(100, 700, "Chapter 1 Page")
    add_watermark(c, "Draft")
    c.showPage()

    # Page 3
    c.bookmarkPage('Chapter 2', fit='/Fit')
    c.drawString(100, 700, "Chapter 2 Page")
    add_watermark(c, "Confidential")
    c.showPage()

    # Page 4
    c.bookmarkPage('Conclusion', fit='/Fit')
    c.drawString(100, 700, "Conclusion Page")
    add_watermark(c, "Final")
    c.showPage()

    c.save()
except Exception as e:
    print(f"Error: {e}")