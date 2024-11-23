from fpdf import FPDF

class PDFWithBookmarksAndWatermarks(FPDF):
    def __init__(self):
        super().__init__()
        self.bookmark_page_numbers = {}
        self.watermark_text = None
        self.embedded_files = {}

    def add_bookmark(self, title, page_number):
        self.bookmark_page_numbers[title] = page_number

    def add_page(self, title=None):
        super().add_page()
        if title:
            self.add_bookmark(title, self.page_no())

    def set_watermark(self, text):
        self.watermark_text = text

    def add_embedded_file(self, file_name, file_data):
        self.embedded_files[file_name] = file_data

    def header(self):
        if self.watermark_text:
            self.set_text_color(192, 192, 192)
            self.set_font('Arial', 'B', 50)
            self.text(10, 100, self.watermark_text)

# Create a PDF file with bookmarks, watermarks, and embedded files
pdf = PDFWithBookmarksAndWatermarks()
pdf.add_page(title='First Page')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is the first page", ln=True)
pdf.add_page(title='Second Page')
pdf.cell(200, 10, txt="This is the second page", ln=True)
pdf.add_page(title='Third Page')
pdf.cell(200, 10, txt="This is the third page", ln=True)
pdf.set_watermark('CONFIDENTIAL')
pdf.add_embedded_file('sample.docx', b'Embedded Word Document Content')
pdf.add_embedded_file('sample.xlsx', b'Embedded Excel Spreadsheet Content')

output_dir = './tmp/'
output_filename = output_dir + 'pdf_with_bookmarks_watermarks_and_embedded_files.pdf'
pdf.output(name=output_filename)