from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the pdf
pdf.set_font("Arial", size=12)

# Add a page title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Features of PDF Files", 0, 1, 'C')
pdf.ln(10)

# Add text content
pdf.set_font("Arial", size=12)
text = """
1. Text: PDF files can contain text data in a structured format.
"""
pdf.multi_cell(0, 10, text)

# Save the pdf with file name
pdf_output = "./tmp/pdf_features.pdf"
pdf.output(name=pdf_output)

print("PDF file generated successfully with features!")