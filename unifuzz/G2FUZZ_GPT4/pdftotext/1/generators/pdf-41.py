from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import red, green, blue, black
import os

def mobile_optimized_canvas(cnv, mobile_optimized=True):
    if mobile_optimized:
        mobile_page_size = landscape(A4)
        cnv.setPageSize(mobile_page_size)

def add_graphics(c):
    # Drawing lines
    c.setStrokeColor(black)
    c.line(50, 750, 300, 750)

    # Drawing curves
    c.setStrokeColor(red)
    c.bezier(50, 600, 100, 650, 200, 550, 300, 600)

    # Drawing rectangles with different fills
    c.setStrokeColor(black)
    c.setFillColor(green)
    c.rect(350, 500, 200, 100, stroke=1, fill=1)

    # Drawing circles with different fills
    c.setFillColor(blue)
    c.circle(150, 400, 50, stroke=1, fill=1)

def add_text(c):
    # Adding a title with a larger font
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 780, "Complex PDF Structure Example")

    # Changing font color and adding more text
    c.setFillColor(black)
    c.setFont("Helvetica", 12)
    c.drawString(50, 730, "This is an example of drawing lines.")
    c.drawString(50, 580, "This is an example of drawing curves.")
    c.drawString(350, 480, "Rectangles and circles with fills.")

def add_images(c):
    # Assuming an image named 'example.jpg' is present in the 'output_dir'
    image_path = os.path.join(output_dir, "example.jpg")
    if os.path.exists(image_path):
        c.drawImage(image_path, 400, 650, width=150, height=100)
    else:
        print("Image file not found, skipping image embedding.")

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# File path for the generated PDF
file_path = os.path.join(output_dir, "complex_structure_example.pdf")

# Create a canvas
c = canvas.Canvas(file_path, pagesize=A4)

# Apply mobile optimization if needed
mobile_optimized_canvas(c, mobile_optimized=True)

# Add graphics to the PDF
add_graphics(c)

# Add text to the PDF
add_text(c)

# Add images to the PDF
add_images(c)

# Save the current page and start a new page
c.showPage()

# You can repeat the process (add_graphics, add_text, add_images) for the new page
# For simplicity, let's just add a simple text to indicate a new page
c.drawString(100, 700, "This is a new page in the PDF.")

# Save the PDF
c.save()

print("PDF generated successfully.")