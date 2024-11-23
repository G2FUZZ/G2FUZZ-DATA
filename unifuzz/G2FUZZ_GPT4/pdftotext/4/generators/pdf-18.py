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

            # Manually add a simple text annotation to the page
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

# Step 3: Apply Digital Rights Management (DRM)
def apply_drm(pdf_path):
    output_path = pdf_path.replace('.pdf', '_drm.pdf')
    
    with open(pdf_path, "rb") as inFile, open(output_path, "wb") as outFile:
        reader = PyPDF2.PdfReader(inFile)
        writer = PyPDF2.PdfWriter()

        # Set document metadata
        writer.add_metadata({
            '/Author': 'Author Name',
            '/Title': 'Document with DRM',
        })
        # Encrypt the document with an owner password and enable 128-bit encryption
        writer.encrypt(user_pwd='', owner_password='owner_password', use_128bit=True)

        for page in reader.pages:
            writer.add_page(page)

        writer.write(outFile)

    return output_path

# Step 4: Generate PDF, add annotation, and apply DRM
pdf_path = './tmp/sample.pdf'
annotated_pdf_path = './tmp/sample_annotated.pdf'
drm_pdf_path = './tmp/sample_drm.pdf'

# Create directories if not present
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

create_pdf(pdf_path)
add_annotation(pdf_path)
apply_drm(annotated_pdf_path)

print(f"PDF with annotations saved as: {annotated_pdf_path}")
print(f"PDF with DRM applied saved as: {drm_pdf_path}")