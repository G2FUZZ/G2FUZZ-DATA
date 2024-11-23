from fpdf import FPDF

class PDFWithBookmarksAndWatermarks(FPDF):
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

# Create a PDF file with bookmarks and watermarks
pdf = PDFWithBookmarksAndWatermarks()
pdf.add_page(title='First Page')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is the first page", ln=True)
pdf.add_page(title='Second Page')
pdf.cell(200, 10, txt="This is the second page", ln=True)
pdf.add_page(title='Third Page')
pdf.cell(200, 10, txt="This is the third page", ln=True)
pdf.set_watermark('CONFIDENTIAL')

output_dir = './tmp/'
output_filename = output_dir + 'pdf_with_bookmarks_and_watermarks.pdf'
pdf.output(name=output_filename)