from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
from PyPDF2.generic import NameObject, DictionaryObject, ArrayObject, DecodedStreamObject, NumberObject, TextStringObject

# Create a simple PDF file using reportlab
output_file_path = './tmp/annotated_pdf.pdf'
c = canvas.Canvas(output_file_path, pagesize=letter)
c.drawString(100, 750, "Hello, this PDF contains annotations.")
c.save()

# Now, open the created PDF to add annotations using PyPDF2
with open(output_file_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)  # Updated to PdfReader
    writer = PyPDF2.PdfWriter()  # Updated to PdfWriter

    # Get the number of pages in the original PDF
    num_pages = len(reader.pages)  # Updated to use len(reader.pages)

    # Iterate through every page to add an annotation
    for i in range(num_pages):
        page = reader.pages[i]  # Updated to use reader.pages[i]

        # Define the annotation to be added
        # Here, we add a text annotation
        annot = DictionaryObject()
        annot.update({
            NameObject("/Subtype"): NameObject("/Text"),
            NameObject("/T"): TextStringObject("Reviewer"),
            NameObject("/Rect"): ArrayObject([NumberObject(100), NumberObject(100), NumberObject(200), NumberObject(200)]),
            NameObject("/Contents"): TextStringObject("This is a comment.")
        })

        # Check if /Annots exists in the page, if not create it
        if "/Annots" in page:
            page["/Annots"].append(annot)
        else:
            page[NameObject("/Annots")] = ArrayObject([annot])

        writer.add_page(page)  # Updated to add_page

    # Save the annotated PDF
    with open(output_file_path, 'wb') as f_out:
        writer.write(f_out)

print("PDF with annotations has been created at './tmp/annotated_pdf.pdf'")