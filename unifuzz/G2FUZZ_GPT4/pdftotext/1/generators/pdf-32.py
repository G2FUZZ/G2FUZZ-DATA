from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Try to use a font that is commonly included with ReportLab
try:
    # Register a font capable of displaying multi-language characters
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
except Exception as e:
    print(f"Error registering font: {e}")

# Create a PDF
c = canvas.Canvas("./tmp/multi_language_tagged_pdf.pdf", pagesize=letter)
c.setTitle("Multi-Language Tagged PDF")
c.setAuthor("Author Name")
c.setSubject("Demonstration of Multi-Language and Tagged PDF Features")
c.setKeywords("PDF, Multi-Language, Tagged, Accessibility")

c.setFont('DejaVuSans', 12)

# English
c.drawString(72, 750, 'Hello, this is English text.')

# Arabic
c.saveState()
c.translate(72, 730)
c.scale(1, -1)
c.drawString(0, 0, 'مرحبا، هذا نص باللغة العربية.')  # Note: Arabic text is right to left
c.restoreState()

# Chinese
c.drawString(72, 710, '你好，这是中文。')

# Save the PDF file
c.save()

print("PDF file with multi-language support has been created.")