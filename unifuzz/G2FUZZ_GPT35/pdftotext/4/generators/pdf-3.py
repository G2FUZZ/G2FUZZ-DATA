from fpdf import FPDF

class PDFWithLinks(FPDF):
    def add_link(self, x, y, w, h, link):
        self.link(x, y, w, h, link)
    
    def set_text_link(self, link):
        self.add_link(self.get_x(), self.get_y(), 0, 0, link)

pdf = PDFWithLinks()
pdf.add_page()
pdf.set_font("Arial", size=12)

link = 'https://www.example.com'
pdf.set_text_color(0, 0, 255)
pdf.set_draw_color(0, 0, 255)
pdf.set_text_link(link)
pdf.cell(200, 10, "Click here to visit Example website", ln=True, link=link)

pdf.output("./tmp/link_example.pdf")