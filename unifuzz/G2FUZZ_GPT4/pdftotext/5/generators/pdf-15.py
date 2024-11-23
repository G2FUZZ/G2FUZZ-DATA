from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create a PDF with ReportLab
c = canvas.Canvas("./tmp/form_submission_feature.pdf", pagesize=letter)
c.drawString(100, 750, "Form Submission Feature PDF")
c.drawString(100, 735, "Fill out the form below and press submit.")

# Simulate a text field by drawing a rectangle
c.drawString(30, 50, "Name:")  # Label for the text field
c.rect(70, 45, 200, 20, stroke=1, fill=0)  # Draw the rectangle

c.save()