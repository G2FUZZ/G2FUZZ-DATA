from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Compression and Certification Features', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create instance of FPDF class
pdf = PDF()
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell for Compression
compression_text = ("10. Compression: They support various compression algorithms to reduce file size "
                    "without significantly compromising quality, making documents easier to store and share.")
pdf.multi_cell(0, 10, compression_text)

# Add a cell for Certification and Timestamping
certification_text = ("8. Certification and Timestamping: PDFs can be certified and time-stamped to validate the "
                      "authenticity and integrity of the document at a specific point in time.")
pdf.multi_cell(0, 10, certification_text)

# Save the pdf with name .pdf
pdf_file_path = os.path.join(output_dir, "PDF_Compression_Certification_Feature.pdf")
pdf.output(pdf_file_path)

print(f"PDF file has been saved at: {pdf_file_path}")