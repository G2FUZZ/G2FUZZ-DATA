from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add a cell
pdf.cell(200, 10, txt = "Welcome to PDF generation with Metadata!", ln = True, align = 'C')

# Metadata
pdf.set_author('Author Name')
pdf.set_title('Document Title')
pdf.set_subject('Document Subject')
pdf.set_keywords('Python, PDF, Metadata, FPDF2')

# Save the pdf with name .pdf
pdf.output('./tmp/generated_pdf_with_metadata.pdf')

print("PDF generated successfully with metadata!")