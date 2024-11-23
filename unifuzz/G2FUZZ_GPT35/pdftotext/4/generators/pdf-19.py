from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add content to the PDF
pdf.cell(200, 10, "PDF Compression Example", 0, 1, "C")
pdf.ln(10)
pdf.multi_cell(0, 10, "PDF files can use various compression algorithms to reduce file size.")
pdf.ln(10)
pdf.multi_cell(0, 10, "Geospatial Data: PDF files can include geospatial data and maps.")

# Embedded Files
pdf.embedded_files = [{'filename': 'sample_file.txt', 'data': b'This is a sample embedded file.'}]

# Save the PDF file
pdf_output = "./tmp/compressed_pdf_example_with_geospatial_and_embedded_files.pdf"
pdf.output(name=pdf_output)