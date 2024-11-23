from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

# Create a PDF file with interactive form fields
def create_pdf_with_form_fields(filename):
    c = canvas.Canvas(filename)
    
    # Add a text input field
    c.drawString(100, 700, "Name:")
    c.roundRect(200, 690, 200, 20, 4, stroke=1, fill=0)
    
    # Add a checkbox
    c.drawString(100, 650, "Gender:")
    c.rect(200, 645, 10, 10)
    c.drawString(220, 650, "Male")
    c.rect(270, 645, 10, 10)
    c.drawString(290, 650, "Female")
    
    # Add a submit button
    c.drawString(100, 610, "Submit:")
    c.roundRect(200, 600, 50, 20, 4, stroke=1, fill=1)
    c.drawString(210, 605, "Submit")
    
    c.save()

# Generate PDF file with form fields
filename = "./tmp/form_fields.pdf"
create_pdf_with_form_fields(filename)
print(f"PDF file with form fields generated successfully: {filename}")