from fpdf import FPDF

class PDFWithComplexStructures(FPDF):
    def __init__(self):
        super().__init__()
        self.bookmark_page_numbers = {}
        self.watermark_text = None

    def add_bookmark(self, title, page_number):
        self.bookmark_page_numbers[title] = page_number

    def add_page(self, title=None):
        super().add_page()
        if title:
            self.add_bookmark(title, self.page_no())

    def set_watermark(self, text):
        self.watermark_text = text

    def header(self):
        if self.watermark_text:
            self.set_text_color(192, 192, 192)
            self.set_font('Arial', 'B', 50)
            self.text(10, 100, self.watermark_text)

    def add_custom_content(self):
        self.set_xy(10, 30)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Table of Contents:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, '1. Introduction', 0, 1, 'L')
        self.cell(0, 10, '2. Methodology', 0, 1, 'L')
        self.cell(0, 10, '3. Results', 0, 1, 'L')

    def add_bookmark_with_link(self, title, page_number):
        self.add_page()
        self.set_xy(10, 50)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Go to page {page_number}', 0, 1, 'L')
        self.add_link(title, page_number)

    def add_link(self, title, page_number):
        self.set_link(page=page_number, link='page' + str(page_number))  # Fixed the missing closing parenthesis

# Create a PDF file with complex structures, bookmarks, and watermarks
pdf = PDFWithComplexStructures()
pdf.add_page(title='First Page')
pdf.set_font("Arial", size=12)
pdf.add_custom_content()
pdf.cell(200, 10, txt="This is the first page", ln=True)
pdf.add_bookmark_with_link('Introduction', 2)
pdf.add_page(title='Second Page')
pdf.cell(200, 10, txt="This is the second page", ln=True)
pdf.add_bookmark_with_link('Methodology', 3)
pdf.add_page(title='Third Page')
pdf.cell(200, 10, txt="This is the third page", ln=True)
pdf.add_bookmark_with_link('Results', 4)
pdf.set_watermark('CONFIDENTIAL')

output_dir = './tmp/'
output_filename = output_dir + 'pdf_with_complex_structures.pdf'
pdf.output(name=output_filename)