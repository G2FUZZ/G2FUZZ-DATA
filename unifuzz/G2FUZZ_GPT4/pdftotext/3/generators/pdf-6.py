from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
c = canvas.Canvas(os.path.join(output_dir, "interactive_form.pdf"), pagesize=letter)
c.drawString(100, 750, "Interactive Form")

# Save the current state and start a new page
c.saveState()
c.showPage()
c.save()

# Use pdfrw to add interactive form elements
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict

# Load the PDF we just created
input_pdf_path = os.path.join(output_dir, "interactive_form.pdf")
output_pdf_path = os.path.join(output_dir, "interactive_form_with_fields.pdf")
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Add form elements to the first page
page = PageMerge(reader.pages[0])

# Text field
page.add(IndirectPdfDict(
    Type="/Annot",
    Subtype="/Widget",
    FT="/Tx",  # Field type: text input
    Rect=[100, 700, 350, 730],
    T="user_name",  # Field name
    V="Jane Doe",  # Default value
    Ff=1<<0,  # Field flags: read-only flag is not set
    DA="/Helv 0 Tf 0 g"  # Default appearance
))

# Checkbox
page.add(IndirectPdfDict(
    Type="/Annot",
    Subtype="/Widget",
    FT="/Btn",  # Field type: button (checkbox)
    Rect=[100, 650, 120, 670],
    T="accept_terms",  # Field name
    V="/Yes",  # Default value: checked
    AS="/Yes",
    Ff=1<<15,  # Field flags: pushbutton flag is not set, meaning it's a checkbox
    DA="/Helv 0 Tf 0 g"
))

# Dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
page.add(IndirectPdfDict(
    Type="/Annot",
    Subtype="/Widget",
    FT="/Ch",  # Field type: choice
    Rect=[100, 600, 350, 620],
    T="dropdown_menu",  # Field name
    V="Option 1",  # Default value
    Opt=options,  # Options
    Ff=1<<19,  # Field flags: combo box
    DA="/Helv 0 Tf 0 g"
))

# Finalize the modifications to the page
page = page.render()

# Write the modified content back to a new file
writer.addpages([page] + reader.pages[1:])
writer.write(output_pdf_path)

print(f"Interactive PDF form has been created at: {output_pdf_path}")