from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def create_simple_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.setAuthor("Author Name")
    c.setTitle("Simple PDF Example")

    # Drawing some text for demonstration
    c.drawString(100, 750, "This text is visible.")
    c.drawString(100, 730, "This text is also visible.")

    # Add some text outside layers for reference
    c.drawString(100, 710, "This text is not on any layer and always visible.")

    c.save()

def create_combined_pdf(output_path):
    # Create individual PDFs that will be assembled
    create_simple_pdf('./tmp/simple_pdf_example1.pdf')
    create_simple_pdf('./tmp/simple_pdf_example2.pdf')
    
    # Initialize a PdfWriter object for the output PDF
    writer = PdfWriter()

    # Read the contents of each PDF file and add them to the output PDF
    for pdf_path in ['./tmp/simple_pdf_example1.pdf', './tmp/simple_pdf_example2.pdf']:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    # Write the assembled document to the specified output path
    with open(output_path, 'wb') as f_out:
        writer.write(f_out)

# Generate the combined PDF with Document Assembly feature
create_combined_pdf('./tmp/combined_pdf_example.pdf')