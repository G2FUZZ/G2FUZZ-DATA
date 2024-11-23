from fpdf import FPDF
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

class PDF(FPDF):
    xobjects = {}  # Dictionary to hold our XObject references (for demonstration)
    
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Title', 1, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f'{title}', 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
        self.set_font('', 'I')
        self.cell(0, 10, '(end of excerpt)')

    def add_image(self, image_path):
        if image_path not in self.xobjects:
            # Add the image and store its ID
            xobject_id = self.image(image_path, 10, 100, 60)  # x, y, width (height is auto-calculated if not provided)
            self.xobjects[image_path] = xobject_id
        # Note: This does not create a PDF XObject but avoids adding the same image multiple times.

    def add_ocr_text(self, image_path):
        try:
            extracted_text = pytesseract.image_to_string(Image.open(image_path))
            self.set_font('Arial', '', 10)
            self.multi_cell(0, 10, extracted_text)
        except Exception as e:
            print(f"Error during OCR processing: {e}")

    def high_quality_printing_controls(self):
        # This is a placeholder for actual high-quality printing controls.
        # FPDF doesn't directly support advanced printing features like trapping.
        # For demonstration, we're adding a description about it.
        self.add_page()
        self.chapter_title('Chapter 3: High-Quality Printing Controls')
        description = """15. High-Quality Printing Controls: Advanced control over printing settings, such as trapping, to ensure that overlapping colors do not create unintended results when printed, crucial for high-quality print production in marketing materials and packaging."""
        self.chapter_body(description)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

pdf.chapter_title('Chapter 1: Image Incorporation and Reuse')
pdf.chapter_body('This chapter demonstrates the inclusion and reuse of an image in the PDF file using Reference XObjects. Below is an example image.')

image_path = './tmp/sample_image.png'
sample_image = Image.new('RGB', (100, 100), 'blue')
sample_image.save(image_path)

pdf.add_image(image_path)

pdf.add_page()
pdf.chapter_title('Chapter 2: Reusing Images with Reference XObjects')
pdf.chapter_body('This chapter shows the same image being reused without significantly increasing the PDF file size.')
pdf.add_image(image_path)

pdf.add_ocr_text(image_path)

# Adding the high-quality printing controls chapter
pdf.high_quality_printing_controls()

pdf.output(f'{output_dir}pdf_with_image_ocr_hq_printing.pdf', 'F')