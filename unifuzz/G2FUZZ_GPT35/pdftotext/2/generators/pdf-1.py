from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Features of PDF Files', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of PDF class
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add features to the PDF file
pdf.chapter_title('Feature:')
pdf.chapter_body('1. Portability: PDF files are designed to be portable and can be viewed on any device with a PDF reader.')

# Save the PDF file in ./tmp/ directory
pdf_output = './tmp/portability_feature.pdf'
pdf.output(name=pdf_output, dest='F')

print(f'PDF file generated: {pdf_output}')