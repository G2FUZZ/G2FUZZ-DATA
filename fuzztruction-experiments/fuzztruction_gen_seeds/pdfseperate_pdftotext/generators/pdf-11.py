from fpdf import FPDF
import os

# Ensure the tmp directory exists
os.makedirs("./tmp/", exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document Structure and Metadata Example', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set metadata
pdf.set_title('Document Title')
pdf.set_author('Author Name')
pdf.set_subject('Subject of the Document')
pdf.set_keywords('PDF, Python, Metadata, Example')

# Add a body
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, 'This document demonstrates how to add structure and metadata to a PDF using Python.', ln=True)

# Save the pdf with name .pdf
pdf_file_path = './tmp/document_with_metadata.pdf'
pdf.output(pdf_file_path)

print(f'PDF file has been saved: {pdf_file_path}')