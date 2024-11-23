from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue, pink, red, green, magenta, white  # Added 'white' here
import os

# Function to add a transparent rectangle
def add_transparent_rectangle(c, color, x, y, width, height, transparency):
    # Set the fill color with transparency
    c.setFillAlpha(transparency)
    c.setFillColor(color)
    # Draw the rectangle
    c.rect(x, y, width, height, fill=1)

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with a canvas
pdf_path = os.path.join(output_dir, "enhanced_layers_transparency.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter  # Keep the page size handy

# Add title
c.setFont("Helvetica", 20)
c.setFillColor(black)
c.drawString(50, height - 50, "Enhanced Layers and Transparency PDF")

# Set background
c.setFillColor(black)
c.rect(0, 0, width, height, fill=1)

# Add opaque rectangle
add_transparent_rectangle(c, blue, 100, 600, 200, 100, 1.0)

# Add semi-transparent rectangle
add_transparent_rectangle(c, pink, 150, 550, 200, 100, 0.5)

# Add very transparent rectangle
add_transparent_rectangle(c, red, 200, 500, 200, 100, 0.2)

# Add an image (ensure you have an image named 'example.jpg' in the output_dir)
image_path = os.path.join(output_dir, "example.jpg")
if os.path.exists(image_path):
    c.drawImage(image_path, 400, height - 200, width=100, height=75)
else:
    c.setFillColor(white)  # Corrected use of 'white'
    c.drawString(400, height - 125, "Image not found.")

# Add interactive form fields
# Note: The import below is redundant as colors were already imported at the top
# from reportlab.lib.colors import magenta, pink, blue, green

# Text Field
form = c.acroForm
c.setFillColor(black)
c.drawString(50, height - 250, "Your Comment:")
form.textfield(name='txtComment', tooltip='Comment', x=150, y=height - 265, borderStyle='inset',
               borderColor=magenta, fillColor=pink, width=400, height=40,
               textColor=blue, forceBorder=True)

# CheckBox
c.drawString(50, height - 300, "Agree to Terms:")
form.checkbox(name='chkAgree', tooltip='Check to agree', x=180, y=height - 310,
              buttonStyle='check', borderColor=black, fillColor=green, textColor=blue,
              forceBorder=True)

# Save the PDF
c.save()

print(f"Enhanced layers and transparency PDF has been created at: {pdf_path}")