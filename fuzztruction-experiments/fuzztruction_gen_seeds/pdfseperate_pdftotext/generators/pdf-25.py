from fpdf import FPDF
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF creation class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Features Compilation', 0, 1, 'C')

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

# Instantiating PDF object
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Adding content for Cross-Platform Compatibility
title1 = "Feature 13: Cross-Platform Compatibility"
body1 = ("Cross-Platform Compatibility: Created as a way to present documents consistently "
         "across multiple devices and operating systems, ensuring they look and function the "
         "same way everywhere.")
pdf.chapter_title(title1)
pdf.chapter_body(body1)

# Adding content for Optical Character Recognition (OCR)
title2 = "Feature 12: Optical Character Recognition (OCR)"
body2 = ("Optical Character Recognition (OCR): PDFs can contain text recognized through OCR "
         "from scanned documents, making it possible to search and edit previously unsearchable "
         "documents.")
pdf.chapter_title(title2)
pdf.chapter_body(body2)

# Saving the PDF to a file
pdf_file_path = os.path.join(output_dir, 'features_compilation.pdf')
pdf.output(pdf_file_path)

print(f"PDF file has been saved to: {pdf_file_path}")