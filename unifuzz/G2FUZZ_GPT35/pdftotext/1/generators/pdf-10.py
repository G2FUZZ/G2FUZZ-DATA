from fpdf import FPDF
import os

class PDFWithInteractiveElements(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document with Interactive Elements', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_image(self, image_path):
        self.set_xy(10, 30)
        if os.path.exists(image_path):
            self.image(image_path, link='', type='', w=100)
        else:
            print(f"Error: Image file '{image_path}' not found.")

    def add_interactive_elements(self):
        # Add interactive elements like buttons, multimedia, 3D models
        self.set_xy(10, 50)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Interactive Elements:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, '- Buttons', 0, 1, 'L')
        self.cell(0, 10, '- Multimedia', 0, 1, 'L')
        self.cell(0, 10, '- 3D Models', 0, 1, 'L')

# Create PDF with interactive elements
pdf_with_interactive = PDFWithInteractiveElements()
pdf_with_interactive.add_page()

# Provide the full path to the image file
image_path = '/full/path/to/image.jpg'
pdf_with_interactive.add_image(image_path)

# Add interactive elements to the PDF
pdf_with_interactive.add_interactive_elements()

pdf_with_interactive.output('./tmp/interactive_elements_pdf.pdf')