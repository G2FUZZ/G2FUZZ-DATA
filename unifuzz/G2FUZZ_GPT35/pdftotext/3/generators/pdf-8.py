from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the document
pdf.set_font("Arial", size=12)

# Add a title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, "Digital Signatures in PDF Files", ln=True, align="C")
pdf.set_font("Arial", size=12)

# Add content
content = """
Digital Signatures:
PDF files can support digital signatures for authentication and integrity verification.
"""

pdf.multi_cell(0, 10, content)

# Save the PDF file
pdf.output("./tmp/digital_signatures.pdf")