from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Compression Example', 0, 1, 'C')

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
text = """10. Compression: PDF files support various compression algorithms, enabling them to contain high-quality information in relatively small file sizes."""
pdf.multi_cell(0, 10, text)

# Save the PDF to a file in the ./tmp/ directory
pdf_file_path = './tmp/compression_example.pdf'
pdf.output(pdf_file_path)

print(f"PDF file has been created at: {pdf_file_path}")