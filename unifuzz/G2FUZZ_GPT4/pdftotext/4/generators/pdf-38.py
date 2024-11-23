import os
from fpdf import FPDF
from PIL import Image
import pytesseract

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Demo PDF with OCR and Tagged Feature', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_ocr_text(self, image_path):
        """
        Extracts text from an image and adds it to the PDF.
        """
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, text)
        except Exception as e:
            print(f"An error occurred during OCR processing: {e}")

    def add_tagged_content(self, tag_type, content):
        """
        Adds tagged content to the PDF for accessibility. 
        Note: This is a simplified approach to demonstrate tagged PDF concept. 
        """
        # This is a placeholder for adding tagged content. FPDF does not support tagged PDFs out of the box.
        # This function is here to illustrate where and how you might integrate or simulate tagged PDF functionality.
        # Actual implementation would require a library that supports PDF/UA or similar standards.
        if tag_type.lower() == 'heading':
            self.set_font('Arial', 'B', 16)
        else:  # Default to normal text
            self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Specify font for a tagged content example
pdf.add_tagged_content('heading', 'Tagged Content Example:')
pdf.add_tagged_content('paragraph', 'This is a paragraph tagged as such for accessibility purposes. Tagged PDFs allow screen readers and other assistive technologies to interpret and navigate the document more effectively.')

# Add a heading cell
pdf.cell(0, 10, 'Image and OCR Example:', 0, 1)

# Ensure the ./tmp directory exists
image_path = './tmp/sample.jpg'
os.makedirs(os.path.dirname(image_path), exist_ok=True)

# Before adding the image, make sure the image file exists at the specified path
if os.path.exists(image_path):
    pdf.image(image_path, x = 10, y = 80, w = 100)  # Adjusted y position to accommodate tagged content
    pdf.ln(85)  # Move below the image
    pdf.add_ocr_text(image_path)  # Add OCR text below the image
else:
    print(f"Error: The file {image_path} does not exist.")

# Save the PDF to a file
pdf.output('./tmp/generated_pdf_with_ocr_and_tagged.pdf')