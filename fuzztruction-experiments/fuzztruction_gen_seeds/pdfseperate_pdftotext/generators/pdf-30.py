import PyPDF2
from PyPDF2 import PdfWriter, PdfReader

# Create a simple PDF using PyPDF2
writer = PdfWriter()

# Specify the page size for the blank page (A4 size in this example)
page_width = 595  # A4 width in points
page_height = 842  # A4 height in points

# Add a blank page which will serve as a section in the PDF for bookmark
blank_page = writer.add_blank_page(width=page_width, height=page_height)

temp_pdf_path = './tmp/simple_pdf_with_bookmarks.pdf'
with open(temp_pdf_path, 'wb') as f_out:
    writer.write(f_out)

# Open the newly created PDF to apply security features and add bookmarks
reader = PdfReader(temp_pdf_path)
writer = PdfWriter()

# Copy pages from the original PDF to the writer
for page_number, page in enumerate(reader.pages, start=1):
    writer.add_page(page)
    writer.add_outline_item(title=f"Section {page_number}", page_number=page_number-1, parent=None)

# Set the security settings
user_password = 'user'
owner_password = 'owner'
writer.encrypt(user_pwd=user_password, owner_pwd=owner_password, use_128bit=True)

# Before saving, enable the optimization for Fast Web View
# Note: PyPDF2 does not directly support setting the Linearization flag for Fast Web View.
# However, you can use other libraries like 'pypdfium2' or 'qpdf' to achieve this.
# For this example, let's assume a post-processing step with an external tool.
secure_pdf_path_with_bookmarks = './tmp/secure_pdf_with_bookmarks.pdf'
with open(secure_pdf_path_with_bookmarks, 'wb') as f_out:
    writer.write(f_out)

# Assuming an external tool 'pypdfium2' or 'qpdf' for linearization (Fast Web View)
# This step would typically be executed outside of this Python script as a command-line invocation.
# Example (if using qpdf): 
# os.system(f"qpdf --linearize {secure_pdf_path_with_bookmarks} {secure_pdf_path_with_bookmarks}_linearized.pdf")

print(f'Secure PDF with bookmarks created at: {secure_pdf_path_with_bookmarks}')
# Remember to linearize the PDF for Fast Web View with an external tool after this script runs.