from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
c = canvas.Canvas(os.path.join(output_dir, "interactive_form_with_articles.pdf"), pagesize=letter)
c.drawString(100, 750, "Interactive Form with Articles")

# Define an article with two threads in a single page document for demonstration
c.drawString(100, 700, "Article Start: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
c.drawString(100, 685, "Continues on page 2...")

# Save the current state and start a new page
c.showPage()
c.drawString(100, 750, "Article Continuation")
c.drawString(100, 700, "Continuation: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
c.drawString(100, 685, "End of Article.")

# Save the canvas
c.save()

print(f"Interactive PDF form with articles has been created at: {os.path.join(output_dir, 'interactive_form_with_articles.pdf')}")