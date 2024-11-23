from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import pdfencrypt

# Create a PDF file with interactive form fields and DRM protection
def create_pdf_with_form_fields_and_drm(filename, user_password="", owner_password="", can_print=True, can_copy=True):
    c = canvas.Canvas(filename, encrypt=pdfencrypt.StandardEncryption(user_password, owner_password, canPrint=can_print, canCopy=can_copy))

    # Add form fields
    c.drawString(100, 700, "Name:")
    c.roundRect(200, 690, 200, 20, 4, stroke=1, fill=0)

    c.drawString(100, 650, "Gender:")
    c.rect(200, 645, 10, 10)
    c.drawString(220, 650, "Male")
    c.rect(270, 645, 10, 10)
    c.drawString(290, 650, "Female")

    c.drawString(100, 610, "Submit:")
    c.roundRect(200, 600, 50, 20, 4, stroke=1, fill=1)
    c.drawString(210, 605, "Submit")

    c.save()

# Generate PDF file with form fields and DRM protection
filename_with_drm = "./tmp/form_fields_with_drm.pdf"
create_pdf_with_form_fields_and_drm(filename_with_drm, user_password="user123", owner_password="owner456", can_print=False, can_copy=False)
print(f"PDF file with form fields and DRM protection generated successfully: {filename_with_drm}")