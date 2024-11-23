from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter  # Updated import statement
import io

# Create a simple PDF with ReportLab
packet = io.BytesIO()
c = canvas.Canvas(packet, pagesize=letter)
c.drawString(100, 750, "3D Model Embedding Example")
c.save()

# Move to the beginning of the StringIO buffer
packet.seek(0)

# Create a new PDF with PyPDF2
new_pdf = PdfReader(packet)  # Updated to use PdfReader
output = PdfWriter()  # Ensure this is updated to PdfWriter if necessary
page = new_pdf.pages[0]  # Updated to access pages for PdfReader
output.add_page(page)  # Updated method to add a page

# Embed the 3D U3D model into the PDF
# This step assumes that the U3D file is named 'example.u3d' and is located in the current directory
u3d_file_path = './example.u3d'
u3d_annotation = {
    'filename': u3d_file_path,
    'page': 0,
    'pos': [100, 100, 200, 200],  # Position and size of the 3D model viewport: [xLL, yLL, width, height]
    '3DD': {
        # Dictionary for 3D settings (optional)
        # Refer to Adobe PDF Specification for more options
    }
}

# Note: As of my last update, PyPDF2 or ReportLab does not support direct embedding of 3D models.
# You would need to manually add the 3D model to the PDF, potentially using a lower-level library or tool
# that supports embedding U3D content directly into PDF files, such as LaTeX with the media9 package or
# using a PDF editor that supports 3D embeddings manually after PDF creation.

# Save the PDF to a file
output_stream = open('./tmp/3d_model_embedded.pdf', 'wb')
output.write(output_stream)
output_stream.close()