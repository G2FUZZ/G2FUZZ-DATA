from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def create_self_contained_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.setAuthor("Author Name")
    c.setTitle("Self-contained PDF Example")

    # Embedding a font
    c.setFont("Helvetica", 12)

    # Drawing some text for demonstration
    c.drawString(100, 750, "This text is visible and uses an embedded font.")
    c.drawString(100, 730, "This text is also visible and uses an embedded font.")

    # Adding colors
    c.setFillColor(colors.red)
    c.drawString(100, 710, "This text is red.")
    
    c.setFillColor(colors.black)  # Resetting color to default
    c.drawString(100, 690, "This text is back to black and always visible.")

    # Including an image
    # Make sure to replace 'path_to_your_image.jpg' with an actual image path
    image_path = 'path_to_your_image.jpg'  # <-- Replace this with the actual path to your image
    if os.path.exists(image_path):
        c.drawImage(image_path, 100, 550, width=200, height=150, preserveAspectRatio=True, mask='auto')
    else:
        print(f"Error: The file {image_path} does not exist.")

    # Including a simple line drawing
    c.line(100, 540, 300, 540)

    # Closing the PDF object cleanly, and we're done.
    c.save()

create_self_contained_pdf('./tmp/self_contained_pdf_example.pdf')