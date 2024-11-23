from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a directory to save the PDF if it doesn't already exist
import os
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# File path for the new PDF
new_file_path = directory + "extended_page_layout_control.pdf"

# Create a PDF with additional feature description
def create_extended_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    
    # Original feature description
    original_feature = '''13. Page Layout Control: PDFs offer precise page layout control, maintaining the exact placement of text, images, and other elements, ensuring consistent formatting across different viewing environments.'''
    
    # New feature description
    new_feature = '''7. Real-time Collaboration and Review: Some PDF software solutions offer features for real-time collaboration, allowing multiple users to view, comment on, and edit PDF documents simultaneously, facilitating teamwork and remote workflows.'''
    
    # Combine both features
    combined_features = f"{new_feature}\n\n{original_feature}"  # Corrected variable name
    
    text.textLines(combined_features)
    c.drawText(text)
    c.save()

create_extended_pdf(new_file_path)