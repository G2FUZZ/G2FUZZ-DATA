from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features Including JavaScript', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Text for Compression feature
compression_text = """10. Compression: PDF files support various compression algorithms, enabling them to contain high-quality information in relatively small file sizes."""
pdf.multi_cell(0, 10, compression_text)

# Adding a new page for JavaScript feature
pdf.add_page()
javascript_text = """6. JavaScript: PDFs can incorporate JavaScript to create dynamic forms and interactive elements, enhancing user interaction and functionality of the document."""
pdf.multi_cell(0, 10, javascript_text)

# Save the PDF to a file in the ./tmp/ directory
pdf_file_path = './tmp/features_including_javascript.pdf'
pdf.output(pdf_file_path)

print(f"PDF file has been created at: {pdf_file_path}")