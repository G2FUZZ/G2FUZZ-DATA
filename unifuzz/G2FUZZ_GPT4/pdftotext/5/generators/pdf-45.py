from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path
file_path = os.path.join(output_dir, 'accessible_pdf_with_advanced_features.pdf')

# Create a PDF with reportlab
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF with Advanced Features Example")

# Adding accessibility features text
text_accessibility = "Accessibility Features: PDFs support accessibility features such as text-to-speech and the ability to reflow text, making documents more accessible to users with disabilities."
c.drawString(72, 720, text_accessibility)  # Starting at x=72, y=720

# Adding rich media and flash support text
text_rich_media = "13. Rich Media and Flash Support: While diminishing in usage, PDFs have historically supported embedding of Flash and other rich media content, allowing for dynamic and interactive elements within documents."
c.drawString(72, 700, text_rich_media)  # Adjust y position to fit new text

# Adding Digital Rights Management (DRM) feature text
text_drm = "15. Digital Rights Management (DRM): PDFs can be protected by DRM systems to control copying, printing, and alteration, ensuring content creators can secure their intellectual property."
c.drawString(72, 680, text_drm)  # Adjust y position for DRM text

# Adding Advanced Search Features text
text_advanced_search = "15. Advanced Search Features: PDFs can offer advanced search capabilities, including context searches, synonym searches, and pattern matching, enhancing the user's ability to locate information within large documents."
c.drawString(72, 660, text_advanced_search)  # Adjust y position for Advanced Search Features text

# Save the PDF
c.showPage()
c.save()

print(f'PDF with basic accessibility features, rich media support, DRM, and advanced search features created at {file_path}')