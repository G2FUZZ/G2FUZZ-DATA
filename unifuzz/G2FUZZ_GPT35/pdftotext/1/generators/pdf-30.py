from fpdf import FPDF

class ComplexPDFGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Complex PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_custom_page(self, title, content):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)

    def add_bookmark(self, title, level=0, page_number=0):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Bookmark: ' + title, 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.set_link(page_number)
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, f'Level: {level}', 0, 1, 'C')

# Create a complex PDF with bookmarks, custom pages, and styling
complex_pdf = ComplexPDFGenerator()
complex_pdf.add_page()

# Adding custom pages with specific content
complex_pdf.add_custom_page('Introduction', 'This is the introduction page.')
complex_pdf.add_custom_page('Chapter 1', 'Content of Chapter 1 goes here.')
complex_pdf.add_custom_page('Chapter 2', 'Content of Chapter 2 goes here.')

# Adding bookmarks with different levels and linking to specific pages
complex_pdf.add_bookmark('Chapter 1', level=1, page_number=2)
complex_pdf.add_bookmark('Subsection A', level=2, page_number=3)
complex_pdf.add_bookmark('Subsection B', level=2, page_number=4)
complex_pdf.add_bookmark('Chapter 2', level=1, page_number=5)

# Output the complex PDF file
complex_pdf.output('./tmp/complex_pdf_with_bookmarks.pdf')