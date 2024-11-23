from fpdf import FPDF

# Create a PDF class
class PDFExtended(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Digital Signatures in PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def extended_features(self):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, 'PDF files can support advanced features like digital rights management, XML forms, and multimedia.')

# Create a PDF object with extended features
pdf_extended = PDFExtended()
pdf_extended.add_page()
pdf_extended.set_font('Arial', '', 12)
pdf_extended.multi_cell(0, 10, 'PDF files can support digital signatures for authentication and integrity verification.')
pdf_extended.extended_features()

# Save the PDF file with extended features
pdf_output_extended = './tmp/digital_signatures_extended.pdf'
pdf_extended.output(name=pdf_output_extended, dest='F').encode('latin1')
print(f'PDF file with digital signatures and extended features generated and saved at: {pdf_output_extended}')