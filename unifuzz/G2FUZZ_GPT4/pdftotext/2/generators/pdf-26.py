from fpdf import FPDF
import requests

class PDF(FPDF):
    def header(self):
        # Add a watermark
        self.set_font('Arial', 'B', 12)
        self.set_text_color(220, 220, 220)
        self.cell(0, 10, 'This is a watermark', align='C', ln=True)
    
    def footer(self):
        # Add a page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_background(self, bg_file):
        self.image(bg_file, x = -0.5, y = -0.5, w = self.w + 1, h = self.h + 1)
        
    def external_references(self, url):
        # Fetch content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Assuming the external reference is text content
            content = response.text
            # Add the content to the PDF
            self.set_font('Arial', '', 10)
            self.set_text_color(60, 128, 255)  # Set a different color to distinguish
            self.multi_cell(0, 10, 'External References:\n'+content)
            self.ln()
        else:
            self.set_font('Arial', 'I', 10)
            self.multi_cell(0, 10, 'Failed to fetch external references.')
            self.ln()

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# If you want to add a background, call `add_background` here
# pdf.add_background('path_to_background_image.jpg')

# Adding a chapter
pdf.chapter_title('Chapter 1')
pdf.chapter_body('This is the body of chapter 1. Here you can put as much text as you want, and it will automatically be divided into lines and pages. This text can also include special characters such as é or ä.')

# Adding external references
external_url = 'http://example.com/some_external_content.txt'
pdf.external_references(external_url)

# Save the PDF to a file
output_file = './tmp/extended_pdf_with_external_references.pdf'
pdf.output(output_file)