from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Setting up the file name and path
file_path = './tmp/bookmark_navigation_demo_with_progressive_loading.pdf'

# Creating a canvas to draw on with 'pageCompression' enabled for progressive loading
c = canvas.Canvas(file_path, pagesize=letter, pageCompression=1)

# Adding a title and some content
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Bookmark and Navigation Features Demo with Progressive Loading")
c.drawString(100, 735, "This document includes bookmarks for navigation and supports progressive loading.")

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

# Add a third page to demonstrate progressive loading feature
c.showPage()
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Progressive Loading Page")
c.drawString(100, 735, "This page is meant to demonstrate the Progressive Loading feature.")
c.bookmarkPage("progressive_loading_page")
c.addOutlineEntry("Progressive Loading", "progressive_loading_page", level=0)

# Saving the PDF file
c.save()