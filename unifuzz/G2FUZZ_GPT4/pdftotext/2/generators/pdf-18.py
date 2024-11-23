from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfdoc import PDFCatalog

file_path = './tmp/article_demo.pdf'

def add_bookmark(c, title, key):
    # This function demonstrates a simple way to add a bookmark to the current page
    # Note: This is a basic implementation and might not fully work as expected for complex PDF structures
    c.bookmarkPage(key)
    c.addOutlineEntry(title, key, level=0)

c = canvas.Canvas(file_path, pagesize=letter)

# Adding a title and some content
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Demo Document with Basic Bookmark")
c.drawString(100, 735, "This document includes a basic bookmark for demonstration.")

# Manually adding a bookmark for the first page
add_bookmark(c, "First Page", "first_page_key")

# Add another page with a different bookmark
c.showPage()
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Second Page")
add_bookmark(c, "Second Page", "second_page_key")

c.save()