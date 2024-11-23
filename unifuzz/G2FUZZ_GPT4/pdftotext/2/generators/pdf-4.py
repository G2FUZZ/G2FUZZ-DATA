from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader

# Create a PDF file with the given content
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Security Features', 0, 1, 'C')

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

pdf = PDF()
pdf.add_page()
pdf.chapter_title('5. Security Features')
pdf.chapter_body('PDF files can incorporate robust security features, including password protection, encryption, digital signatures, and rights management, to control access and modifications.')

# Save the PDF to a file
pdf_file_path = './tmp/security_features.pdf'
pdf.output(pdf_file_path)

# Add password protection to the PDF
password = "secret"
writer = PdfWriter()

reader = PdfReader(pdf_file_path)
writer.append_pages_from_reader(reader)

writer.encrypt(password)
protected_pdf_path = './tmp/protected_security_features.pdf'
with open(protected_pdf_path, 'wb') as f_out:
    writer.write(f_out)

print(f"PDF with security features created and password protected at: {protected_pdf_path}")