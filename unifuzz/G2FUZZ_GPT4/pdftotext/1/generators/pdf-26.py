from fpdf import FPDF
import os

# Create a class to represent the PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features: Compression & JavaScript Support', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create a PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Existing Compression feature text
compression_text = ("11. Compression: PDF format supports efficient compression algorithms, reducing file size "
                    "without significantly compromising quality, facilitating easier storage and sharing.")
pdf.multi_cell(0, 10, compression_text)
pdf.ln(10)  # Add a line break for spacing

# New JavaScript Support feature text
javascript_support_text = ("12. JavaScript Support: PDF forms and documents can include JavaScript for form validation, "
                           "automation of repetitive tasks, and customization of user interactions.")
pdf.multi_cell(0, 10, javascript_support_text)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the PDF into the ./tmp/ directory
pdf_file_path = './tmp/features_demo.pdf'
pdf.output(pdf_file_path)

print(f"PDF file has been saved to {pdf_file_path}")