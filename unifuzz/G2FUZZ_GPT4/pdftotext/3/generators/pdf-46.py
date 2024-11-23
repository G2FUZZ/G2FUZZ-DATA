from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, black, red, blue, green, Color
import os

# Define magenta using RGB values
magenta = Color(1, 0, 1)

# Create a directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to save the PDF
file_path = './tmp/digital_print_ready_with_repurposable_content_enhanced.pdf'

# Create a canvas
c = canvas.Canvas(file_path, pagesize=letter)
width, height = letter  # Get the default letter size

# Set a title and add some graphical content
c.setFont("Helvetica", 20)
c.drawString(72, height - 100, "Digital Print-Ready with Repurposable Content: Enhanced")

# Draw some shapes
c.setStrokeColor(pink)
c.setFillColor(red)
c.rect(72, height - 200, 100, 50, fill=1)
c.setStrokeColor(black)
c.setFillColor(blue)
c.circle(122, height - 300, 40, fill=1)

# Add an image (ensure you have an image named 'example.jpg' in the './tmp/' directory)
image_path = os.path.join('./tmp', "example.jpg")
if os.path.exists(image_path):
    c.drawImage(image_path, 72, height - 450, width=200, height=150)
else:
    c.drawString(72, height - 400, "Image not found.")

# Add interactive form fields
form = c.acroForm
c.drawString(72, height - 500, "Your Name:")
form.textfield(name='txtName', tooltip='Name', x=152, y=height - 515, borderStyle='inset',
               borderColor=magenta, fillColor=pink, width=300, height=20,
               textColor=blue, forceBorder=True)

c.drawString(72, height - 530, "Subscribe to Newsletter:")
form.checkbox(name='chkSubscribe', tooltip='Check to subscribe', x=222, y=height - 540,
              buttonStyle='check', borderColor=black, fillColor=green, textColor=blue,
              forceBorder=True)

# Save the current state and start a new page for additional text content
c.showPage()

text_content = """
Digital Print-Ready: PDFs can be optimized for printing, ensuring that the printed document matches the on-screen version
in terms of layout, colors, and fonts, making it ideal for professional print production.

Repurposable Content: PDF files can be structured to enable content reflow and repurposing, making it easier to adapt content for different screen sizes and devices, enhancing accessibility.
"""

# Add the repurposed text content on the second page
c.setFont("Helvetica", 12)
c.drawString(72, height - 72, text_content.strip())  # 72 points = 1 inch from the border

# Save the PDF
c.save()

print(f"Enhanced PDF file with graphical elements and interactive form fields has been saved to: {file_path}")