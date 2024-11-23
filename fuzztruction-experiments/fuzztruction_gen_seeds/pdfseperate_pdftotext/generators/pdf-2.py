from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a PDF with embedded images
c = canvas.Canvas("./tmp/image_embedding.pdf", pagesize=letter)
width, height = letter  # Default page size (8.5 * 11 inches, or 215.9mm * 279.4mm)

# Embedding a raster image (JPEG, PNG, etc.)
raster_image_path = './tmp/image.jpg'  # Update the path to your image

# Check if the raster image file exists before attempting to draw it
if os.path.exists(raster_image_path):
    c.drawImage(raster_image_path, x=100, y=height - 300, width=200, height=200)  # Adjust position and size as needed
else:
    print(f"Error: The file {raster_image_path} does not exist.")

# Embedding a vector image (SVG)
vector_image_path = './tmp/vector.svg'  # Update the path to your SVG file

# Check if the vector image file exists before attempting to draw it
if os.path.exists(vector_image_path):
    drawing = svg2rlg(vector_image_path)
    renderPDF.draw(drawing, c, 300, height - 400)  # Adjust position as needed
else:
    print(f"Error: The file {vector_image_path} does not exist.")

c.save()