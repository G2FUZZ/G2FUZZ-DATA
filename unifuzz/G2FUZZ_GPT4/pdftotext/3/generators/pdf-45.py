from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import pink, black, red, blue, green
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
pdf_path = os.path.join(output_dir, "enhanced_interactive_pdf.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter  # Keep the page size handy

# Draw a title and some lines and shapes
c.setFont("Helvetica", 20)
c.drawString(100, height - 50, "Enhanced Interactive PDF")
c.setFont("Helvetica", 12)
c.drawString(100, height - 100, "This PDF includes shapes, images, and form fields.")

# Draw some shapes
c.setStrokeColor(pink)
c.setFillColor(red)
c.rect(100, height - 200, 100, 50, fill=1)
c.setStrokeColor(black)
c.setFillColor(blue)
c.circle(150, height - 300, 40, fill=1)

# Add an image (ensure you have an image named 'example.jpg' in the output_dir)
image_path = os.path.join(output_dir, "example.jpg")
if os.path.exists(image_path):
    c.drawImage(image_path, 100, height - 400, width=200, height=150)
else:
    c.drawString(100, height - 350, "Image not found.")

# Add interactive form fields
from reportlab.lib.colors import magenta, pink, blue, green

# Text Field
form = c.acroForm
c.drawString(100, height - 450, "Your Name:")
form.textfield(name='txtName', tooltip='Name', x=180, y=height - 465, borderStyle='inset',
               borderColor=magenta, fillColor=pink, width=300, height=20,
               textColor=blue, forceBorder=True)

# CheckBox
c.drawString(100, height - 480, "Subscribe to Newsletter:")
form.checkbox(name='chkSubscribe', tooltip='Check to subscribe', x=250, y=height - 490,
              buttonStyle='check', borderColor=black, fillColor=green, textColor=blue,
              forceBorder=True)

# Save the current state and start a new page
c.showPage()

# Second page with text and a line
c.drawString(100, height - 50, "Second Page")
c.line(100, height - 60, width - 100, height - 60)

# Save the canvas
c.save()

print(f"Enhanced interactive PDF has been created at: {pdf_path}")