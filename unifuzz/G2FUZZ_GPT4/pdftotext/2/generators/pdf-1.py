from fpdf import FPDF
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Text and Fonts Embedding', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_title("Text and Fonts Embedding")

# Add a chapter
pdf.chapter_title("Chapter 1: Introduction to Fonts Embedding")
pdf.chapter_body("PDF files can encapsulate not only the textual content but also the specific fonts used, ensuring that documents appear the same on any device or software platform. This feature is crucial for preserving the document's intended appearance, regardless of where or how it's viewed. Embedding fonts within PDFs ensures that text is displayed consistently, maintaining the design and layout integrity of the document.")

# Save the pdf file
pdf.output(f"{output_dir}text_and_fonts_embedding.pdf")