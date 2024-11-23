from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the PDF
pdf.set_font("Arial", size=12)

# Add a cell with text
pdf.cell(200, 10, "PDF files can contain text information, including fonts, sizes, and styles.", 0, 1, 'C')

# Save the pdf with name .tmp/pdf_file_1.pdf
pdf.output("./tmp/pdf_file_1.pdf")