from fpdf import FPDF
import os

class PDFWithComplexStructures(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My Complex PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_custom_content(self):
        self.set_xy(10, 30)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Table of Contents:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, '1. Introduction', 0, 1, 'L')
        self.cell(0, 10, '2. Methodology', 0, 1, 'L')
        self.cell(0, 10, '3. Results', 0, 1, 'L')

    def add_bookmark(self, title, page_number):
        self.add_page()
        self.set_xy(10, 50)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Go to page {page_number}', 0, 1, 'L')
        self.add_link(title, page_number)

    def add_link(self, title, page_number):
        self.set_link(page=page_number, link='page' + str(page_number))

# Create PDF with complex structures
pdf_complex = PDFWithComplexStructures()
pdf_complex.add_page()

# Add custom content to the PDF
pdf_complex.add_custom_content()

# Add bookmarks with links to specific pages
pdf_complex.add_bookmark('Introduction', 2)
pdf_complex.add_bookmark('Methodology', 3)
pdf_complex.add_bookmark('Results', 4)

pdf_complex.output('./tmp/complex_pdf_structure.pdf')