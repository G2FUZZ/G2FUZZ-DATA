from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the path for the new PDF file including the OCGs feature description
file_path = os.path.join(output_dir, "enhanced_digital_publishing_options_with_ocgs.pdf")

# Create a PDF file with the specified content, including OCGs feature
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    content = """\
9. Layers (Optional Content Groups - OCGs): Beyond simply including layers, PDFs allow for the creation of optional content groups, which can be selectively viewed or hidden by the user, offering dynamic control over document presentation.
14. Non-linear (Optimized) PDF: This feature allows for faster display of PDF files from the web by downloading the pages in the order they are needed, rather than in sequential order.
15. Digital Publishing Options: PDF format is widely used for digital publishing, supporting features like page transitions and embedded page thumbnails, suitable for e-books, magazines, and online brochures.
    """
    text.textLines(content)
    c.drawText(text)
    c.showPage()
    c.save()

create_pdf(file_path)