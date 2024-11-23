from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PIL import Image
import pytesseract

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple PDF file
c = canvas.Canvas(f"{output_dir}example_with_ocr.pdf", pagesize=letter)

# Add some content
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a simple PDF.")
c.setFillColorRGB(1, 0, 0)
c.drawString(100, 710, "This text represents 'layered' content.")
c.save()

# Use OCR on an image and save the result as a PDF
image_path = f"{output_dir}sample_image.jpg"

# Check if the image file exists
if os.path.exists(image_path):
    # Load the image with PIL
    image = Image.open(image_path)
    # Use pytesseract to do OCR on the image
    ocr_result = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')

    # Save the OCR result as a PDF
    with open(f"{output_dir}example_with_ocr_ocr_layer.pdf", 'wb') as f:
        f.write(ocr_result)

    print("PDF with OCR created successfully.")
else:
    print(f"Error: The file {image_path} does not exist. Please ensure the image file is placed in the ./tmp/ directory.")