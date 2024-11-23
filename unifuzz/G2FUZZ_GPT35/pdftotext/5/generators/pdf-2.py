import os
from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Specify the full path to the image file
image_path = "/full/path/to/image.jpg"

# Check if the image file exists
if os.path.exists(image_path):
    # Add the image to the PDF
    pdf.image(image_path, x=10, y=10, w=100)
else:
    print(f"Error: Image file '{image_path}' not found.")

# Save the PDF file
pdf_output_path = "./tmp/image_pdf.pdf"
pdf.output(name=pdf_output_path, dest='F')