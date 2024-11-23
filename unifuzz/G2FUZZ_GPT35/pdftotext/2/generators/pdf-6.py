from reportlab.pdfgen import canvas
from datetime import datetime

# Create a new PDF file
c = canvas.Canvas("./tmp/metadata_example.pdf")

# Set metadata
c.setAuthor("John Doe")
c.setCreator("My PDF Generator")
c.setTitle("Sample PDF with Metadata")
c.setSubject("Demonstrating metadata in PDF files")
c.setKeywords(["PDF", "metadata", "example"])

# Add content to the PDF
c.drawString(100, 700, "PDF file with metadata example")
c.drawString(100, 680, f"Creation Date: {datetime.now()}")

# Save the PDF file
c.save()