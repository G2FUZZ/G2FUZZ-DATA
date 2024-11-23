from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the tmp directory exists
output_directory = "./tmp/"
os.makedirs(output_directory, exist_ok=True)

# Define the file path
file_path = os.path.join(output_directory, "accessibility_features_extended.pdf")

# Create a PDF with ReportLab
c = canvas.Canvas(file_path, pagesize=letter)

# Add some content
c.drawString(72, 750, "Accessibility Features in PDF")
c.drawString(72, 735, "-----------------------------------")
c.drawString(72, 720, "1. Text-to-Speech: This PDF supports text-to-speech for users with visual impairments.")
c.drawString(72, 705, "2. Tagged PDFs: Content in this PDF is tagged for better screen reader support.")
c.drawString(72, 690, "3. Keyboard Shortcuts: Users can navigate this PDF using keyboard shortcuts.")
c.drawString(72, 675, "15. Non-destructive Editing: Some PDF editors offer non-destructive editing capabilities, allowing users to make changes to a PDF document without permanently altering the original content.")

# Note: Actual implementation of these features requires more than just adding text to a PDF.
# For example, creating a tagged PDF for real accessibility support would involve using a library
# that supports this feature directly, or manually tagging elements in a PDF creation tool that supports accessibility features.
# Similarly, text-to-speech and keyboard navigation are typically functionalities provided by the PDF reader or the user's operating system.

# Save the PDF
c.save()

print(f"PDF with additional accessibility features created at: {file_path}")