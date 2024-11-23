from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# File path for the generated PDF
file_path = os.path.join(output_dir, "vector_graphics_example.pdf")

# Create a canvas
c = canvas.Canvas(file_path, pagesize=A4)

# Draw a rectangle (vector graphic)
c.rect(100, 700, 200, 100, stroke=1, fill=0)

# Draw a circle (vector graphic)
c.circle(300, 600, 50, stroke=1, fill=0)

# Add some text
c.setFont("Helvetica", 12)
c.drawString(100, 650, "Rectangle and Circle (Vector Graphics)")

# Save the PDF
c.showPage()
c.save()