from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from reportlab.pdfbase.pdfdoc import PDFCatalog, PDFDictionary, PDFName, PDFString
from reportlab.pdfbase import pdfdoc

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# SVG content as a string
svg_content = """
<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.  
</svg>
"""

# Temporary SVG file path
temp_svg_file_path = './tmp/temp_svg_file.svg'

# Write the SVG content to a temporary file
with open(temp_svg_file_path, 'w') as svg_file:
    svg_file.write(svg_content)

# Convert SVG file to a ReportLab graphics object
svg_graphics = svg2rlg(temp_svg_file_path)

# Create a PDF file and draw the SVG on it
pdf_file_path = './tmp/svg_in_pdf_with_attachments.pdf'
c = canvas.Canvas(pdf_file_path, pagesize=A4)
renderPDF.draw(svg_graphics, c, 100, 700)  # Drawing the SVG onto the PDF canvas

# Optionally, attach a file to the PDF
attachment_file_path = './path/to/your/attachment.txt'  # Path to the file you want to attach
if os.path.exists(attachment_file_path):
    # Define the file attachment annotation
    attachment_annotation = PDFDictionary({
        PDFName('Type'): PDFName('Filespec'),
        PDFName('F'): PDFString(attachment_file_path),
        PDFName('UF'): PDFString(attachment_file_path),
        PDFName('Desc'): PDFString('Attached File Description'),
    })
    
    # Define the EmbeddedFiles entry in the PDF Catalog
    ef_entry = PDFDictionary({
        PDFName(attachment_file_path): attachment_annotation,
    })
    
    # Define the Names entry with the EmbeddedFiles entry
    names_dict = PDFDictionary({
        PDFName('EmbeddedFiles'): PDFDictionary({
            PDFName('Names'): [PDFString('AttachmentName'), ef_entry],
        })
    })
    
    # Add the Names dictionary to the PDF catalog of the document
    if not hasattr(c._doc, 'Catalog'):
        c._doc.Catalog = PDFCatalog()
    c._doc.Catalog.Names = names_dict

    # Note: This method sets the necessary entries, but full support for embedding and accessing
    # attachments may require additional steps or a different approach, especially for creating
    # attachments that can be opened directly from the PDF viewer.

c.save()

print(f"PDF with SVG and attachment has been saved to {pdf_file_path}")