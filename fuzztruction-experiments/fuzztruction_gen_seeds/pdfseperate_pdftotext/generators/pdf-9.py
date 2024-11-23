from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfdoc import PDFCatalog, PDFDocument
# Ensure pdfrw is installed in your environment if you plan to use it
# import pdfrw

def create_accessible_pdf(path):
    # Initialize a canvas
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    # Title and Author for accessibility
    c.setTitle("Accessible PDF Example")
    c.setAuthor("Author Name")

    # Adding a bookmark
    c.bookmarkPage("page1")
    c.addOutlineEntry("Title Page", "page1", level=0)

    # Adding text with a note on accessibility
    c.drawString(72, height - 72, "Accessible PDF Example")
    c.drawString(72, height - 96, "This PDF includes bookmarks for accessibility.")

    c.showPage()
    c.save()

# Save the PDF to the desired path
create_accessible_pdf('./tmp/accessible_pdf_example.pdf')