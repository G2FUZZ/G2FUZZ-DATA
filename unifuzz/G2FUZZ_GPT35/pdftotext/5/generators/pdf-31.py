import os
from fpdf import FPDF

class PDFWithText(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Header of the Page', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDFWithText()
pdf.set_auto_page_break(auto=True, margin=15)

# Add first page
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'First Page', 0, 1, 'C')

# Add text content
pdf.set_font('Arial', '', 12)
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
pdf.multi_cell(0, 10, lorem_ipsum)

# Add second page
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Second Page', 0, 1, 'C')

# Add a table
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Table Example:', 0, 1)
pdf.set_fill_color(200, 220, 255)
pdf.cell(40, 10, 'Column 1', 1, 0, 'C', 1)
pdf.cell(40, 10, 'Column 2', 1, 1, 'C', 1)
for i in range(1, 11):
    pdf.cell(40, 10, f'Row {i}, Col 1', 1, 0, 'C')
    pdf.cell(40, 10, f'Row {i}, Col 2', 1, 1, 'C')

# Save the PDF file
pdf_output_path = "./tmp/complex_pdf.pdf"
pdf.output(name=pdf_output_path, dest='F')