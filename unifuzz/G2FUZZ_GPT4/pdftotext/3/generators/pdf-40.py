from fpdf import FPDF
import os
from PIL import Image, ImageDraw

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
    
    def flatten_transparency(self, image_path):
        """
        Flatten an image's transparency layer to ensure compatibility with 
        processes that cannot handle transparency.
        """
        # Open the image
        with Image.open(image_path) as img:
            # Convert the image to RGBA if it is not
            img = img.convert("RGBA")
            
            # Create a new background image with white background
            background = Image.new("RGB", img.size, (255, 255, 255))
            
            # Paste the image onto the background
            background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
            
            # Save the flattened image
            flattened_path = os.path.splitext(image_path)[0] + "_flattened.png"
            background.save(flattened_path)
            
            return flattened_path

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

# Adding a chapter
pdf.chapter_title('Chapter 1: Image Incorporation with Transparency Flattening')
pdf.chapter_body('This chapter demonstrates the inclusion of an image with transparency flattening in the PDF file. Below is an example image after transparency flattening.')

# Creating a sample image for demonstration. This should be replaced with your actual image path.
image_path = './tmp/sample_image_with_transparency.png'
# Create a sample image with transparency for demonstration
sample_image = Image.new('RGBA', (100, 100))
draw = ImageDraw.Draw(sample_image)
draw.rectangle([10, 10, 90, 90], fill=(0, 0, 255, 127))  # Semi-transparent fill
sample_image.save(image_path)

# Flatten the transparency and get the path of the flattened image
flattened_image_path = pdf.flatten_transparency(image_path)

# Adding an image (ensure the image path is correct and points to a valid image file)
pdf.add_image(flattened_image_path)

pdf.output(f'{output_dir}pdf_with_flattened_image.pdf', 'F')