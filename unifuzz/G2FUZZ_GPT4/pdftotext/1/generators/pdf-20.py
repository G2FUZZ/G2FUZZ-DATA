from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features Including Compression and Watermarks', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF object
pdf = PDF()
pdf.add_page()

# Adding Compression feature description
compression_title = "11. Compression"
compression_body = ("PDF format supports efficient compression algorithms, reducing file size "
                    "without significantly compromising quality, facilitating easier storage and sharing.")
pdf.chapter_title(compression_title)
pdf.chapter_body(compression_body)

# Adding Watermarks feature description
watermarks_title = "5. Watermarks"
watermarks_body = ("PDFs can include watermarks, visible or invisible, used for branding or to indicate "
                   "the document's status (e.g., draft, confidential).")
pdf.chapter_title(watermarks_title)
pdf.chapter_body(watermarks_body)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the PDF into the ./tmp/ directory
pdf_file_path = './tmp/features_demo.pdf'
pdf.output(pdf_file_path)

print(f"PDF file has been saved to {pdf_file_path}")