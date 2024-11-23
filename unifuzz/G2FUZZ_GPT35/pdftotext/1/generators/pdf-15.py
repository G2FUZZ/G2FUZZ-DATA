from fpdf import FPDF

# Create a PDF class
class PDFWithOCR(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Digital Signatures and OCR in PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def add_ocr_feature(self):
        self.set_font('Arial', '', 12)
        self.ln(10)
        self.multi_cell(0, 10, 'PDF files can be created with OCR technology to make scanned text searchable and selectable.')

# Create a PDF object with OCR feature
pdf_with_ocr = PDFWithOCR()
pdf_with_ocr.add_page()
pdf_with_ocr.set_font('Arial', '', 12)
pdf_with_ocr.multi_cell(0, 10, 'PDF files can support digital signatures for authentication and integrity verification.')
pdf_with_ocr.add_ocr_feature()

# Save the PDF file with OCR feature
pdf_output_with_ocr = './tmp/digital_signatures_with_ocr.pdf'
pdf_with_ocr.output(name=pdf_output_with_ocr, dest='F').encode('latin1')
print(f'PDF file with digital signatures and OCR feature generated and saved at: {pdf_output_with_ocr}')