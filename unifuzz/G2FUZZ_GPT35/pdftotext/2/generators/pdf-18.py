from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

# Create a PDF file with interactive elements, including a 3D Model and Measurement Tools
filename = "./tmp/interactive_pdf_with_3d_and_measurement_tools.pdf"
c = canvas.Canvas(filename, pagesize=letter)
c.drawString(100, 700, "Click here to open Google")
c.linkURL("http://www.google.com", (100, 700, 200, 715), relative=1, thickness=1, color=blue)
c.bookmarkPage("Google", fit="XYZ", top=700)

# Embed a 3D Model
c.drawString(100, 600, "Click here to interact with a 3D Model")
c.linkURL("3dmodel.pdf", (100, 600, 300, 615), relative=1, thickness=1, color=blue)

# Measurement Tools
c.drawString(100, 500, "Measurement Tools: Scaling and Dimensioning objects")
c.linkURL("measurement_tools.pdf", (100, 500, 350, 515), relative=1, thickness=1, color=blue)

# Save the PDF file
c.showPage()
c.save()

print(f"PDF file with interactive elements, a 3D Model, and Measurement Tools generated and saved as '{filename}'")