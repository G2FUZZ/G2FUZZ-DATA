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

# Redaction feature
pdf.set_text_color(255, 255, 255)  # Set text color to white for redaction
pdf.rect(20, 50, 160, 20, 'F')  # Draw a filled white rectangle for redaction

# Save the PDF file
pdf_output = "./tmp/compressed_pdf_with_redaction.pdf"
pdf.output(name=pdf_output)