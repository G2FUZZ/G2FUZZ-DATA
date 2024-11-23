from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from arabic_reshaper import reshape
from bidi.algorithm import get_display
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def add_rtl_text(canvas, text, x, y, font_name='Helvetica', font_size=12):
    reshaped_text = reshape(text)  # Reshape the RTL text
    bidi_text = get_display(reshaped_text)  # Reorder the reshaped text for proper display
    canvas.setFont(font_name, font_size)
    canvas.drawString(x, y, bidi_text)

def create_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # English text
    c.drawString(100, 750, "This document supports multiple languages.")
    
    # Arabic text
    arabic_text = "هذا المستند يدعم لغات متعددة."
    add_rtl_text(c, arabic_text, 100, 730)
    
    # Chinese text
    chinese_text = "该文档支持多种语言。"
    c.setFont("Helvetica", 12)
    c.drawString(100, 710, chinese_text)
    
    # Non-Rectangular Links
    # Draw an ellipse which will act as a clickable link
    c.setStrokeColor(colors.red)
    c.setFillColor(colors.transparent)
    c.ellipse(100, 600, 200, 650, stroke=1, fill=0)
    # Define the clickable area for the link (ellipse coordinates)
    c.linkURL("https://example.com", (100, 600, 200, 650), relative=1, thickness=0, color=colors.transparent)
    
    c.save()

# Generate the PDF
create_pdf(output_dir + 'multi_language_support_with_links.pdf')