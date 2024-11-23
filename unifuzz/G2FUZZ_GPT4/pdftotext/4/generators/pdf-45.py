import os
import csv
from fpdf import FPDF
from PIL import Image
import pytesseract
import qrcode

class EnhancedPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Advanced PDF Document with Dynamic Content', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Advanced Features Included', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, label, 0, 1)
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section_from_csv(self, csv_path):
        """
        Adds a section with dynamic content loaded from a CSV file.
        """
        self.add_page()
        self.chapter_title('Dynamic Data Section')
        try:
            with open(csv_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                    self.chapter_body(', '.join(row))
        except Exception as e:
            print(f"Error loading CSV data: {e}")

    def add_qr_code(self, data, size=50):
        """
        Generates a QR code for given data and embeds it into the PDF.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = './tmp/qr_code.png'
        img.save(img_path)
        self.image(img_path, x=10, y=None, w=size)
        os.remove(img_path)  # Clean up the generated QR code image file

    def add_link(self, text, url):
        """
        Adds a text with a hyperlink.
        """
        self.set_text_color(0, 0, 255)
        self.set_font('Arial', 'U', 12)
        self.write(10, text, url)
        self.set_text_color(0)
        self.ln(20)  # Move below the link

# Create instance of EnhancedPDF class
pdf = EnhancedPDF()

# Add a page
pdf.add_page()

# Add a section with the title and body
pdf.chapter_title('Introduction to Advanced PDF Features')
pdf.chapter_body('This document showcases advanced features such as dynamic content from CSV files, embedding QR codes, and adding hyperlinks.')

# Ensure the ./tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Add dynamic content from a CSV
csv_path = './tmp/sample_data.csv'
# Make sure your CSV exists or this will raise an error
pdf.add_section_from_csv(csv_path)

# Add a QR code linking to some geospatial data or any other data
pdf.add_qr_code('https://example.com/geospatial-data')

# Add a hyperlink
pdf.add_link('Click here to visit GitHub', 'https://github.com')

# Save the PDF to a file
pdf.output('./tmp/advanced_generated_pdf.pdf')