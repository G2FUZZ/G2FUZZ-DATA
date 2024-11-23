from fpdf import FPDF
import os

# Create a directory to save PDF files if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF class with metadata
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document with Metadata', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create PDF object
pdf = PDF()
pdf.add_page()

# Set metadata
pdf.set_title('Sample PDF')
pdf.set_author('John Doe')
pdf.set_subject('PDF Generation')
pdf.set_keywords('PDF, Python, Metadata')

# Add content
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, 'This PDF contains document metadata, such as author, title, subject, and keywords.', ln=True)

# Save the PDF to a file
pdf_file_path = os.path.join(output_dir, "document_with_metadata.pdf")
pdf.output(pdf_file_path)

print(f"PDF with metadata has been created: {pdf_file_path}")