from fpdf import FPDF
import requests
from barcode import EAN13
from barcode.writer import ImageWriter
import os

class PDF(FPDF):
    # Other methods remain unchanged

    def insert_barcode(self, value):
        # Ensure the ./tmp/ directory exists
        tmp_dir = './tmp/'
        os.makedirs(tmp_dir, exist_ok=True)  # Create ./tmp/ if it doesn't exist
        
        # Generate barcode
        ean = EAN13(value, writer=ImageWriter())
        barcode_file = os.path.join(tmp_dir, f'barcode_{value}.png')
        ean.write(barcode_file)
        
        # Insert barcode image
        self.image(barcode_file, x=10, y=self.get_y(), w=50)
        os.remove(barcode_file)  # Clean up after embedding
        self.ln(60)  # Adjust line position after barcode

    def insert_image(self, image_path, img_w=0, img_h=0):
        # Ensure the image file exists
        if not os.path.exists(image_path):
            print(f"Error: The file {image_path} does not exist.")
            return

        if img_w == 0 and img_h == 0:
            self.image(image_path)
        else:
            self.image(image_path, w=img_w, h=img_h)
        self.ln()

# Ensure the ./tmp/ directory exists
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Adding an image with dynamic resizing
# Make sure to replace 'path_to_image.jpg' with the correct path
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
image_path = os.path.join(script_dir, 'path_to_image.jpg')  # Build the full path to the image
pdf.insert_image(image_path, img_w=100, img_h=100)

# Continue with the rest of your PDF generation code...

# Save the PDF to a file in the ./tmp/ directory
output_file = os.path.join(tmp_dir, 'advanced_pdf_features.pdf')
pdf.output(output_file)