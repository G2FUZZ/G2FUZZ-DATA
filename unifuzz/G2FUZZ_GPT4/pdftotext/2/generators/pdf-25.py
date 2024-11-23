from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.pdfbase import pdfform
from reportlab.lib.utils import ImageReader

file_path = './tmp/bookmark_navigation_print_settings_demo.pdf'

c = canvas.Canvas(file_path, pagesize=letter)

# Adding a title and some content
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Bookmark, Navigation and Print Settings Demo")
c.drawString(100, 735, "This document includes bookmarks for navigation and embedded print settings.")

# Adding bookmarks for navigation
# Add a bookmark to the first page
c.bookmarkPage("first_page")
c.addOutlineEntry("First Page", "first_page", level=0)

# Add another page with a different bookmark and content
c.showPage()
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Second Page")
c.bookmarkPage("second_page")
c.addOutlineEntry("Second Page", "second_page", level=0)

# Adding a third page to demonstrate embedded print settings
c.showPage()
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Print Settings Page")

# Unfortunately, directly embedding print settings such as paper size, duplex mode,
# and color options within a PDF using ReportLab is not straightforward
# as it requires specific support from the PDF viewer or printer software,
# which is not directly controlled through ReportLab's API.

# One approach to indicate preferred print settings is by including text instructions
# or using PDF actions or JavaScript (for PDF viewers that support it),
# but these methods are outside the scope of ReportLab's current capabilities.
# Therefore, we include a placeholder text here to illustrate where such instructions
# might go, acknowledging that implementing this would depend on the specific
# requirements and capabilities of the software and hardware being used to view and print the PDF.

c.drawString(100, 730, "Note: This document is intended to be printed in duplex mode,")
c.drawString(100, 715, "with color output on letter-size paper. Please adjust your printer settings accordingly.")

# Saving the PDF file
c.save()