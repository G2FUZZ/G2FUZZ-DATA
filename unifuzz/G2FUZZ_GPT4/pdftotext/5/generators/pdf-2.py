from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
pdf_file = os.path.join(output_dir, 'vector_raster_graphics.pdf')
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Add a vector graphic (a rectangle in this example)
c.setStrokeColorRGB(0, 0, 0)
c.setFillColorRGB(0.7, 0.7, 0.7)
c.rect(100, 600, 200, 100, fill=1)

# Create a simple raster image (100x100 red square) using PIL
raster_image_path = os.path.join(output_dir, 'temp_raster_image.png')
img = Image.new('RGB', (100, 100), (255, 0, 0))
img.save(raster_image_path)

# Insert the raster image into the PDF
c.drawImage(raster_image_path, 100, 450, width=200, height=100)

# Finalize and save the PDF
c.showPage()
c.save()

# Clean up the temporary raster file
os.remove(raster_image_path)

print(f"PDF with vector and raster graphics saved to {pdf_file}")