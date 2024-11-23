from fpdf import FPDF

class PDFWithBookmarks(FPDF):
    def __init__(self):
        super().__init__()
        self.bookmark_page_numbers = {}

    def add_bookmark(self, title, page_number):
        self.bookmark_page_numbers[title] = page_number

    def add_page(self, title=None):
        super().add_page()
        if title:
            self.add_bookmark(title, self.page_no())

# Create a PDF file with bookmarks
pdf = PDFWithBookmarks()
pdf.add_page(title='First Page')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is the first page", ln=True)
pdf.add_page(title='Second Page')
pdf.cell(200, 10, txt="This is the second page", ln=True)
pdf.add_page(title='Third Page')
pdf.cell(200, 10, txt="This is the third page", ln=True)

output_dir = './tmp/'
output_filename = output_dir + 'pdf_with_bookmarks.pdf'
pdf.output(name=output_filename)