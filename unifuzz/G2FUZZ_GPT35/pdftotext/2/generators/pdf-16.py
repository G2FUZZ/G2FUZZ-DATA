from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add content to the PDF
pdf.set_font("Arial", style='', size=12)
pdf.cell(200, 10, "Digital Signatures in PDF files", ln=True, align='C')
pdf.ln(10)
pdf.multi_cell(0, 10, "PDF files support digital signatures for authentication and verification of document integrity.")
pdf.ln(10)
pdf.multi_cell(0, 10, "Digital Rights Management (DRM): PDF files can incorporate DRM controls to manage and protect copyrighted content.")

# Save the PDF file
file_path = "./tmp/digital_signatures_drm.pdf"
pdf.output(name=file_path)