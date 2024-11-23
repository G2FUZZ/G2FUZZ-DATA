from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Create a directory for storing the output if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Register the DejaVuSans font that comes with ReportLab for wider Unicode support
dejavu_font_path = "DejaVuSans.ttf"
pdfmetrics.registerFont(TTFont('DejaVuSans', dejavu_font_path))

# Create a canvas
c = canvas.Canvas(os.path.join(output_dir, "multi_language_geospatial_features.pdf"), pagesize=letter)

# English text
c.setFont('DejaVuSans', 12)
c.drawString(100, 750, "Hello, this is English text.")

# Arabic text, note that Arabic is written right to left
arabic_text = "مرحبا، هذا نص باللغة العربية"
arabic_text_reversed = arabic_text[::-1]
c.drawString(100, 725, arabic_text_reversed)

# Chinese text
chinese_text = "你好，这是中文文本。"
c.setFont('DejaVuSans', 12)
c.drawString(100, 700, chinese_text)

# Geospatial Features Description
c.setFont('DejaVuSans', 10)
geospatial_features_description = "13. Geospatial Features: They can embed geospatial information, allowing for interactive maps and location data to be viewed and manipulated within the document."
c.drawString(50, 675, geospatial_features_description)

# Save the PDF file
c.save()

print("PDF with multi-language support and geospatial features generated successfully.")