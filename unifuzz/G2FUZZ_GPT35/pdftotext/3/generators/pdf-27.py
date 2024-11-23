from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import pytesseract
from io import BytesIO

def add_watermark(c, text):
    c.saveState()
    c.setFont("Helvetica", 40)
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
    c = canvas.Canvas("./tmp/extended_pdf_with_ocr.pdf", pagesize=letter)

    font_path = "path/to/Helvetica.ttf"  # Provide the correct path to the Helvetica.ttf font file
    pdfmetrics.registerFont(TTFont('Helvetica', font_path))
    c.setFont("Helvetica", 12)

    c.setViewerPreference('/PageMode', '/UseOutlines')

    for i in range(1, 6):  # Creating multiple pages with different content
        c.bookmarkPage(f'Page {i}', fit=f'/Fit{i}')
        c.drawString(100, 700, f'This is Page {i}')
        add_watermark(c, f'Watermark on Page {i}')

        if i % 2 == 0:  # Adding different watermarks based on page number
            add_watermark(c, "Confidential")
        else:
            add_watermark(c, "Draft")

        c.showPage()

    # Perform OCR on an example image and add the OCR result to the PDF
    image_path = "path/to/another_example_image.jpg"  # Provide the path to another example image for OCR
    ocr_text = perform_ocr(image_path)
    c.drawString(100, 600, f"OCR Result: {ocr_text}")

    c.save()
except Exception as e:
    print(f"Error: {e}")