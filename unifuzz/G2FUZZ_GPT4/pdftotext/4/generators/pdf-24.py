from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib import colors
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Helper function for page numbering
def add_page_number(canvas, page_num, x=100, y=100):
    canvas.saveState()
    canvas.setFont('Times-Roman', 10)
    # This example adds page number as a roman numeral, you can format it differently
    page_label = str(page_num)  # Change this as per requirement, for Roman: reportlab.lib.pagesizes.toRoman(page_num)
    canvas.drawString(x, y, page_label)
    canvas.restoreState()

# Create a PDF with specific layout settings
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    
    # Configure styles and spacing
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    
    # Define pages info
    pages = [
        {
            "heading": "Page Layout Preservation",
            "text": "Ensures that the layout, spacing, fonts, and images appear as intended, regardless of the software or device used to view the document."
        },
        {
            "heading": "Second Page Title",
            "text": "This is an example of the second page to demonstrate page numbering and labels."
        }
    ]

    for i, page in enumerate(pages, start=1):
        # Adding a Heading
        frame1 = Frame(50, height - 100, width - 100, 50, showBoundary=0)
        story = [Paragraph(page["heading"], styleH)]
        frame1.addFromList(story, c)
        
        # Adding a paragraph
        frame2 = Frame(50, height - 200, width - 100, 100, showBoundary=0)
        story = [Paragraph(page["text"], styleN)]
        frame2.addFromList(story, c)

        # Optionally add an image to the first page as an example
        if i == 1:
            image_path = 'path/to/your/image.jpg'  # Update this path to an actual image file path
            # Ensure the image file exists before trying to add it
            if os.path.exists(image_path):
                c.drawImage(image_path, 100, 400, width=300, height=200)  # Example dimensions and position

        # Page number
        add_page_number(c, i, x=500, y=50)  # Example position for the page number

        # Finalize the page
        c.showPage()

    # Finalize the PDF
    c.save()

# Generate the PDF
pdf_path = './tmp/layout_preservation_with_pagenums.pdf'
create_pdf(pdf_path)