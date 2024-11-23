from fpdf import FPDF

class PDFWithLinks(FPDF):

    def add_link(self, x, y, w, h, link):
        # Add a clickable link to the PDF
        self.link(x, y, w, h, link)

# Create a PDF file with a clickable link
pdf = PDFWithLinks()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Click here to visit Google", 0, 1, "C")
pdf.add_link(85, 15, 35, 10, "https://www.google.com")

# Save the PDF file
pdf.output("./tmp/clickable_link.pdf")