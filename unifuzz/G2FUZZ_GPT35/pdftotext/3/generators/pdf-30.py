from fpdf import FPDF
import os

class AdvancedPDF(FPDF):

    def add_page_with_header(self, title, header_text):
        self.add_page()
        self.set_font("Arial", style="B", size=16)
        self.cell(0, 10, title, 0, 1, "C")
        self.set_font("Arial", size=12)
        self.cell(0, 10, header_text, 0, 1, "C")
        self.ln(10)
    
    def add_table(self, headers, data):
        col_width = 40
        row_height = 10
        for header in headers:
            self.cell(col_width, row_height, header, border=1)
        self.ln(row_height)
        for row in data:
            for col in row:
                self.cell(col_width, row_height, col, border=1)
            self.ln(row_height)
    
    def add_image(self, img_path, w=0, h=0):
        if os.path.exists(img_path):
            self.image(img_path, w=w, h=h)
        else:
            print(f"Error: Image file '{img_path}' not found.")

# Create a PDF file with advanced features
pdf_advanced = AdvancedPDF()
pdf_advanced.add_page_with_header("Advanced PDF Example", "This PDF includes tables, images, and custom styling")
pdf_advanced.set_font("Arial", size=12)

# Add a table to the PDF
headers = ["Header 1", "Header 2", "Header 3", "Header 4"]
data = [
    ["Data 1", "Data 2", "Data 3", "Data 4"],
    ["Data 5", "Data 6", "Data 7", "Data 8"],
    ["Data 9", "Data 10", "Data 11", "Data 12"]
]
pdf_advanced.add_table(headers, data)

# Add an image to the PDF (provide the correct path to the image file)
image_path = "path/to/example.jpg"
pdf_advanced.add_image(image_path, w=100, h=100)

# Save the PDF file
pdf_advanced.output("./tmp/advanced_pdf_example.pdf")