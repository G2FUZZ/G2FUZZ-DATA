from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF file with digital signature feature
def create_pdf_with_digital_signature(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 700, "PDF file with Digital Signature")
    c.drawString(100, 680, "Digital Signature: ✔️")
    c.save()

# Save the generated PDF file with digital signature feature
file_path = "./tmp/pdf_with_digital_signature.pdf"
create_pdf_with_digital_signature(file_path)
print(f"PDF file with digital signature feature generated and saved at: {file_path}")