from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add a hyperlink
html = """<a href="https://www.example.com">Visit Example.com</a>"""
pdf.write_html(html)

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinked_document.pdf")