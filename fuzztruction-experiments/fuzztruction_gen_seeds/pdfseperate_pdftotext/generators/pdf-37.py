from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('Arial', 'B', 50)
        self.set_text_color(225, 225, 225)
        self.cell(0, 0, 'DRAFT', align='C', ln=True)
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def add_page(self, orientation=''):
        # Call the superclass add_page method with only the supported parameter
        super().add_page(orientation=orientation)
        # Note: Removed unsupported parameters 'format' and 'same'
        # Additional setup or features you want to add when a new page is created can be done here

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a hyperlink
html = """<a href="https://www.example.com">Visit Example.com</a>"""
pdf.write_html(html)

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinked_watermarked_document_with_assembly_feature.pdf")

# Note: The explanation about adding Document Assembly features remains valid but is not directly applicable through FPDF's API.