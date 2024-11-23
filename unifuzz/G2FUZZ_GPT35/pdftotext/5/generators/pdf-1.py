from fpdf import FPDF

# Create PDF file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "PDF files can contain text data, which can be easily searched, selected, and copied.", ln=True)

# Save PDF file
pdf_output = "./tmp/pdf_with_text.pdf"
pdf.output(pdf_output)