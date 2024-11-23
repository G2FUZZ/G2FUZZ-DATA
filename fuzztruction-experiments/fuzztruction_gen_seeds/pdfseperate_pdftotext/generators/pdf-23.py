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

# Save the PDF with name .pdf
pdf.output("./tmp/hyperlinked_pronunciation_hints_document.pdf")