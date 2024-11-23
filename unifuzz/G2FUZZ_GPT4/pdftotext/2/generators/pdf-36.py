from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.lib import colors

# Create a PDF with vector graphics and transparency groups
def create_pdf_with_vector_graphics_and_transparency(output_path):
    # Set up the PDF canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Create a drawing object
    d = Drawing(width, height)

    # Add vector graphics (For simplicity, we'll draw a rectangle and a circle)
    d.add(renderPDF.Path(fillColor=colors.red, strokeColor=colors.blue, strokeWidth=4,
                         path="M100,100 L150,200 Q200,300 250,200 L300,100 Z"))  # Example path
    d.add(renderPDF.Circle(300, 600, 100, fillColor=colors.green, strokeColor=colors.black, strokeWidth=2))

    # Add transparency group
    # Begin a transparency group
    c.saveState()
    c.setFillColorRGB(0, 1, 0, alpha=0.5)  # Set the fill color with transparency
    c.setStrokeColorRGB(0, 0, 1, alpha=0.5)  # Set the stroke color with transparency
    c.rect(150, 450, 200, 100, fill=1)  # Draw a rectangle with transparency
    c.restoreState()  # End the transparency group

    # Render the drawing onto the canvas
    renderPDF.draw(d, c, 0, 0)

    # Save the PDF
    c.save()

# Output path
output_path = './tmp/vector_graphics_with_transparency.pdf'

# Create the PDF
create_pdf_with_vector_graphics_and_transparency(output_path)