from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add a hyperlink
html = """<a href="https://www.example.com">Visit Example.com</a>"""
pdf.write_html(html)

# Add Versioning and Incremental Updates feature description
versioning_updates_description = """5. Versioning and Incremental Updates: PDF files can be created to allow for incremental updates, where changes are appended to the end of the file without a complete rewrite, facilitating efficient document revision management."""

# You may want to adjust the position and size as needed for the new text.
pdf.set_xy(10, 20) # Adjusted for the new feature text
pdf.set_text_color(0, 0, 255) # Setting text color to blue for visibility
pdf.multi_cell(0, 10, versioning_updates_description)

# Add Color Spaces feature description
color_spaces_description = """7. Color Spaces: They support a variety of color spaces including CMYK, RGB, and spot colors, ensuring accurate color reproduction for printing and digital viewing."""

# You may want to adjust the position and size as needed.
pdf.set_xy(10, 80) # Adjusted for the subsequent text, ensure not to overlap with the previous text
pdf.set_text_color(0, 0, 255) # Keeping text color to blue for consistency
pdf.multi_cell(0, 10, color_spaces_description)

# Save the pdf with name .pdf
pdf.output("./tmp/extended_version_incremental_updates_document.pdf")