from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfform
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFError

# Create a PDF file with bookmarks, interactive forms, and layers
def create_pdf_with_bookmarks_forms_and_layers(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)

    # Add bookmarks
    c.bookmarkPage("Start of Document")
    c.drawString(100, 700, "This is the start of the document.")
    c.showPage()

    c.bookmarkPage("Middle of Document")
    c.drawString(100, 600, "This is the middle of the document.")
    c.showPage()

    c.bookmarkPage("End of Document")
    c.drawString(100, 500, "This is the end of the document.")
    c.showPage()

    # Add interactive forms
    c.drawString(100, 400, "Please fill out the form below:")
    c.setFont("Helvetica", 12)
    c.drawString(100, 380, "Name:")
    c.rect(200, 375, 200, 20, fill=0)
    c.drawString(100, 350, "Email:")
    c.rect(200, 345, 200, 20, fill=0)

    c.showPage()

    # Add layers
    try:
        registerFont(TTFont('Arial', 'Arial.ttf'))
        c.setFont("Arial", 12)
        c.drawString(100, 700, "This text is on Layer 1")
        c.setPageDuration(5)
        c.beginLayer("Layer 1")
        c.drawString(100, 650, "This text is on Layer 2")
        c.endLayer()
    except TTFError:
        print("Error: Font file not found.")

    c.save()

# Save the PDF file with bookmarks, interactive forms, and layers
file_name = "./tmp/pdf_with_bookmarks_forms_and_layers.pdf"
create_pdf_with_bookmarks_forms_and_layers(file_name)