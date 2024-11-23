from fpdf import FPDF

# Create a PDF class inheriting from FPDF
class PDF(FPDF):
    def add_link(self, x, y, w, h, link):
        # Store the current position
        self._out('q')
        # Set the annotation attributes
        self._out('%.2F %.2F %.2F %.2F re' % (x * self.k, (self.h - y) * self.k, w * self.k, -h * self.k))
        self._out('W')
        self._out('2 J')
        self._out('1 j')
        self.set_link('', 0, link)
        # Close the annotation
        self._out('ET')
        self._out('Q')

# Create a PDF object
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set up a link
link = 'https://www.example.com'
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Click Here to Visit Example', ln=True, align='C', link=link)

# Save the PDF file
pdf.output('./tmp/link_example.pdf')