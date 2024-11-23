from fpdf import FPDF
import os

class PDFWithImage(FPDF):
    def __init__(self, transition_effect=None):
        super().__init__()
        self.transition_effect = transition_effect

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document', 0, 1, 'C')

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

    def set_page_transition(self, transition_effect):
        self.set_display_mode('fullwidth')
        self.set_transition(transition_effect)

# Create PDF with image and set page transition
pdf = PDFWithImage(transition_effect=13)  # 13 is the page transition effect for a dissolve effect
pdf.add_page()

# Provide the full path to the image file
image_path = '/full/path/to/image.jpg'
pdf.add_image(image_path)

pdf.output('./tmp/image_pdf_with_transition.pdf')