from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF with Interactive Elements', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_link(self, url, text):
        self.set_text_color(0, 0, 255)
        self.set_font('Arial', 'U', 12)
        self.write(10, text, url)


# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

pdf = PDF()
pdf.add_page()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.chapter_title('Interactive Element: Hyperlink')
pdf.chapter_body('This PDF includes an interactive hyperlink element. You can click on the link below to visit a webpage.')

# Add a hyperlink
pdf.add_link('https://www.example.com', 'Visit Example.com')

pdf.output('./tmp/interactive_elements.pdf')