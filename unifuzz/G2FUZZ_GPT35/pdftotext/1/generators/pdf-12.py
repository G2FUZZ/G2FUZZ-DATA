from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF file with form fields, Accessibility Features, and Compression
def create_pdf_with_all_features(file_name):
    c = canvas.Canvas(file_name, pagesize=letter, verbosity=0, encrypt=None)
    c.drawString(100, 700, "Please fill out the form:")
    c.drawString(100, 650, "Name:")
    c.drawString(100, 630, "Email:")
    c.drawString(100, 610, "Phone:")
    c.drawString(100, 590, "Address:")

    c.drawString(100, 550, "Comments:")
    c.rect(100, 500, 400, 50, stroke=1, fill=0)

    c.drawString(100, 450, "Signature:")
    c.rect(100, 400, 200, 50, stroke=1, fill=0)

    c.drawString(100, 350, "Date:")
    c.drawString(200, 350, "_______________")

    c.drawString(100, 300, "Accessibility Features:")
    c.drawString(200, 280, "PDF files can be created to meet accessibility standards for users with disabilities.")

    c.drawString(100, 250, "Compression:")
    c.drawString(200, 230, "PDF files can utilize various compression algorithms to reduce file size without losing quality.")

    c.save()

# Generate a PDF file with form fields, Accessibility Features, and Compression
file_name = "./tmp/form_fields_accessibility_compression_example.pdf"
create_pdf_with_all_features(file_name)
print(f"PDF file with form fields, Accessibility Features, and Compression generated: {file_name}")