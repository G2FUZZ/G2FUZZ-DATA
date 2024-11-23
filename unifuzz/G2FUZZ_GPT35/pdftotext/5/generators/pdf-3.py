from fpdf import FPDF

class PDFWithHyperlinks(FPDF):
    def add_link(self, x, y, w, h, link):
        self.link(x, y, w, h, link)

pdf = PDFWithHyperlinks()
pdf.add_page()
pdf.set_font("Arial", size=12)

link = "https://www.example.com"
pdf.cell(200, 10, "Click here to visit Example Website", ln=True, link=link)

pdf.output("./tmp/clickable_hyperlink.pdf")