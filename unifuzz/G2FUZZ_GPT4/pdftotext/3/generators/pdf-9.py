from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
text = """9. Compression: PDF format supports efficient compression algorithms, enabling documents to be compressed to smaller sizes for easier sharing and storage, without significantly compromising quality."""
pdf.multi_cell(0, 10, text)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the pdf with name .pdf
pdf_file_path = './tmp/compression_info.pdf'
pdf.output(pdf_file_path)

print(f"PDF file has been successfully saved to {pdf_file_path}")