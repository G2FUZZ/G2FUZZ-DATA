from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# SVG content as a string
svg_content = """
<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.  
</svg>
"""

# Temporary SVG file path
temp_svg_file_path = './tmp/temp_svg_file.svg'

# Write the SVG content to a temporary file
with open(temp_svg_file_path, 'w') as svg_file:
    svg_file.write(svg_content)

# Convert SVG file to a ReportLab graphics object
svg_graphics = svg2rlg(temp_svg_file_path)

# Create a PDF file and draw the SVG on it
pdf_file_path = './tmp/svg_in_pdf_with_bookmarks.pdf'
c = canvas.Canvas(pdf_file_path, pagesize=A4)

# Drawing the SVG onto the PDF canvas
renderPDF.draw(svg_graphics, c, 100, 700)

# Adding a bookmark for the SVG drawing
c.bookmarkPage("svg_drawing")
c.addOutlineEntry("SVG Drawing", "svg_drawing", level=0, closed=False)

# Configuring the document to open with outlines expanded
# Directly access the Catalog attribute of the document and set the PageMode
catalog = c._doc.Catalog
catalog.PageMode = 'UseOutlines'

c.save()

# Optionally, delete the temporary SVG file after use
os.remove(temp_svg_file_path)

print(f"PDF with SVG and bookmarks has been saved to {pdf_file_path}")