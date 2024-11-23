from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features - Compression & OCR', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

title = 'Compression & OCR'
body = 'PDF files support various compression methods to reduce file size without compromising quality. \n\n' \
       'OCR (Optical Character Recognition): PDF files can be created with OCR technology to convert scanned images of text into searchable and editable text.'

pdf.chapter_title(title)
pdf.chapter_body(body)

pdf.output('./tmp/compression_ocr_features.pdf')