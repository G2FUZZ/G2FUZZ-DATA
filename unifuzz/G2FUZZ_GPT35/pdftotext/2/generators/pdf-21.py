from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue

# Create a PDF file with interactive elements, including a 3D Model and Bookmarks
filename = "./tmp/interactive_pdf_with_3d_and_bookmarks.pdf"
c = canvas.Canvas(filename, pagesize=letter)

# Add Bookmark for Google page
c.drawString(100, 700, "Click here to open Google")
c.linkURL("http://www.google.com", (100, 700, 200, 715), relative=1, thickness=1, color=blue)
c.bookmarkPage("Google", fit="XYZ", top=700)

# Add Bookmark for 3D Model page
c.drawString(100, 600, "Click here to interact with a 3D Model")
c.linkURL("3dmodel.pdf", (100, 600, 300, 615), relative=1, thickness=1, color=blue)
c.bookmarkPage("3D Model", fit="XYZ", top=600)

# Add Bookmark for a specific section
c.drawString(100, 500, "Sample Section")
c.bookmarkPage("Sample Section", fit="XYZ", top=500)

# Save the PDF file
c.showPage()
c.save()

print(f"PDF file with interactive elements, a 3D Model, and Bookmarks generated and saved as '{filename}'")