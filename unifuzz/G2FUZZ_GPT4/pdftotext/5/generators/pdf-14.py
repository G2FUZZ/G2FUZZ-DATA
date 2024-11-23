from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import arabic_reshaper
from bidi.algorithm import get_display

# Create a function to add RTL support
def add_rtl_text(canvas_obj, text, x, y, font_name='Helvetica', font_size=12):
    reshaped_text = arabic_reshaper.reshape(text)  # Reshape the text
    bidi_text = get_display(reshaped_text)  # Reorder the text for RTL
    canvas_obj.setFont(font_name, font_size)
    canvas_obj.drawString(x, y, bidi_text)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a PDF with multi-language support
c = canvas.Canvas("./tmp/multi_language_support.pdf", pagesize=letter)
c.setFont("Helvetica", 10)

# Adding English text
c.drawString(100, 750, "Hello World! (English)")

# Adding Arabic text
arabic_text = "مرحبا بالعالم! (Arabic)"
add_rtl_text(c, arabic_text, 100, 730)

# Adding Hebrew text (another RTL example)
hebrew_text = "שלום עולם! (Hebrew)"
add_rtl_text(c, hebrew_text, 100, 710)

# Adding French text
c.drawString(100, 690, "Bonjour le monde! (French)")

# Adding Chinese text
chinese_text = "你好，世界！(Chinese)"
c.drawString(100, 670, chinese_text)

# Save the PDF
c.save()