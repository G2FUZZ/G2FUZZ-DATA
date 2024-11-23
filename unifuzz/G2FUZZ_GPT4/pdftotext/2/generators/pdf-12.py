from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Page Layout Control in PDFs', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create instance of FPDF class
# Page orientation: 'P' or 'L' (Portrait or Landscape), 'mm' (unit of measurement), 'A4' (format)
pdf = PDF(orientation='P', unit='mm', format='A4')

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
pdf.cell(0, 10, '13. Page Layout Control:', 0, 1)
pdf.multi_cell(0, 10, (
    "They offer precise control over page layout, margins, and orientation, ensuring that documents print and "
    "display exactly as intended."
))

# Save the pdf with name .pdf
pdf.output("./tmp/page_layout_control.pdf")