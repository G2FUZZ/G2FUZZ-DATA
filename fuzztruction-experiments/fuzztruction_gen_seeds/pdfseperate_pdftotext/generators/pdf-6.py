from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, DictionaryObject, ArrayObject, NumberObject, TextStringObject

# Create a PDF file
output_file = "./tmp/annotated_pdf.pdf"
c = canvas.Canvas(output_file, pagesize=letter)
c.drawString(100, 750, "Hello, this is a PDF with annotations.")
c.save()

# Function to add annotation
def add_annotation_to_pdf(input_pdf_path, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    page = reader.pages[0]
    
    # Define the annotation to be added
    # Note: Adjust the Rect values to position your annotation as needed
    new_annotation = DictionaryObject({
        NameObject("/Type"): NameObject("/Annot"),
        NameObject("/Subtype"): NameObject("/Text"),
        NameObject("/Rect"): ArrayObject([NumberObject(100), NumberObject(700), NumberObject(150), NumberObject(720)]),
        NameObject("/Contents"): TextStringObject("This is an annotation."),
        NameObject("/C"): ArrayObject([NumberObject(1), NumberObject(0), NumberObject(0)]),  # Red color
        NameObject("/Open"): NameObject("true")
    })

    if "/Annots" in page:
        page["/Annots"].append(new_annotation)
    else:
        page[NameObject("/Annots")] = ArrayObject([new_annotation])

    for page in reader.pages:
        writer.add_page(page)
    
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

# Add annotation to the existing PDF
add_annotation_to_pdf(output_file, "./tmp/annotated_pdf_with_annotation.pdf")