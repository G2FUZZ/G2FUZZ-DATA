from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame, Image
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a PDF with specific layout settings
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    
    # Configure styles and spacing
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    
    # Adding a Heading
    frame1 = Frame(50, height - 100, width - 100, 50, showBoundary=0)
    story = [Paragraph("Page Layout Preservation", styleH)]
    frame1.addFromList(story, c)
    
    # Adding a paragraph
    text = "Ensures that the layout, spacing, fonts, and images appear as intended, regardless of the software or device used to view the document."
    frame2 = Frame(50, height - 200, width - 100, 100, showBoundary=0)
    story = [Paragraph(text, styleN)]
    frame2.addFromList(story, c)

    # Adding an image
    image_path = 'path/to/your/image.jpg'  # Update this path to an actual image file path
    # Ensure the image file exists before trying to add it
    if os.path.exists(image_path):
        c.drawImage(image_path, 100, 400, width=300, height=200)  # Example dimensions and position

    # Finalize the PDF
    c.showPage()
    c.save()

# Generate the PDF
pdf_path = './tmp/layout_preservation.pdf'
create_pdf(pdf_path)