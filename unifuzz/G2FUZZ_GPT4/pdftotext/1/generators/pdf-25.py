from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import os

# Function to adjust canvas size for mobile optimization
def mobile_optimized_canvas(cnv, mobile_optimized=True):
    if mobile_optimized:
        # Assuming a common mobile screen aspect ratio and adjusting the canvas size
        # Landscape orientation for better mobile viewing
        mobile_page_size = landscape(A4)
        cnv.setPageSize(mobile_page_size)

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# File path for the generated PDF
file_path = os.path.join(output_dir, "vector_graphics_optimized_example.pdf")

# Create a canvas
c = canvas.Canvas(file_path, pagesize=A4)

# Apply mobile optimization if needed
mobile_optimized_canvas(c, mobile_optimized=True)

# Draw a rectangle (vector graphic)
c.rect(100, 500, 200, 100, stroke=1, fill=0)

# Draw a circle (vector graphic)
c.circle(300, 400, 50, stroke=1, fill=0)

# Add some text
c.setFont("Helvetica", 12)
c.drawString(100, 550, "Rectangle and Circle (Vector Graphics)")

# Additional text for Mobile Optimization feature
c.drawString(100, 530, "9. Mobile Optimization: PDF files optimized for mobile devices.")

# Save the PDF
c.showPage()
c.save()