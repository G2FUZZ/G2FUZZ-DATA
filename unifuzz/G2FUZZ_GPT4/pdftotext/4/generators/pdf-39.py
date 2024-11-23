from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
import os

# Step 1: Create a PDF file with ReportLab
def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 750, "Hello, World!")
    c.save()

# Step 2: Add an annotation (basic example)
def add_annotation(pdf_path):
    output_path = pdf_path.replace('.pdf', '_annotated.pdf')
    
    with open(pdf_path, "rb") as inFile, open(output_path, "wb") as outFile:
        reader = PyPDF2.PdfReader(inFile)
        writer = PyPDF2.PdfWriter()

        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]

            # Manually add a simple text annotation to the page's '/Annots' array
            annotation = PyPDF2.generic.DictionaryObject({
                PyPDF2.generic.NameObject('/Type'): PyPDF2.generic.NameObject('/Annot'),
                PyPDF2.generic.NameObject('/Subtype'): PyPDF2.generic.NameObject('/Text'),
                PyPDF2.generic.NameObject('/Contents'): PyPDF2.generic.createStringObject('Sample Annotation Text'),
                PyPDF2.generic.NameObject('/Rect'): PyPDF2.generic.ArrayObject([
                    PyPDF2.generic.FloatObject(100),
                    PyPDF2.generic.FloatObject(750),
                    PyPDF2.generic.FloatObject(150),
                    PyPDF2.generic.FloatObject(770)
                ]),
                PyPDF2.generic.NameObject('/F'): PyPDF2.generic.NumberObject(4)
            })

            if '/Annots' in page:
                page['/Annots'].append(annotation)
            else:
                page[PyPDF2.generic.NameObject('/Annots')] = PyPDF2.generic.ArrayObject([annotation])

            writer.add_page(page)

        writer.write(outFile)

    return output_path

# Step 4: Watermark Detection
def detect_watermark(pdf_path):
    with open(pdf_path, "rb") as inFile:
        reader = PyPDF2.PdfReader(inFile)

        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            text = page.extract_text()
            # This is a simplistic check; in a real scenario, more sophisticated analysis would be needed
            if "Watermark" in text or "Do not copy" in text:
                print(f"Watermark or copy protection notice detected on page {pageNum + 1}.")
                return True
    print("No watermark detected.")
    return False

# Step 3: Generate PDF and add annotation
pdf_path = './tmp/sample.pdf'
annotated_pdf_path = './tmp/sample_annotated.pdf'

# Create directories if not present
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

create_pdf(pdf_path)
add_annotation(pdf_path)
detect_watermark(annotated_pdf_path)

print(f"PDF with annotations saved as: {annotated_pdf_path}")