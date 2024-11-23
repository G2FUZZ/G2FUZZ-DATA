from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font for the file
pdf.set_font("Arial", size=12)

# Adding text to the file
pdf.cell(200, 10, "PDF Compression Example", 0, 1, "C")
pdf.cell(200, 10, "PDF files support compression algorithms to reduce file size without compromising quality.", 0, 1, "C")

# Save the file
output_path = "./tmp/compressed_pdf_example.pdf"
pdf.output(output_path)