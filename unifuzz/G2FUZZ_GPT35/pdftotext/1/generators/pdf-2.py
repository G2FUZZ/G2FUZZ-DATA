from fpdf import FPDF
import os

class PDFWithImage(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_image(self, image_path):
        self.set_xy(10, 30)
        if os.path.exists(image_path):
            self.image(image_path, link='', type='', w=100)
        else:
            print(f"Error: Image file '{image_path}' not found.")

# Create PDF with image
pdf = PDFWithImage()
pdf.add_page()

# Provide the full path to the image file
image_path = '/full/path/to/image.jpg'
pdf.add_image(image_path)

pdf.output('./tmp/image_pdf.pdf')