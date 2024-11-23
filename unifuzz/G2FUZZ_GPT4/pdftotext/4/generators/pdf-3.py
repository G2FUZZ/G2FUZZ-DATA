import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Demo PDF with Raster Image', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Specify font
pdf.set_font('Arial', 'B', 16)

# Add a cell
pdf.cell(40, 10, 'Image Example:', 0, 1)

# Ensure the ./tmp directory exists
image_path = './tmp/sample.jpg'
os.makedirs(os.path.dirname(image_path), exist_ok=True)

# Before adding the image, make sure the image file exists at the specified path
if os.path.exists(image_path):
    pdf.image(image_path, x = 10, y = 30, w = 100)
else:
    print(f"Error: The file {image_path} does not exist.")

# Save the PDF to a file
pdf.output('./tmp/generated_pdf_with_image.pdf')