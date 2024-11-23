from fpdf import FPDF
import os

# Create a directory to save PDF files if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF class with additional features for handling images and tables
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Comprehensive Report with Advanced Layout', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)
        
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_table(self, header, data):
        self.set_font('Arial', 'B', 12)
        col_width = self.w / 4  # Adjusted for 4 columns
        for col in header:
            self.cell(col_width, 10, col, border=1)
        self.ln()
        self.set_font('Arial', '', 12)
        for row in data:
            for item in row:
                self.cell(col_width, 10, item, border=1)
            self.ln()

# Create PDF object
pdf = PDF()
pdf.add_page()

# Set metadata
pdf.set_title('Comprehensive Report with Advanced Features')
pdf.set_author('John Doe')
pdf.set_subject('Comprehensive Report Generation')
pdf.set_keywords('PDF, Python, Report, Images, Tables')

# Add a section with a different font
pdf.chapter_title('Section 1: Introduction')
pdf.chapter_body('This section introduces the comprehensive report generated with Python, demonstrating the inclusion of images, tables, and different font styles and sizes.')

# Add Image
pdf.chapter_title('Section 2: Image')
# Ensure the image file exists at the specified path or replace the path with an existing image file
# pdf.image('./path/to/your-image.jpg', x=10, y=pdf.get_y(), w=190)
pdf.ln(10)  # Add a line break after the image

# Add a table
header = ['Header 1', 'Header 2', 'Header 3']
data = [['Row 1 Col 1', 'Row 1 Col 2', 'Row 1 Col 3'],
        ['Row 2 Col 1', 'Row 2 Col 2', 'Row 2 Col 3'],
        ['Row 3 Col 1', 'Row 3 Col 2', 'Row 3 Col 3']]
pdf.chapter_title('Section 3: Table')
pdf.add_table(header, data)

# Save the PDF to a file
pdf_file_path = os.path.join(output_dir, "comprehensive_report.pdf")
pdf.output(pdf_file_path)

print(f"Comprehensive report with advanced layout features has been created: {pdf_file_path}")