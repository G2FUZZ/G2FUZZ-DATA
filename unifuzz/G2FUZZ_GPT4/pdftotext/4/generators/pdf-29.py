import os
from fpdf import FPDF
from PIL import Image
import pytesseract
from barcode import EAN13
from barcode.writer import ImageWriter

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Extended PDF with OCR, Mobile, Print Production, and Barcode Generation Tools Feature', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Enhanced with Print Production and Barcode Generation Tools', 0, 0, 'C')

    def add_ocr_text(self, image_path):
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, text)
        except Exception as e:
            print(f"An error occurred during OCR processing: {e}")

    def add_mobile_compatibility(self):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Mobile Compatibility Feature:', 0, 1)
        self.set_font('Arial', '', 12)
        mobile_compatibility_description = """
        5. Mobile Compatibility: Optimized for viewing and interaction on mobile devices, 
        ensuring accessibility and usability across various screen sizes and platforms.
        """
        self.multi_cell(0, 10, mobile_compatibility_description)

    def add_print_production_tools(self):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Print Production Tools Feature:', 0, 1)
        self.set_font('Arial', '', 12)
        print_production_tools_description = """
        7. Print Production Tools: Contains advanced features for print production, including output previews, color separations, and ink management, ensuring high-quality print outputs.
        """
        self.multi_cell(0, 10, print_production_tools_description)

    def add_barcode_generation(self):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Barcode Generation Feature:', 0, 1)
        self.set_font('Arial', '', 12)
        barcode_generation_description = """
        15. Barcode Generation: Supports the generation and inclusion of various types of barcodes within the document, useful for inventory, retail, and logistical applications.
        """
        self.multi_cell(0, 10, barcode_generation_description)
        # Ensure the directory exists
        barcode_dir = "./tmp"
        if not os.path.exists(barcode_dir):
            os.makedirs(barcode_dir)
        barcode_file = os.path.join(barcode_dir, "barcode.jpeg")
        # Generate and save the barcode
        barcode = EAN13("123456789012", writer=ImageWriter())
        barcode.save(barcode_file)
        # Verify the barcode file exists before attempting to add it to the PDF
        if os.path.exists(barcode_file):
            self.image(barcode_file, x=10, y=None, w=100)
        else:
            print(f"Failed to generate or locate the barcode image at {barcode_file}")

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Specify font
pdf.set_font('Arial', 'B', 16)

# Add a cell
pdf.cell(0, 10, 'Image, OCR, Mobile, Print Production, and Barcode Generation Tools Example:', 0, 1)

# Ensure the ./tmp directory exists
image_path = './tmp/sample.jpg'
os.makedirs(os.path.dirname(image_path), exist_ok=True)

if os.path.exists(image_path):
    pdf.image(image_path, x = 10, y = 30, w = 100)
    pdf.ln(85)
    pdf.add_ocr_text(image_path)
else:
    print(f"Error: The file {image_path} does not exist.")

pdf.add_mobile_compatibility()
pdf.add_print_production_tools()
pdf.add_barcode_generation()

# Save the PDF to a file
pdf_output_path = './tmp/extended_pdf_with_ocr_mobile_print_production_and_barcode_generation_tools.pdf'
pdf.output(pdf_output_path)

# Cleanup: Delete the barcode image file
barcode_file = "./tmp/barcode.jpeg"
if os.path.exists(barcode_file):
    os.remove(barcode_file)