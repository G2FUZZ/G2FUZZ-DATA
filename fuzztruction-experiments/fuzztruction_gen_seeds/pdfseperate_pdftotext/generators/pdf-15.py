from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def header(self):
        # This method could be used to add a watermark or header
        self.set_font('Arial', 'B', 50)
        self.set_text_color(225, 225, 225)
        self.cell(0, 0, 'DRAFT', align='C', ln=True)
        self.ln(20)  # Move below the watermark for the next content

    def footer(self):
        # This method could be used to add a footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a hyperlink
html = """<a href="https://www.example.com">Visit Example.com</a>"""
pdf.write_html(html)

# Optionally add more text or elements here

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinked_watermarked_document.pdf")