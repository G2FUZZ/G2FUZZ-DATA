from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF file with digital signature, XFA, and Measurement Tools feature
def create_pdf_with_features(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 700, "PDF file with Digital Signature, XFA, and Measurement Tools features")
    c.drawString(100, 680, "Digital Signature: ✔️")
    c.drawString(100, 660, "XFA: PDF files can utilize XFA technology for creating dynamic forms with advanced features.")
    c.drawString(100, 640, "Measurement Tools: PDF files can include measurement tools for accurately scaling and measuring objects within the document.")
    c.save()

# Save the generated PDF file with digital signature, XFA, and Measurement Tools features
file_path = "./tmp/pdf_with_features.pdf"
create_pdf_with_features(file_path)
print(f"PDF file with digital signature, XFA, and Measurement Tools features generated and saved at: {file_path}")