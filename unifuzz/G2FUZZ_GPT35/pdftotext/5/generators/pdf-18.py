from fpdf import FPDF

class PDFWithMetadata(FPDF):
    def set_metadata(self, author, title, keywords, creation_date):
        self.set_author(author)
        self.set_title(title)
        self.set_keywords(keywords)
        self.set_creation_date(creation_date)

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def add_geospatial_data(self, location):
        self.location = location

# Create a PDF file with metadata and geospatial data
pdf = PDFWithMetadata()
pdf.set_metadata(author='John Doe', title='Sample PDF with Metadata', keywords='PDF, Metadata, Python', creation_date='2021-09-30')
pdf.add_geospatial_data(location='Coordinates: 40.7128° N, 74.0060° W')

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "This is a PDF file with metadata and geospatial data", 0, 1, 'C')
pdf.cell(200, 10, pdf.location, 0, 1, 'C')

output_file = "./tmp/sample_pdf_with_metadata_and_geospatial_data.pdf"
pdf.output(output_file)