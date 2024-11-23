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

    def add_markup_and_review_tools(self, description):
        self.markup_and_review_tools = description

# Create a PDF file with metadata, geospatial data, and Markup and Review Tools feature
pdf = PDFWithMetadata()
pdf.set_metadata(author='John Doe', title='Sample PDF with Metadata', keywords='PDF, Metadata, Python', creation_date='2021-09-30')
pdf.add_geospatial_data(location='Coordinates: 40.7128° N, 74.0060° W')
pdf.add_markup_and_review_tools(description='PDF files provide markup and review tools for collaborative editing, feedback, and annotation workflows.')

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "This is a PDF file with metadata, geospatial data, and Markup and Review Tools feature", 0, 1, 'C')
pdf.cell(200, 10, pdf.location, 0, 1, 'C')
pdf.cell(200, 10, pdf.markup_and_review_tools, 0, 1, 'C')

output_file = "./tmp/sample_pdf_with_metadata_geospatial_data_and_markup_review_tools.pdf"
pdf.output(output_file)