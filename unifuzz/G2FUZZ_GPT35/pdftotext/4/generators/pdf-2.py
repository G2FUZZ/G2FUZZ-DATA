from fpdf import FPDF
import os

class PDFWithImage(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def add_image(self, image_path, x, y, w, h):
        if os.path.exists(image_path):
            self.image(image_path, x, y, w, h)
        else:
            print(f"Error: Image file '{image_path}' not found.")

pdf = PDFWithImage()
pdf.add_page()
pdf.add_image('example.jpg', 10, 10, 100, 0)
pdf.output('./tmp/example_with_image.pdf')