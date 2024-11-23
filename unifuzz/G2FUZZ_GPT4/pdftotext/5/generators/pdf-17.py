from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features: Compression and Watermarks', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Instantiating a PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Adding content about PDF compression
compression_content = """12. Compression: PDFs support efficient compression of document content, reducing file size without significantly impacting quality, which is crucial for storage and distribution."""
pdf.multi_cell(0, 10, compression_content)

# Adding a space between the two features
pdf.ln(10)

# Adding content about Watermarks and Backgrounds
watermarks_backgrounds_content = """2. Watermarks and Backgrounds: PDFs can include watermarks and backgrounds, which can be used for branding, copyright protection, or simply to enhance the appearance of the document."""
pdf.multi_cell(0, 10, watermarks_backgrounds_content)

# Saving the PDF to a file
output_path = './tmp/pdf_features_compression_and_watermarks.pdf'
pdf.output(output_path)

print(f'PDF file has been saved to: {output_path}')