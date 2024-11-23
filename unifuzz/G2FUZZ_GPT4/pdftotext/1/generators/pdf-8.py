from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
from PyPDF2.generic import NameObject, DictionaryObject, ArrayObject, NumberObject, TextStringObject

# Create a simple PDF file
pdf_path = './tmp/annotated_pdf.pdf'
can = canvas.Canvas(pdf_path, pagesize=letter)
can.drawString(100, 750, "Hello, this PDF includes an annotation.")
can.save()

# Function to add a text annotation to an existing PDF
def add_annotation(pdf_path):
    # Open the PDF we just created
    with open(pdf_path, 'rb') as f_in:
        # Use PdfReader instead of PdfFileReader
        reader = PyPDF2.PdfReader(f_in)
        # Use PdfWriter instead of PdfFileWriter
        writer = PyPDF2.PdfWriter()
        
        # Copy all pages from the reader to the writer
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            
            # Define the annotation to be added
            # Note: The positions and sizes are arbitrary for demonstration
            annotation = DictionaryObject({
                NameObject("/Type"): NameObject("/Annot"),
                NameObject("/Subtype"): NameObject("/Text"),
                NameObject("/Rect"): ArrayObject([NumberObject(100), NumberObject(700), NumberObject(150), NumberObject(720)]),
                NameObject("/Contents"): TextStringObject("This is a text annotation"),
            })
            
            # Add annotation object to the page
            if "/Annots" in page:
                page["/Annots"].append(annotation)
            else:
                page[NameObject("/Annots")] = ArrayObject([annotation])
            
            writer.add_page(page)
        
        # Write the modified content to a new file
        with open('./tmp/annotated_pdf_with_comments.pdf', 'wb') as f_out:
            writer.write(f_out)

# Add the annotation
add_annotation(pdf_path)