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
    c = canvas.Canvas("./tmp/extended_pdf_file.pdf", pagesize=letter)

    font_path = "path/to/Arial.ttf"  # Provide the correct path to the Arial.ttf font file
    pdfmetrics.registerFont(TTFont('Arial', font_path))
    c.setFont("Arial", 12)

    c.setViewerPreference('/PageMode', '/UseOutlines')

    # Cover Page
    c.bookmarkPage('Cover Page', fit='/Fit')
    c.drawString(100, 700, "Cover Page")
    add_watermark(c, "Draft Version")
    c.showPage()

    # Table of Contents
    c.bookmarkPage('Table of Contents', fit='/Fit')
    c.drawString(100, 700, "Table of Contents")
    c.setFillColorRGB(0, 0, 1)  # Blue color for TOC
    c.drawString(100, 680, "1. Introduction")
    c.drawString(100, 660, "2. Chapter 1")
    c.drawString(100, 640, "3. Chapter 2")
    c.drawString(100, 620, "4. Conclusion")
    c.showPage()

    # Introduction
    c.bookmarkPage('Introduction', fit='/Fit')
    c.drawString(100, 700, "Introduction Page")
    add_watermark(c, "Confidential")
    c.showPage()

    # Chapter 1
    c.bookmarkPage('Chapter 1', fit='/Fit')
    c.drawString(100, 700, "Chapter 1 Page")
    add_watermark(c, "Draft")
    c.showPage()

    # Chapter 2
    c.bookmarkPage('Chapter 2', fit='/Fit')
    c.drawString(100, 700, "Chapter 2 Page")
    add_watermark(c, "Confidential")
    c.showPage()

    # Conclusion
    c.bookmarkPage('Conclusion', fit='/Fit')
    c.drawString(100, 700, "Conclusion Page")
    add_watermark(c, "Final Version")
    c.showPage()

    c.save()
except Exception as e:
    print(f"Error: {e}")