from fpdf import FPDF
from pathlib import Path

# Ensure the tmp directory exists
Path("./tmp").mkdir(parents=True, exist_ok=True)

class PDFWithLinks(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF with Interactive Elements', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_hyperlink(self, x, y, w, h, url):
        self.set_xy(x, y)
        self.set_text_color(0, 0, 255)
        self.set_font('', 'U')
        self.cell(w, h, url, 0, 1, '', False, url)
        self.set_text_color(0)
        self.set_font('')

    def add_button(self, x, y, w, h, name):
        self.set_xy(x, y)
        self.set_fill_color(200, 220, 255)
        self.cell(w, h, name, 0, 1, 'C', 1)

# Create the PDF object
pdf = PDFWithLinks()

# Add a page
pdf.add_page()

# Adding a hyperlink
pdf.set_font("Arial", size=12)
pdf.add_hyperlink(10, 20, 100, 10, 'https://www.python.org')

# Adding a button (Note: This button is not interactive due to limitations with simple PDF generation)
pdf.add_button(10, 40, 30, 10, 'Button')

# Save the PDF to file
pdf.output('./tmp/interactive_pdf.pdf')