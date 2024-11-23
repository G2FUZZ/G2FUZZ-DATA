from fpdf import FPDF
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF with Hyperlinks', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_hyperlink(self, x, y, w, h, url):
        self.set_xy(x, y)
        self.set_text_color(0, 0, 255)
        self.set_font('Arial', 'U', 12)
        self.cell(w, h, url, 0, 1, '', False, url)

pdf = PDF()
pdf.add_page()

# Adding a chapter
pdf.chapter_title('Introduction')
pdf.chapter_body('This PDF contains an internal and an external hyperlink. Please check the next page for the internal link.')

# Adding an external hyperlink
pdf.set_xy(10, 50)
pdf.add_hyperlink(10, 50, 100, 10, 'https://www.python.org')

# Adding a page which will be the target of the internal link
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'This is the target of the internal link.', 0, 1)

# Adding an internal hyperlink to the first page
pdf.add_link()
link = pdf.add_link()
pdf.set_link(link, page=2)
pdf.set_xy(10, 60)
pdf.set_font('Arial', 'U', 12)
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 10, 'Go to Page 2', 0, 1, '', False, link)

pdf.output('./tmp/hyperlinks_pdf.pdf')