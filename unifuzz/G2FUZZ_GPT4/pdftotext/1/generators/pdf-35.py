from fpdf import FPDF
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Image, Color, and Logical Structure Management in PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def color_management_section(self):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Color Management', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, 'PDFs support sophisticated color management systems, ensuring that colors are '
                                'represented accurately across different devices and print outputs.')

    def logical_structure_trees_section(self):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Logical Structure Trees', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, '5. Logical Structure Trees: This feature defines the hierarchy and relationship '
                                'between document elements like headings, paragraphs, tables, and footnotes, further '
                                'enhancing accessibility and document reflow capabilities on mobile devices.')

# Create instance of FPDF class
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Example of integrating an image into a PDF file.", ln=True)

# Assuming an image named 'example.jpg' exists in the current directory
image_path = 'example.jpg'  # Make sure to adjust this path to your image's path
if os.path.exists(image_path):
    pdf.image(image_path, x=10, y=30, w=100)
else:
    print(f"Error: The image '{image_path}' was not found. Please ensure it exists in the specified path.")

# Add Color Management section
pdf.color_management_section()

# Add Logical Structure Trees section
pdf.logical_structure_trees_section()

# Save the pdf with name .pdf
pdf_file_path = os.path.join(output_dir, 'Image_Color_Logical_Structure_PDF.pdf')
pdf.output(pdf_file_path)

print(f"PDF file has been created: {pdf_file_path}")