from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def set_metadata(self, title='', author='', subject='', keywords='', creation_date=''):
        self.title = title
        self.author = author
        self.subject = subject
        self.keywords = keywords
        self.creation_date = creation_date

# Create a PDF object
pdf = PDF()
pdf.set_metadata(title='Sample PDF', author='John Doe', subject='Metadata Example', keywords='PDF, Metadata', creation_date='2022-12-01')

# Add a page
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.cell(200, 10, 'PDF Metadata Example', 0, 1, 'C')

# Output the PDF file
pdf.output('./tmp/metadata_example.pdf')