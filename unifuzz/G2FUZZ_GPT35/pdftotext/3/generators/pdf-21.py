from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the document
pdf.set_font("Arial", size=12)

# Add a title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, "Digital Signatures, 3D Models, and Embedded Files in PDF Files", ln=True, align="C")
pdf.set_font("Arial", size=12)

# Add content
content = """
Digital Signatures:
PDF files can support digital signatures for authentication and integrity verification.

3D Models:
PDF files can include 3D models and interactive 3D elements.

Embedded Files:
PDF files can include attachments or embedded files such as other documents, spreadsheets, or multimedia content.
"""

pdf.multi_cell(0, 10, content)

# Save the PDF file
pdf.output("./tmp/digital_signatures_3d_models_embedded_files.pdf")