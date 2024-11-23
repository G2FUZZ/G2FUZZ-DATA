from fpdf import FPDF

class PDFWithMetadata(FPDF):
    def set_metadata(self, author, title, keywords, creation_date):
        self.set_author(author)
        self.set_title(title)
        self.set_keywords(keywords)
        self.set_creation_date(creation_date)

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

# Create a PDF file with metadata
pdf = PDFWithMetadata()
pdf.set_metadata(author='John Doe', title='Sample PDF with Metadata', keywords='PDF, Metadata, Python', creation_date='2021-09-30')

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "This is a PDF file with metadata", 0, 1, 'C')

output_file = "./tmp/sample_pdf_with_metadata.pdf"
pdf.output(output_file)