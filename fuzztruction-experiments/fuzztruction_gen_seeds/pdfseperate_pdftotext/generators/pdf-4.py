from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color  # Import the Color class
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a basic PDF using FPDF (for demonstration, FPDF itself does not support interactive elements)
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Interactive PDF Example', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create a basic PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Unfortunately, this PDF does not support interactive elements due to limitations.", 0, 1)
pdf_file_path = './tmp/basic_pdf.pdf'
pdf.output(pdf_file_path)

# Create an interactive PDF using ReportLab
c = canvas.Canvas("./tmp/interactive_pdf.pdf", pagesize=letter)
c.drawString(100, 750, "ReportLab Interactive PDF Example")
c.drawString(100, 735, "This demonstrates basic PDF generation.")
c.drawString(100, 720, "Unfortunately, fully interactive features require more complex handling.")

# For demonstration, add a link (which is a basic form of interactivity)
# Use the Color class to define the color
link_color = Color(0, 0, 1)  # Define the color using the Color class
c.linkURL("https://www.example.com", (100, 700, 200, 720), relative=1, thickness=0.5, color=link_color)

c.save()

print("PDFs generated in ./tmp/")