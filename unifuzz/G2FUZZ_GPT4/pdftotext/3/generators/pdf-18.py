from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
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

def create_pdf_with_drm(output_path):
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
    
    # Enable DRM by setting permissions
    # Note: ReportLab does not directly support DRM features such as restricting editing, copying, or printing.
    # However, you can use PyPDF2 or pikepdf libraries to open this generated PDF and set restrictions as shown below.
    # The following line is just an illustrative placeholder and won't actually apply any DRM.
    # You would need to use an external library to open and modify the PDF permissions.
    # c.saveState()
    
    c.save()

# Note for the developer: After generating the PDF with ReportLab, use PyPDF2 or pikepdf to apply DRM.
# Example with pikepdf (not included in this script):
# import pikepdf
# with pikepdf.open('source.pdf') as pdf:
#     pdf.save('secured_output.pdf', encryption=pikepdf.Encryption(owner='owner_password', user='user_password', allow=pikepdf.Permissions.none))

# Generate the PDF with DRM placeholder
create_pdf_with_drm(output_dir + 'multi_language_support_with_drm.pdf')