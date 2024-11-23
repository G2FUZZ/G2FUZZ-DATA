from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Define the path for saving the PDF
pdf_path = "./tmp/multi_layer_multimedia_javascript.pdf"

# Create a canvas to draw on
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter  # Unpack the width and height of the page

# Draw a title
c.setFont("Helvetica", 16)
c.drawString(100, height - 100, "Multi-layer and Multimedia Integration")

# Add some text to describe the multimedia content
c.setFont("Helvetica", 12)
c.drawString(100, height - 140, "This PDF includes links to multimedia content including JavaScript.")

# Placeholder for a multimedia link (e.g., to an audio file)
c.drawString(100, height - 180, "Audio File: Click here to listen (fake link)")

# Placeholder for a 3D model link
c.drawString(100, height - 220, "3D Model: Click here to view (fake link)")

# Introduce JavaScript Integration feature
c.drawString(100, height - 260, "JavaScript Integration: Click here for dynamic content (fake link)")

# Here we'll add a simple piece of JavaScript to display a message when the PDF is opened
# Note: JavaScript actions in PDFs might not work in all viewers
c.bookmarkPage("page1")
c.addOutlineEntry("JavaScript demo", "page1", level=0, closed=True)
c.showOutline()

# Note: Adding JavaScript directly via ReportLab is not supported. This line is commented out as a placeholder.
# c.addJS("app.alert('Welcome to the interactive PDF!');")

# Save the PDF
c.save()

print(f"PDF saved to {pdf_path}")