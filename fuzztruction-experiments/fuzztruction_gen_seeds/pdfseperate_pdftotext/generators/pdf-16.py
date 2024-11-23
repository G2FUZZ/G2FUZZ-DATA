from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def attach_file_link(self, filepath, display_name):
        """
        Create a link in the PDF that, when clicked, will prompt to open a file.
        This is a workaround and does not embed the file into the PDF.

        Args:
        - filepath (str): The path to the file.
        - display_name (str): The text displayed in the PDF for the link.
        """
        self.set_text_color(0, 0, 255)  # Set link color to blue
        self.set_font('Arial', 'U', 12)  # Set font for the link
        self.write(5, display_name, filepath)  # Write the link
        self.set_text_color(0, 0, 0)  # Reset text color to black

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a hyperlink
html = """<a href="https://www.example.com">Visit Example.com</a>"""
pdf.write_html(html)

# Attach a file link
# Note: This will not embed the file into the PDF, but create a clickable link in the document.
# The file path is displayed as a link, and the file needs to be in the same location as the PDF when opened.
pdf.attach_file_link('path/to/your/file.txt', 'YourFileDisplayName.txt')

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinked_and_attached_document.pdf")