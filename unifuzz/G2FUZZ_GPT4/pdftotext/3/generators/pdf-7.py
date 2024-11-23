from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue

# Create a function to add a transparent rectangle
def add_transparent_rectangle(c, color, x, y, width, height, transparency):
    # Set the fill color with transparency
    c.setFillAlpha(transparency)
    c.setFillColor(color)
    # Draw the rectangle
    c.rect(x, y, width, height, fill=1)

# Create a new PDF with a canvas
c = canvas.Canvas("./tmp/layers_transparency.pdf", pagesize=letter)

# Set background
c.setFillColor(black)
c.rect(0, 0, 600, 800, fill=1)

# Add opaque rectangle
add_transparent_rectangle(c, blue, 100, 600, 200, 100, 1.0)

# Add semi-transparent rectangle
add_transparent_rectangle(c, blue, 150, 550, 200, 100, 0.5)

# Add very transparent rectangle
add_transparent_rectangle(c, blue, 200, 500, 200, 100, 0.2)

# Save the PDF
c.save()