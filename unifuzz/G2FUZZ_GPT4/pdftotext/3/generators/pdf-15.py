from fpdf import FPDF, HTMLMixin

class MyPDF(FPDF, HTMLMixin):
    def header(self):
        # This function could be used to generate thumbnails but FPDF doesn't support direct thumbnail generation.
        # Instead, it could be used to prepare for adding thumbnails through another library or manually.
        pass

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

# Unfortunately, FPDF does not have built-in support for generating page thumbnails and previews directly.
# To add thumbnails, you would typically need to generate thumbnail images of each page separately,
# then embed these images into a PDF as thumbnails. This often involves using external tools or libraries
# in conjunction with FPDF to first capture page images, resize them into thumbnails,
# and then reference these images within the PDF's structure.
# This is a complex task that requires manipulating the PDF structure at a lower level than FPDF provides.

# Since we cannot directly implement the feature within the scope of FPDF's capabilities,
# the suggestion is to use additional libraries like PyMuPDF (fitz) to create thumbnails
# and then integrate them into the PDF, or use other tools to post-process the PDF files.

# Save the pdf with name .pdf
pdf.output("./tmp/extended_hyperlinks.pdf")