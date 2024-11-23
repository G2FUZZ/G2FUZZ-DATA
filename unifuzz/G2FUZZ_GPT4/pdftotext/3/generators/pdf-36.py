import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
c = canvas.Canvas(os.path.join(output_dir, "interactive_form_with_embedded_files.pdf"), pagesize=letter)

# [Your code for drawing on the canvas goes here...]

# Save the canvas
c.save()

print(f"Interactive PDF form with embedded files feature has been created at: {os.path.join(output_dir, 'interactive_form_with_embedded_files.pdf')}")