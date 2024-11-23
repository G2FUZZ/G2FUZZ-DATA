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

# Add Multi-Language Support feature description
multi_language_support_description = """4. Multi-Language Support: PDFs can support multiple languages within the same document, including right-to-left languages such as Arabic and Hebrew, enhancing global usability and accessibility."""

# You may want to adjust the position and size as needed for the Multi-Language Support.
pdf.set_xy(10, 20)
pdf.set_text_color(255, 0, 0) # Setting text color to red for visibility
pdf.multi_cell(0, 10, multi_language_support_description)

# Add Color Spaces feature description
color_spaces_description = """7. Color Spaces: They support a variety of color spaces including CMYK, RGB, and spot colors, ensuring accurate color reproduction for printing and digital viewing."""

# You may want to adjust the position and size as needed for the Color Spaces.
pdf.set_xy(10, 50)
pdf.set_text_color(0, 0, 255) # Setting text color to blue for visibility
pdf.multi_cell(0, 10, color_spaces_description)

# Add Real-time Collaboration feature description
real_time_collaboration_description = """15. Real-time Collaboration: Some PDF solutions offer real-time collaboration features, allowing multiple users to view, comment, and edit documents simultaneously, enhancing teamwork and productivity."""

# You may want to adjust the position and size as needed for the Real-time Collaboration.
pdf.set_xy(10, 100)
pdf.set_text_color(0, 128, 0) # Setting text color to green for visibility
pdf.multi_cell(0, 10, real_time_collaboration_description)

# Save the pdf with name .pdf
pdf.output("./tmp/extended_hyperlinked_document_with_additional_feature.pdf")