from fpdf import FPDF, HTMLMixin
from PyPDF2 import PdfReader, PdfWriter

class PDF(FPDF, HTMLMixin):
    def header(self):
        # This method could be used to add a watermark or header
        self.set_font('Arial', 'B', 50)
        self.set_text_color(225, 225, 225)
        self.cell(0, 0, 'DRAFT', align='C', ln=True)
        self.ln(20)  # Move below the watermark for the next content

    def footer(self):
        # This method could be used to add a footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_pdf_with_hyperlink():
    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add a hyperlink
    html = """<a href="https://www.example.com">Visit Example.com</a>"""
    pdf.write_html(html)

    # Save the pdf with name .pdf
    pdf.output("./tmp/hyperlinked_watermarked_document.pdf")

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Extracts pages from a PDF and creates a new PDF with those pages.
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to the output PDF file.
    :param start_page: The first page to extract (0-indexed).
    :param end_page: The last page to extract (0-indexed).
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Extract specified pages and add them to the writer
    for i in range(start_page, end_page + 1):
        writer.add_page(reader.pages[i])

    # Write to a new PDF file
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

# Create a PDF with a hyperlink
create_pdf_with_hyperlink()

# Example usage of the page extraction feature
# Extract pages 0 to 0 (effectively the first page) from the created PDF
extract_pages("./tmp/hyperlinked_watermarked_document.pdf", "./tmp/extracted_pages.pdf", 0, 0)