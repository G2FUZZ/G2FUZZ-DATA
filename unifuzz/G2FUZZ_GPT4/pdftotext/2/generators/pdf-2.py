from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.lib import colors  # Import the colors module

# Create a PDF with vector graphics
def create_pdf_with_vector_graphics(output_path):
    # Set up the PDF canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Create a drawing object
    d = Drawing(width, height)

    # Add vector graphics (For simplicity, we'll draw a rectangle and a circle)
    d.add(renderPDF.Path(fillColor=colors.red, strokeColor=colors.blue, strokeWidth=4,
                         path="M100,100 L150,200 Q200,300 250,200 L300,100 Z"))  # Example path
    d.add(renderPDF.Circle(300, 600, 100, fillColor=colors.green, strokeColor=colors.black, strokeWidth=2))

    # Render the drawing onto the canvas
    renderPDF.draw(d, c, 0, 0)

    # Save the PDF
    c.save()

# Output path
output_path = './tmp/vector_graphics.pdf'

# Create the PDF
create_pdf_with_vector_graphics(output_path)