from fpdf import FPDF, HTMLMixin

class MyPDF(FPDF, HTMLMixin):
    def footer(self):
        # This method is overriding the footer method of the FPDF class.
        # It is called automatically at the bottom of each page.
        # We'll use it to add page labels.
        
        # Set the font for the footer to Arial, italic, and size 8.
        self.set_font('Arial', 'I', 8)
        
        # Get the label of the current page.
        # The getPageLabel method should be implemented to retrieve
        # the custom label for a given page number. This method is not
        # a part of the original FPDF library, so we need to implement it.
        page_label = self.get_page_label(self.page_no())
        
        # Add a cell with the page label. Adjust the width and position as needed.
        # The cell is positioned at the right with a width of 0, meaning it extends to the right margin.
        # The ln=True argument indicates that we want to move below this cell after we place it.
        self.cell(0, 10, page_label, 0, 0, 'C')

    def get_page_label(self, page_number):
        # This is a placeholder method for getting a page label.
        # You should implement your logic here to return the
        # appropriate label for each page number.
        # For example, you might return 'A-1' for the first page,
        # 'A-2' for the second page, etc.
        # This example simply returns 'Page ' + the page number,
        # but you can customize it as needed.
        return 'Page ' + str(page_number)

# Create instance of FPDF class
pdf = MyPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Adding a cell
pdf.cell(200, 10, txt="Welcome to the PDF with hyperlinks!", ln=True)

# Adding a hyperlink
link = "http://www.example.com"
pdf.set_text_color(0, 0, 255)
pdf.write(5, "Click here to visit example.com", link)

# Here, you could add your logic to define page labels if needed.
# For example, setting a custom label for each page based on some criteria.
# Since the example get_page_label method returns a simple label,
# no additional setup is needed for this demonstration.

# Save the pdf with name .pdf
pdf.output("./tmp/hyperlinks_with_page_labels.pdf")