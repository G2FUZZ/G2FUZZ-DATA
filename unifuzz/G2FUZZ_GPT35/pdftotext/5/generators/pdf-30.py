from fpdf import FPDF
import os

class AdvancedPDFGenerator(FPDF):
    def add_image(self, x, y, w, h, image_path):
        if os.path.exists(image_path):
            self.image(image_path, x, y, w, h)
        else:
            print(f"Error: Image file '{image_path}' not found.")

    def add_table(self, header, data, col_width=40):
        for item in header:
            self.cell(col_width, 10, item, border=1)
        self.ln()
        for row in data:
            for item in row:
                self.cell(col_width, 10, item, border=1)
            self.ln()

    def header(self):
        self.set_font("Arial", style='B', size=12)
        self.cell(0, 10, "Header Section", 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", style='I', size=8)
        self.cell(0, 10, "Page %s" % self.page_no(), 0, 0, 'C')

pdf = AdvancedPDFGenerator()
pdf.add_page()

# Adding an image to the PDF
image_path = 'full/path/to/image.jpg'  # Provide the full path to the image file
pdf.add_image(10, 10, 40, 40, image_path)

# Adding a table to the PDF
header = ['Name', 'Age', 'Country']
data = [
    ['Alice', '25', 'USA'],
    ['Bob', '30', 'Canada'],
    ['Eve', '22', 'UK']
]
pdf.add_table(header, data)

# Adding custom header and footer
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(left=15, top=30, right=15)
pdf.add_page()
pdf.cell(200, 10, "Content of the second page", ln=True)

pdf.output("./tmp/advanced_pdf_with_images_tables_headers_footer.pdf")