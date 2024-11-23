from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Ensure the ./tmp/ directory exists or create it
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the correct path to your image here
image_path = "correct/path/to/your/image.jpg"  # Update this line with the correct path

# Create a PDF file
pdf_path = os.path.join(output_dir, "pdf_with_image.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)

# Verify the image path before attempting to add it to the PDF
if os.path.exists(image_path):
    # Add an image. Specify dimensions and position as needed
    c.drawImage(image_path, 100, 500, width=200, height=150)  # Adjust the position and size as needed
else:
    print(f"Error: The specified image file does not exist at {image_path}")

# Save the PDF
c.save()