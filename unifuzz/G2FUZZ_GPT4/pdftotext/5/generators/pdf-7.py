from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import NameObject, DictionaryObject, ArrayObject, IndirectObject
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Step 1: Create a simple PDF with ReportLab
c = canvas.Canvas(os.path.join(output_dir, "annotated_pdf.pdf"))
c.drawString(100,750,"Hello, this PDF contains annotations.")
c.save()

# Step 2: Add annotation using PyPDF2
reader = PdfReader(os.path.join(output_dir, "annotated_pdf.pdf"))
writer = PdfWriter()

# Copy pages from reader to writer
num_pages = len(reader.pages)
for i in range(num_pages):
    writer.add_page(reader.pages[i])

# Define a text annotation
annotation = DictionaryObject({
    NameObject("/Type"): NameObject("/Annot"),
    NameObject("/Subtype"): NameObject("/Text"),
    NameObject("/Contents"): NameObject("(This is a text annotation)"),
    NameObject("/Rect"): ArrayObject([100, 700, 160, 730]),
    NameObject("/C"): ArrayObject([1, 0, 0]),
    NameObject("/Open"): NameObject("true")
})

# Add annotation to the first page
if "/Annots" in reader.pages[0]:
    reader.pages[0]["/Annots"].append(annotation)
else:
    reader.pages[0][NameObject("/Annots")] = ArrayObject([annotation])

# Write to a new file
with open(os.path.join(output_dir, "annotated_pdf_with_comments.pdf"), "wb") as f_out:
    writer.write(f_out)

print("PDF with annotations created successfully.")