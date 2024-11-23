from reportlab.graphics.shapes import Drawing, Rect, Circle
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors  # Import the colors module

# Create a new PDF with vector graphics
c = canvas.Canvas("./tmp/vector_graphics_example.pdf", pagesize=letter)

# Draw some vector graphics (a simple rectangle and a circle)
c.setStrokeColorRGB(0.2, 0.5, 0.3)
c.setFillColorRGB(1, 0, 0)
c.rect(100, 650, 200, 100, fill=1)
c.setFillColorRGB(0.1, 0.2, 0.5)
c.circle(300, 550, 50, fill=1)

# Add some text
c.setFillColorRGB(0, 0, 0)
c.setFont("Helvetica", 12)
c.drawString(100, 620, "Vector Graphics Example: Rectangle and Circle")

# Save the PDF
c.save()

# Now, let's create a more complex vector graphic using ReportLab's Drawing object
drawing = Drawing(400, 200)

# Add a rectangle and a circle to the drawing, using colors from the colors module
drawing.add(Rect(50, 50, 300, 100, fillColor=colors.blue))
drawing.add(Circle(200, 150, 50, fillColor=colors.red))

# Save this drawing as a PDF
drawing_file = "./tmp/complex_vector_graphics_example.pdf"
renderPDF.drawToFile(drawing, drawing_file)