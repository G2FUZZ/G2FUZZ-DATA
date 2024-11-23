from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
from PyPDF2.generic import NameObject, DictionaryObject, ArrayObject, NumberObject, TextStringObject
from PyPDF2 import PdfReader, PdfWriter
from endesive import pdf
import os
from reportlab.pdfbase import pdfdoc

pdfdoc.PDFCatalog.OpenAction = '<</S /Launch /F (yourfile.pdf)>>'

# Create a simple PDF file
pdf_path = './tmp/annotated_pdf.pdf'
can = canvas.Canvas(pdf_path, pagesize=letter)
can.drawString(100, 750, "Hello, this PDF includes an annotation.")
# Standards Compliance and Validation: Adding metadata for PDF/A compliance
can.saveState()
can.setTitle("PDF with Annotation and Standards Compliance")
can.setAuthor("Author Name")
can.setSubject("PDF/A compliance")
can.setCreator("Your Application Name")
can.save()

# Function to add a text annotation to an existing PDF
def add_annotation(pdf_path):
    # Open the PDF we just created
    with open(pdf_path, 'rb') as f_in:
        reader = PdfReader(f_in)
        writer = PdfWriter()
        
        # Copy all pages from the reader to the writer
        for page in reader.pages:
            # Define the annotation to be added
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

# Additionally, apply a digital signature for further validation
def add_digital_certificate(input_pdf_path, output_pdf_path, cert_file, key_file):
    """
    Sign a PDF with a digital certificate.

    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path where the signed PDF will be saved.
    :param cert_file: Path to the signer's certificate (.pem file).
    :param key_file: Path to the signer's private key (.pem file).
    """
    # Check if the certificate and key files exist
    if not os.path.exists(cert_file):
        raise FileNotFoundError(f"The certificate file was not found: {cert_file}")
    if not os.path.exists(key_file):
        raise FileNotFoundError(f"The key file was not found: {key_file}")

    dct = {
        "sigflags": 3,
        "sigpage": 0,
        "sigbutton": True,
        "contact": "signer@example.com",
        "location": "Location",
        "signingdate": b"D:20230101000000+00'00'",
        "reason": "Signing the PDF",
        "certification_level": 1,
    }

    with open(cert_file, 'rb') as fcert, open(key_file, 'rb') as fkey:
        p12 = fcert.read()
        key = fkey.read()
        datau = open(input_pdf_path, 'rb').read()
        datas = pdf.cms.sign(datau, dct, p12, key, 'sha256')

        with open(output_pdf_path, 'wb') as fp:
            fp.write(datau)
            fp.write(datas)

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Add the annotation
add_annotation(pdf_path)

# Example usage of add_digital_certificate
# Ensure you replace 'path/to/your/certificate.pem' and 'path/to/your/private_key.pem'
# with the actual paths to your certificate and private key files.
try:
    add_digital_certificate(
        './tmp/annotated_pdf_with_comments.pdf',
        './tmp/signed_annotated_pdf_with_comments.pdf',
        'path/to/your/certificate.pem',  # Replace with your actual certificate path
        'path/to/your/private_key.pem'   # Replace with your actual key path
    )
except FileNotFoundError as e:
    print(e)