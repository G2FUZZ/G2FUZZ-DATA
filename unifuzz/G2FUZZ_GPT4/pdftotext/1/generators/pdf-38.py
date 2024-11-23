from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the path for the new PDF file
file_path = os.path.join(output_dir, "digital_publishing_options_with_3d_and_compression.pdf")

# Create a PDF file with the specified content
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    content = """\
15. Digital Publishing Options: PDF format is widely used for digital publishing, supporting features like page transitions and embedded page thumbnails, suitable for e-books, magazines, and online brochures.
2. 3D Models: Some PDFs can include 3D models that users can interact with, useful for technical documentation, architectural plans, and educational materials.
8. Object-level Compression: Advanced compression techniques can compress specific elements of a PDF file, such as text, images, and vector graphics, optimizing file size without broadly compromising quality.
    """
    text.textLines(content)
    c.drawText(text)
    c.showPage()
    c.save()

create_pdf(file_path)