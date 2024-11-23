from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF File with Formatting', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.add_page()
pdf.chapter_title('Chapter 1: Introduction')
pdf.chapter_body('This is the introduction section of the PDF file with formatting.')

pdf.add_page()
pdf.chapter_title('Chapter 2: Main Content')
pdf.chapter_body('This is the main content section of the PDF file with formatting.')

pdf.output('./tmp/formatted_pdf_file.pdf')