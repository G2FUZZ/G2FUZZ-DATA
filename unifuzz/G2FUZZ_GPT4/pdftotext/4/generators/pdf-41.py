from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def add_layered_graphics_to_pdf_with_metadata(text, filename, metadata, compression=True):
    """
    Add text, layered graphics, and custom metadata to a PDF file with an option for compression.
    """
    c = canvas.Canvas(filename, pagesize=A4)
    if compression:
        c.setPageCompression(1)

    # Adding custom metadata
    c.setAuthor(metadata.get('Author', ''))
    c.setTitle(metadata.get('Title', ''))
    c.setSubject(metadata.get('Subject', ''))
    # Additional metadata can be added similarly

    # Text layer
    c.drawString(100, 800, text)
    
    # Starting a new layer for graphics
    c.saveState()
    c.setFillColorRGB(1,0,0) # Red color
    c.rect(100, 600, 100, 100, fill=1)
    c.restoreState()
    
    # Another Layer for different graphics
    c.saveState()
    c.setFillColorRGB(0,1,0) # Green color
    c.circle(150, 550, 50, fill=1)
    c.restoreState()
    
    c.save()

# Directory to save the PDF
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Filename for the PDF
pdf_filename = os.path.join(output_dir, 'layered_graphics_pdf_with_metadata.pdf')

# Text to add to the PDF
text_content = "This PDF demonstrates layered graphics along with text content and custom metadata."

# Custom metadata for the PDF
custom_metadata = {
    'Author': 'John Doe',
    'Title': 'Layered Graphics PDF',
    'Subject': 'Demonstration of Layered Graphics and Custom Metadata in a PDF'
}

# Generate the PDF with text, layered graphics, and custom metadata
add_layered_graphics_to_pdf_with_metadata(text_content, pdf_filename, custom_metadata)