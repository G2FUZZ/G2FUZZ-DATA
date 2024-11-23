from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Define the path for saving the PDF file
output_path = './tmp/text_and_fonts_embedding.pdf'

# Register a TTFont (TrueType Font)
# You can replace 'Vera.ttf' with any TrueType font file you have available.
# For this example, it assumes Vera.ttf is in the same directory as the script.
# If you don't have it, you can use any other TTF file, just ensure to change the path or name.
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

# Create a canvas
c = canvas.Canvas(output_path, pagesize=letter)

# Set the font to Vera, size 12
c.setFont('Vera', 12)

# Add some text to the page
text = "This is a sample text with the Vera font embedded in the PDF file."
c.drawString(72, 720, text)  # Position: 72 points from the left and 720 from the bottom

# Save the PDF file
c.save()

print("PDF file has been created with text and embedded font.")