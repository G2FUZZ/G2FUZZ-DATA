from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# SVG content as a string for the base layer
base_layer_svg_content = """
<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.  
</svg>
"""

# SVG content for an additional layer
additional_layer_svg_content = """
<svg height="100" width="100">
  <rect x="10" y="10" width="80" height="80" stroke="blue" stroke-width="3" fill="yellow" />
  Sorry, your browser does not support inline SVG.  
</svg>
"""

# Write the base layer SVG content to a temporary file
temp_base_layer_file_path = './tmp/temp_base_layer_svg_file.svg'
with open(temp_base_layer_file_path, 'w') as svg_file:
    svg_file.write(base_layer_svg_content)

# Write the additional layer SVG content to a temporary file
temp_additional_layer_file_path = './tmp/temp_additional_layer_svg_file.svg'
with open(temp_additional_layer_file_path, 'w') as svg_file:
    svg_file.write(additional_layer_svg_content)

# Convert SVG files to ReportLab graphics objects
base_layer_graphics = svg2rlg(temp_base_layer_file_path)
additional_layer_graphics = svg2rlg(temp_additional_layer_file_path)

# Create a PDF file
pdf_file_path = './tmp/svg_with_layers_in_pdf.pdf'
c = canvas.Canvas(pdf_file_path, pagesize=A4)

# Drawing the base layer
renderPDF.draw(base_layer_graphics, c, 100, 700)

# Drawing the additional layer on top
renderPDF.draw(additional_layer_graphics, c, 150, 650)

# Save the PDF
c.save()

# Optionally, delete the temporary SVG files after use
os.remove(temp_base_layer_file_path)
os.remove(temp_additional_layer_file_path)

print(f"PDF with SVG and layered graphics has been saved to {pdf_file_path}")