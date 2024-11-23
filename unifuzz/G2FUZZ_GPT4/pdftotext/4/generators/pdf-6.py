from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Define the path for saving the PDF
pdf_path = "./tmp/multi_layer_multimedia.pdf"

# Create a canvas to draw on
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter  # Unpack the width and height of the page

# Draw a title
c.setFont("Helvetica", 16)
c.drawString(100, height - 100, "Multi-layer and Multimedia Integration")

# Add some text to describe the multimedia content
c.setFont("Helvetica", 12)
c.drawString(100, height - 140, "This PDF includes links to multimedia content.")

# Here we would normally embed or link the multimedia files
# For demonstration, we'll just draw placeholders and a fake link

# Placeholder for a multimedia link (e.g., to an audio file)
c.drawString(100, height - 180, "Audio File: Click here to listen (fake link)")

# Placeholder for a 3D model link
c.drawString(100, height - 220, "3D Model: Click here to view (fake link)")

# Save the PDF
c.save()

print(f"PDF saved to {pdf_path}")