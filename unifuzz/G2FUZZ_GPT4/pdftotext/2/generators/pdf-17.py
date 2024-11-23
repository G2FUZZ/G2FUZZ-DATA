from fpdf import FPDF
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Text, Fonts, and Attachments Embedding', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_attachment(self, file_path):
        # Unfortunately, FPDF does not support embedding attachments in PDFs directly.
        # You would need to use a different library or manually add attachments to the PDF after creation.
        # This function is a placeholder to illustrate where and how attachment functionality would ideally be integrated.
        pass

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_title("Text, Fonts, and Attachments Embedding")

# Add a chapter for Text and Fonts Embedding
pdf.chapter_title("Chapter 1: Introduction to Fonts Embedding")
pdf.chapter_body("PDF files can encapsulate not only the textual content but also the specific fonts used, ensuring that documents appear the same on any device or software platform. This feature is crucial for preserving the document's intended appearance, regardless of where or how it's viewed. Embedding fonts within PDFs ensures that text is displayed consistently, maintaining the design and layout integrity of the document.")

# Add a chapter for Attachments
pdf.chapter_title("Chapter 2: Attachments")
pdf.chapter_body("PDFs can include other files as attachments within the document, allowing for the bundling of related documents and resources. This facilitates the distribution of comprehensive information packets that include supplementary materials like data sheets, terms and conditions, or other pertinent documents. However, incorporating attachments directly into PDFs requires features not supported by the FPDF library used in this script, necessitating alternative solutions or libraries.")

# Save the pdf file
pdf.output(f"{output_dir}text_fonts_and_attachments_embedding.pdf")