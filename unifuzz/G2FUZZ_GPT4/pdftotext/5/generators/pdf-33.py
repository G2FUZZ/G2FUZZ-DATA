from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# File path for the new PDF
file_path = os.path.join(output_dir, 'accessible_pdf_with_additional_features.pdf')

# Create a PDF with reportlab
c = canvas.Canvas(file_path, pagesize=letter)
c.setTitle("Accessible PDF with Enhanced Features Example")

# Adding accessibility features text
text_accessibility = "Accessibility Features: PDFs support accessibility features such as text-to-speech and the ability to reflow text, making documents more accessible to users with disabilities."
c.drawString(72, 720, text_accessibility)  # Starting at x=72, y=720

# Adding rich media and flash support text
text_rich_media = "13. Rich Media and Flash Support: While diminishing in usage, PDFs have historically supported embedding of Flash and other rich media content, allowing for dynamic and interactive elements within documents."
c.drawString(72, 700, text_rich_media)  # Adjust y position to fit new text

# Adding Predictive Text and Spell Check feature text
text_predictive_text = "3. Predictive Text and Spell Check: Some PDF creation and viewing software include features for predictive text input and spell checking, enhancing the efficiency and accuracy of form filling and content creation."
c.drawString(72, 680, text_predictive_text)  # Adjust y position to fit new text

# Save the PDF
c.showPage()
c.save()

print(f'PDF with enhanced accessibility features and rich media support created at {file_path}')