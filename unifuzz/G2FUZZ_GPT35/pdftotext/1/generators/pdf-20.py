from fpdf import FPDF
import os

class PDFWithImageAndGeospatialData(FPDF):
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

    def add_geospatial_data(self, geospatial_data):
        self.set_xy(10, 50)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, f'Geospatial Data: {geospatial_data}')

# Create PDF with image and geospatial data
pdf = PDFWithImageAndGeospatialData()
pdf.add_page()

# Provide the full path to the image file
image_path = '/full/path/to/image.jpg'
pdf.add_image(image_path)

# Add geospatial data to the PDF
geospatial_data = "PDF files can store geospatial data and maps for location-based information."
pdf.add_geospatial_data(geospatial_data)

pdf.output('./tmp/image_geospatial_pdf.pdf')