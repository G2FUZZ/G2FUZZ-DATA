from fpdf import FPDF, HTMLMixin

class MyPDF(FPDF, HTMLMixin):
    pass

# Create instance of FPDF class
pdf = MyPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Adding a cell
pdf.cell(200, 10, txt="Welcome to the PDF with hyperlinks!", ln=True)

# Adding a hyperlink
link = "http://www.example.com"
pdf.set_text_color(0, 0, 255)
pdf.write(5, "Click here to visit example.com", link)

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinks.pdf")