from fpdf import FPDF
import os
from PIL import Image
import pytesseract

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF with Interactive Elements and OCR', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_link(self, url, text):
        self.set_text_color(0, 0, 255)
        self.set_font('Arial', 'U', 12)
        self.write(10, text, url)

    def add_ocr_layer(self, image_path):
        # Ensure pytesseract is pointing to your installation of tesseract if not in PATH
        # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
        try:
            # Open the image and convert it to grayscale (optional, but often helps with OCR accuracy)
            img = Image.open(image_path).convert('L')
            ocr_text = pytesseract.image_to_string(img, lang='eng')

            # Add the OCR text as a chapter in the PDF
            self.add_page()
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, ocr_text)
        except Exception as e:
            print(f"Error processing OCR: {e}")

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

pdf = PDF()
pdf.add_page()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.chapter_title('Interactive Element: Hyperlink')
pdf.chapter_body('This PDF includes an interactive hyperlink element. You can click on the link below to visit a webpage.')

# Add a hyperlink
pdf.add_link('https://www.example.com', 'Visit Example.com')

# Assuming you have a scanned image to perform OCR on
# Replace 'path_to_image.jpg' with the actual file path
pdf.add_ocr_layer('path_to_image.jpg')

pdf.output('./tmp/interactive_elements_with_ocr.pdf')