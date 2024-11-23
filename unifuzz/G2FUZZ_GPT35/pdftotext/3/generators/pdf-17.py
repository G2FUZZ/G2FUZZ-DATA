from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import pytesseract
from io import BytesIO

def add_watermark(c, text):
    c.saveState()
    c.setFont("Arial", 40)
    c.setFillAlpha(0.5)
    c.translate(300, 400)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()

def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

try:
    c = canvas.Canvas("./tmp/bookmarks_with_ocr.pdf", pagesize=letter)

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

    # Perform OCR on an example image and add the OCR result to the PDF
    image_path = "path/to/example_image.jpg"  # Provide the path to the example image for OCR
    ocr_text = perform_ocr(image_path)
    c.drawString(100, 600, f"OCR Result: {ocr_text}")

    c.showPage()

    c.save()
except Exception as e:
    print(f"Error: {e}")