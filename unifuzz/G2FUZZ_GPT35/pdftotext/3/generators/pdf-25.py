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

# Set XML metadata
xml_metadata = """
<?xml version="1.0"?>
<metadata>
    <description>PDF files can include XML metadata for better integration with document management systems.</description>
</metadata>
"""

# Set metadata in the PDF
pdf.set_creator("Your Name")
pdf.set_author("Your Name")
pdf.set_title("PDF File with Metadata")
pdf.set_subject("PDF Metadata Example")
pdf.set_keywords("PDF, Metadata, fpdf")

# Save the pdf with name .tmp/pdf_file_with_metadata.pdf
pdf.output("./tmp/pdf_file_with_metadata.pdf")