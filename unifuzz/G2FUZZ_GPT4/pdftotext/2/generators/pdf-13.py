from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Setting up the file name and path
file_path = './tmp/bookmark_navigation_demo.pdf'

# Creating a canvas to draw on
c = canvas.Canvas(file_path, pagesize=letter)

# Adding a title and some content
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Bookmark and Navigation Features Demo")
c.drawString(100, 735, "This document includes bookmarks for navigation.")

# Adding bookmarks for navigation
# Add a bookmark to the first page
c.bookmarkPage("first_page")
c.addOutlineEntry("First Page", "first_page", level=0)

# Add another page with a different bookmark
c.showPage()
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Second Page")
c.bookmarkPage("second_page")
c.addOutlineEntry("Second Page", "second_page", level=0)

# Saving the PDF file
c.save()