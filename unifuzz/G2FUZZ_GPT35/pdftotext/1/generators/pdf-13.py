from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Digital Signatures in PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

# Create a PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'PDF files can support digital signatures for authentication and integrity verification.')

# Adding Embedded Fonts feature
pdf.set_font('Times', '', 12)  # Embedding Times font
pdf.multi_cell(0, 10, 'PDF files can embed fonts to ensure consistent display across different devices.')

# Save the PDF file
pdf_output = './tmp/digital_signatures_and_embedded_fonts.pdf'
pdf.output(name=pdf_output, dest='F').encode('latin1')
print(f'PDF file with digital signatures and embedded fonts features generated and saved at: {pdf_output}')