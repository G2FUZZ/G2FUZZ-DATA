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
    
    def batch_processing(self, task):
        if task == 'printing':
            print("Batch Processing: Printing PDF files...")
            # Add printing functionality here
        elif task == 'conversion':
            print("Batch Processing: Converting PDF files...")
            # Add conversion functionality here
        elif task == 'optimization':
            print("Batch Processing: Optimizing PDF files...")
            # Add optimization functionality here
        else:
            print("Batch Processing: Task not supported.")
    
pdf = PDFWithImage()
pdf.add_page()
pdf.add_image('example.jpg', 10, 10, 100, 0)
pdf.batch_processing('printing')
pdf.output('./tmp/example_with_image_and_batch_processing.pdf')