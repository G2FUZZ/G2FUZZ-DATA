from fpdf import FPDF

class PDFVersion(FPDF):
    def __init__(self, pdf_version='1.4'):
        super().__init__()
        self.pdf_version = pdf_version
        self.redacted_areas = []

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF File with Formatting and Redaction', 0, 1, 'C')

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

    def add_redaction_area(self, x, y, width, height):
        self.redacted_areas.append((x, y, width, height))

    def redact_areas(self):
        for area in self.redacted_areas:
            self.set_fill_color(0, 0, 0)  # Fill with black color to redact
            self.rect(area[0], area[1], area[2], area[3], style='F')

    def output(self, name='', dest=''):
        self.output_version(name, dest, self.pdf_version)

    def output_version(self, name, dest, pdf_version):
        if name == '':
            name = 'doc.pdf'
        if dest == '':
            dest = 'F'
        FPDF.output(self, name, dest)

pdf = PDFVersion(pdf_version='1.6')
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.add_page()
pdf.chapter_title('Chapter 1: Introduction')
pdf.chapter_body('This is the introduction section of the PDF file with formatting.')

pdf.add_page()
pdf.chapter_title('Chapter 2: Main Content')
pdf.chapter_body('This is the main content section of the PDF file with formatting.')

# Redact an area on the second page
pdf.add_redaction_area(30, 50, 100, 20)
pdf.redact_areas()

pdf.output('./tmp/formatted_redacted_pdf_file.pdf')