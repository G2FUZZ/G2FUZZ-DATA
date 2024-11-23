from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue, PCMYKColor  # Adjusted import

# Create a function to add a transparent rectangle
def add_transparent_rectangle(c, color, x, y, width, height, transparency):
    # Set the fill color with transparency
    c.setFillAlpha(transparency)
    c.setFillColor(color)
    # Draw the rectangle
    c.rect(x, y, width, height, fill=1)

# Function to add a rectangle with CMYK color and overprint
def add_cmyk_color_rectangle(c, cmyk_color, x, y, width, height, overprint=False):
    # Set overprint state for non-stroking operations
    c.setFillOverprint(overprint)
    c.setFillColor(cmyk_color)
    c.rect(x, y, width, height, fill=1)
    # Reset overprint state to default
    c.setFillOverprint(False)

# Create a new PDF with a canvas
c = canvas.Canvas("./tmp/layers_transparency_spot_overprint.pdf", pagesize=letter)

# Define a CMYK color
Pantone300 = PCMYKColor(100, 50, 0, 0, spotName='Pantone 300 C', density=1.0)  # Adjusted for CMYK color

# Set background
c.setFillColor(black)
c.rect(0, 0, 600, 800, fill=1)

# Add opaque rectangle
add_transparent_rectangle(c, blue, 100, 600, 200, 100, 1.0)

# Add semi-transparent rectangle
add_transparent_rectangle(c, blue, 150, 550, 200, 100, 0.5)

# Add very transparent rectangle
add_transparent_rectangle(c, blue, 200, 500, 200, 100, 0.2)

# Add a rectangle with CMYK color without overprint
add_cmyk_color_rectangle(c, Pantone300, 100, 400, 200, 100, overprint=False)

# Add a rectangle with CMYK color with overprint
add_cmyk_color_rectangle(c, Pantone300, 150, 350, 200, 100, overprint=True)

# Save the PDF
c.save()