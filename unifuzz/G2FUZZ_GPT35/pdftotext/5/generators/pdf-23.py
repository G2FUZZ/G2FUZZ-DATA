from fpdf import FPDF
import zipfile
import os

class PDFWithMetadata(FPDF):
    def set_metadata(self, author, title, keywords, creation_date):
        self.set_author(author)
        self.set_title(title)
        self.set_keywords(keywords)
        self.set_creation_date(creation_date)

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def package_files(self, files_to_package, output_file):
        zip_file = zipfile.ZipFile(output_file, 'w')

        for file_path in files_to_package:
            if os.path.exists(file_path):
                file_name = os.path.basename(file_path)
                zip_file.write(file_path, file_name)
            else:
                print(f"File not found: {file_path}")

        zip_file.close()

# Create a PDF file with metadata and package functionality
pdf = PDFWithMetadata()
pdf.set_metadata(author='John Doe', title='Sample PDF with Metadata', keywords='PDF, Metadata, Python', creation_date='2021-09-30')

# Add content to the PDF
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "This is a PDF file with metadata and packaged files", 0, 1, 'C')

# Package additional files
files_to_package = ['./file1.txt', './images/image1.jpg']
output_pdf_with_package = "./tmp/sample_pdf_with_package.zip"
pdf.package_files(files_to_package, output_pdf_with_package)