from fpdf import FPDF
import os

# Create a directory to save PDF files if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF class with metadata and additional features
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document with Metadata and Bounding Box Support', 0, 1, 'C')

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

    # Drawing a bounding box
    def add_bounding_box(self):
        self.set_fill_color(220, 220, 220) # Light gray background
        self.rect(10, 100, 190, 60, 'DF') # x, y, width, height, style

    # Demonstrating clipping path with text (simple emulation)
    def add_clipping_path_text(self):
        self.set_font('Arial', '', 12)
        self.set_xy(15, 105)
        self.cell(0, 10, 'This text is within the bounding box.')

# Create PDF object
pdf = PDF()
pdf.add_page()

# Set metadata
pdf.set_title('Sample PDF with Bounding Box and Clipping Path Support')
pdf.set_author('John Doe')
pdf.set_subject('Advanced PDF Generation')
pdf.set_keywords('PDF, Python, Metadata, Bounding Box, Clipping Path')

# Add content
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, 'This PDF contains document metadata, including author, title, subject, keywords, and demonstrates bounding box and clipping path support.', ln=True)

# Adding Bounding Box and Clipping Path Support description
pdf.chapter_title('14. Bounding Box and Clipping Path Support')
bounding_box_description = "PDFs support bounding boxes for graphics and text, as well as clipping paths for images, allowing for precise control over content display and print output."
pdf.chapter_body(bounding_box_description)

# Adding a bounding box and clipping path text
pdf.add_bounding_box()
pdf.add_clipping_path_text()

# Save the PDF to a file
pdf_file_path = os.path.join(output_dir, "document_with_advanced_features.pdf")
pdf.output(pdf_file_path)

print(f"PDF with metadata and additional features has been created: {pdf_file_path}")