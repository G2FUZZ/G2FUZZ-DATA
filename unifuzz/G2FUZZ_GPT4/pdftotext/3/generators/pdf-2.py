from fpdf import FPDF
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

class PDF(FPDF):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, f'{title}', 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, body):
        # Read text file
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 10, body)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 10, '(end of excerpt)')

    def add_image(self, image_path):
        self.image(image_path, 10, 100, 0, 60)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

# Adding a chapter
pdf.chapter_title('Chapter 1: Image Incorporation')
pdf.chapter_body('This chapter demonstrates the inclusion of an image in the PDF file. Below is an example image.')
# Ensure you have an image in the specified path or adjust the path to where your image is located.
# For this example, make sure you have an image at "./tmp/sample_image.png"
image_path = './tmp/sample_image.png'
# Creating a sample image for demonstration. This should be replaced with your actual image path.
from PIL import Image
sample_image = Image.new('RGB', (100, 100), 'blue')
sample_image.save(image_path)

# Adding an image (ensure the image path is correct and points to a valid image file)
pdf.add_image(image_path)

pdf.output(f'{output_dir}pdf_with_image.pdf', 'F')