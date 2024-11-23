from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF with Interactive Elements & VDP', 0, 1, 'C')

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
    
    def add_vdp_content(self, data):
        self.set_font('Arial', '', 12)
        for record in data:
            self.add_page()
            for field, value in record.items():
                self.cell(0, 10, f'{field}: {value}', 0, 1)
            self.ln(20)

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Sample data for VDP
data = [
    {'Name': 'John Doe', 'Event': 'Marathon', 'Year': '2023'},
    {'Name': 'Jane Smith', 'Event': 'Triathlon', 'Year': '2023'},
]

pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.add_page()
pdf.chapter_title('Interactive Element: Hyperlink & VDP')
pdf.chapter_body('This PDF includes an interactive hyperlink element. You can click on the link below to visit a webpage. Additionally, it demonstrates Variable Data Printing by dynamically inserting personalized content for different recipients.')

# Add a hyperlink
pdf.add_link('https://www.example.com', 'Visit Example.com')

# Add VDP content
pdf.add_vdp_content(data)

pdf.output('./tmp/interactive_vdp_elements.pdf')