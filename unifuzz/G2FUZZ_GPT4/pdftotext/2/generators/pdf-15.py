from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import pdfencrypt
import os

# Create a directory for storing the output if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Register the DejaVuSans font that comes with ReportLab for wider Unicode support
# Note: Ensure 'DejaVuSans.ttf' is available in your ReportLab package or adjust the path accordingly
dejavu_font_path = "DejaVuSans.ttf"  # This path might need to be adjusted based on your ReportLab installation
pdfmetrics.registerFont(TTFont('DejaVuSans', dejavu_font_path))

# DRM settings - encrypt the PDF to restrict copying, printing, and editing
# You can specify a user password and an owner password. Owner password allows full access if opened with it.
# Permissions can be controlled by the `canPrint`, `canModify`, `canCopy`, `canAnnotate` parameters.
encryption = pdfencrypt.StandardEncryption(userPassword="userpass", ownerPassword="ownerpass",
                                           canPrint=0, canModify=0, canCopy=0, canAnnotate=0)

# Create a canvas with encryption
c = canvas.Canvas(os.path.join(output_dir, "multi_language_support_with_DRM.pdf"), pagesize=letter, encrypt=encryption)

# English text
c.setFont('DejaVuSans', 12)
c.drawString(100, 750, "Hello, this is English text.")

# Arabic text, note that Arabic is written right to left
# For simplicity, this example will use reversed text as a placeholder for Arabic.
arabic_text = "مرحبا، هذا نص باللغة العربية"
arabic_text_reversed = arabic_text[::-1]  # Normally, you would reshape and reorder Arabic text here
c.drawString(100, 725, arabic_text_reversed)

# Chinese text
chinese_text = "你好，这是中文文本。"
c.setFont('DejaVuSans', 12)
c.drawString(100, 700, chinese_text)

# Save the PDF file
c.save()

print("PDF with multi-language support and DRM generated successfully.")