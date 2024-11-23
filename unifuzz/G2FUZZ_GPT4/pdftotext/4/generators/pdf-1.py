from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Define the path for saving the PDF file
pdf_path = "./tmp/text_and_font_embedding.pdf"

# Register a TrueType font
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# Create a canvas
c = canvas.Canvas(pdf_path, pagesize=letter)

# Set the font to the registered font and define the size
c.setFont("DejaVuSans", 12)

# Add some text to the PDF
c.drawString(72, 720, "Hello, this is a sample text with an embedded font!")

# Save the PDF file
c.save()

print(f"PDF generated successfully at {pdf_path}")