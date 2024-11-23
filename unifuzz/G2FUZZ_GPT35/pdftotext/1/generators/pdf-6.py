from reportlab.pdfgen import canvas

# Create a PDF file with form fields
def create_pdf_with_form_fields(file_name):
    c = canvas.Canvas(file_name)
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

    c.save()

# Generate a PDF file with form fields
file_name = "./tmp/form_fields_example.pdf"
create_pdf_with_form_fields(file_name)
print(f"PDF file with form fields generated: {file_name}")