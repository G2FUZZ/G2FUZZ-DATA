from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Define the path for saving the PDF
pdf_path = "./tmp/color_management_example.pdf"

# Create a canvas object
c = canvas.Canvas(pdf_path, pagesize=letter)

# Set a title (optional)
c.setTitle("Color Management Example")

# Example of sophisticated color management by specifying colors in different ways
# and ensuring they are accurately represented

# Using named colors
c.setFillColor(colors.red)
c.rect(100, 700, 100, 50, fill=1, stroke=0)

# Using RGB colors
c.setFillColorRGB(0, 1, 0)  # Pure green
c.rect(100, 630, 100, 50, fill=1, stroke=0)

# Using CMYK colors
c.setFillColorCMYK(0, 0, 1, 0)  # Pure blue
c.rect(100, 560, 100, 50, fill=1, stroke=0)

# Adding a gradient as an example of sophisticated color use (requires PDF level 2.0)
c.setFillColor(colors.red)
c.rect(100, 490, 100, 50, fill=1, stroke=0)
c.setFillColor(colors.blue)
c.rect(100, 420, 100, 50, fill=1, stroke=0)

# To apply a gradient, you would typically use shading patterns or external libraries
# since the basic canvas.rect() does not support gradients directly.

# For semi-transparent fill, adjust the global alpha
c.saveState()
c.setFillAlpha(0.5)
c.setStrokeColor(colors.black)  # Set the stroke color here
c.rect(100, 490, 100, 50, fill=1, stroke=1)  # Use stroke=1 to apply the stroke
c.restoreState()

# Text to explain color management
c.setFillColor(colors.black)
c.setFont("Helvetica", 12)
c.drawString(220, 720, "Named color: Red")
c.drawString(220, 650, "RGB color: Green")
c.drawString(220, 580, "CMYK color: Blue")
c.drawString(220, 510, "Gradient from Red to Blue")

# Save the PDF file
c.save()