import os
from fpdf import FPDF
from PIL import Image
import pytesseract

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Demo PDF with OCR Feature', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_ocr_text(self, image_path):
        """
        Extracts text from an image and adds it to the PDF.
        """
        # Ensure pytesseract is pointing to your installation of Tesseract if not in PATH
        # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, text)
        except Exception as e:
            print(f"An error occurred during OCR processing: {e}")

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Specify font
pdf.set_font('Arial', 'B', 16)

# Add a cell
pdf.cell(0, 10, 'Image and OCR Example:', 0, 1)

# Ensure the ./tmp directory exists
image_path = './tmp/sample.jpg'
os.makedirs(os.path.dirname(image_path), exist_ok=True)

# Before adding the image, make sure the image file exists at the specified path
if os.path.exists(image_path):
    pdf.image(image_path, x = 10, y = 30, w = 100)
    pdf.ln(85)  # Move below the image
    pdf.add_ocr_text(image_path)  # Add OCR text below the image
else:
    print(f"Error: The file {image_path} does not exist.")

# Save the PDF to a file
pdf.output('./tmp/generated_pdf_with_ocr.pdf')