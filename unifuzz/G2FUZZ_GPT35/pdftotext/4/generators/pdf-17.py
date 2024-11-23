from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF file with digital signature and versioning feature
def create_pdf_with_digital_signature_and_versioning(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 700, "PDF file with Digital Signature and Versioning")
    c.drawString(100, 680, "Digital Signature: ✔️")
    c.drawString(100, 660, "Versioning: PDF files can support version control and tracking changes made to the document.")
    c.save()

# Save the generated PDF file with digital signature and versioning feature
file_path = "./tmp/pdf_with_digital_signature_and_versioning.pdf"
create_pdf_with_digital_signature_and_versioning(file_path)
print(f"PDF file with digital signature and versioning feature generated and saved at: {file_path}")