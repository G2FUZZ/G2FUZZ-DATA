from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the text
pdf.set_font("Arial", size=12)

# Add a page
pdf.add_page()

# Set the content for the PDF
text = "PDF files can contain text content that can be searched, selected, and copied."

# Add a cell
pdf.cell(200, 10, txt=text, ln=True, align='L')

# Save the pdf with name .tmp/pdf_file.pdf
pdf.output("./tmp/pdf_file.pdf")