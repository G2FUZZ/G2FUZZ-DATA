from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Compression Feature', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Instantiating a PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Adding content about PDF compression
content = """12. Compression: PDFs support efficient compression of document content, reducing file size without significantly impacting quality, which is crucial for storage and distribution."""

pdf.multi_cell(0, 10, content)

# Saving the PDF to a file
output_path = './tmp/pdf_compression_feature.pdf'
pdf.output(output_path)

print(f'PDF file has been saved to: {output_path}')