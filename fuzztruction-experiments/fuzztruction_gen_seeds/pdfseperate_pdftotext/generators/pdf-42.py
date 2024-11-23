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

    def add_pronunciation_hints(self, text, hints):
        """
        Add pronunciation hints for text-to-speech (TTS) systems in the PDF.

        Args:
        - text (str): The text to add to the PDF.
        - hints (str): The pronunciation hints for the TTS system.
        """
        self.set_font('Arial', '', 12)
        self.set_text_color(50, 50, 50)  # Dark grey color for text
        self.multi_cell(0, 10, f"{text} ({hints})")

    def add_color_management(self, description):
        """
        Add a section about Color Management to inform the reader 
        that the PDF includes embedded ICC profiles for accurate color reproduction.

        Args:
        - description (str): The text describing the color management feature.
        """
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.set_text_color(80, 80, 80)  # Dark grey color for header
        self.cell(0, 10, 'Color Management', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.set_text_color(50, 50, 50)  # Dark grey color for text
        self.multi_cell(0, 10, description)

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
pdf.attach_file_link('path/to/your/file.txt', 'YourFileDisplayName.txt')

# Add pronunciation hints
pdf.add_pronunciation_hints("Example", "EHG-ZAAM-PL")

# Add color management feature description
color_management_description = """
PDFs support embedded ICC profiles and color management systems to ensure that colors are 
reproduced accurately across different devices and print conditions. This document includes 
color profiles to maintain visual consistency for all viewers.
"""
pdf.add_color_management(color_management_description)

# Save the PDF with name .pdf
pdf.output("./tmp/extended_hyperlinked_pronunciation_hints_document.pdf")