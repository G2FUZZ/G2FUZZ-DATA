from fpdf import FPDF
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            # Customize the first page header
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'Comprehensive PDF Document', 0, 1, 'C')
        else:
            # Standard header for other pages
            self.set_font('Arial', 'I', 12)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Chapter %d : %s' % (num, title), 0, 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, w=150)
        self.ln()

    def add_table_of_contents(self):
        self.add_page()
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Table of Contents', 0, 1, 'C')
        self.ln(10)

        # Simulate adding some chapters
        self.set_font('Arial', '', 12)
        for chapter_num in range(1, 4):
            self.cell(0, 10, 'Chapter {}: Some Title Here'.format(chapter_num), 0, 1)
            self.ln(5)

        # Create a link to the first page
        first_page_link = self.add_link()
        self.set_link(first_page_link, page=1)

        # Add a link back to the first page
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Go to First Page', 0, 1, 'C', link=first_page_link)

# Create instance of FPDF class
pdf = PDF()

# Create a link to the first page before adding any pages
first_page_link = pdf.add_link()

# Add first page to start
pdf.add_page()

# Set the link to the first page now that it's added
pdf.set_link(first_page_link, page=1)

# Add a table of contents
pdf.add_table_of_contents()

# Add chapters
for i in range(1, 4):
    pdf.add_page()
    pdf.chapter_title(i, 'Introduction to Chapter {}'.format(i))
    pdf.chapter_body('This is the content of chapter {}. Here you could describe the purpose of this chapter and include any relevant information. You can also embed images, tables, and other elements to enrich the document.'.format(i))
    
    # Optionally add an image to each chapter
    # Ensure an image exists at this path or adjust the path to an existing image
    # pdf.add_image('path/to/image.jpg')

# Save the pdf file
pdf_file_path = f"{output_dir}comprehensive_document.pdf"
pdf.output(pdf_file_path)

print(f"PDF file has been created: {pdf_file_path}")