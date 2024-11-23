from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black
import os
from PyPDF2 import PdfReader, PdfWriter  # Updated import statement

# Create a directory for storing the output if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Register the DejaVuSans font
dejavu_font_path = "DejaVuSans.ttf"  # This path might need to be adjusted
pdfmetrics.registerFont(TTFont('DejaVuSans', dejavu_font_path))

# Create a temporary PDF file path
temp_pdf_path = os.path.join(output_dir, "temp_multi_language_support_redacted.pdf")

# Create a canvas
c = canvas.Canvas(temp_pdf_path, pagesize=letter)

# Function to draw redaction marks
def apply_redaction(x, y, width, height, color=black):
    """
    Apply redaction mark on specified coordinates.
    
    :param x: X coordinate
    :param y: Y coordinate
    :param width: Width of the redaction mark
    :param height: Height of the redaction mark
    :param color: Color of the redaction mark
    """
    c.setFillColor(color)
    c.rect(x, y, width, height, stroke=0, fill=1)

# English text
c.setFont('DejaVuSans', 12)
c.drawString(100, 750, "Hello, this is English text.")

# Arabic text, note that Arabic is written right to left
arabic_text = "مرحبا، هذا نص باللغة العربية"
arabic_text_reversed = arabic_text[::-1]
c.drawString(100, 725, arabic_text_reversed)

# Redact part of the Arabic text as example
apply_redaction(100, 720, 200, 15)

# Chinese text
chinese_text = "你好，这是中文文本。"
c.setFont('DejaVuSans', 12)
c.drawString(100, 700, chinese_text)

# Save the temporary PDF file
c.save()

# Now, let's proceed without adding Page Labels to the PDF
final_pdf_path = os.path.join(output_dir, "multi_language_support_redacted.pdf")

input_pdf = PdfReader(temp_pdf_path)  # Updated to use PdfReader
output_pdf = PdfWriter()  # Updated to use PdfWriter

# Copy pages from input_pdf to output_pdf
for i in range(len(input_pdf.pages)):
    output_pdf.add_page(input_pdf.pages[i])

# Write the output PDF
with open(final_pdf_path, "wb") as f_out:
    output_pdf.write(f_out)

# Clean up the temporary file
os.remove(temp_pdf_path)

print("PDF with multi-language support and redaction generated successfully.")