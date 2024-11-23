from fpdf import FPDF
import os

# Create tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

class PDF(FPDF):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, title, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, body):
        # Read text file
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 10, body)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 10, '(end of excerpt)')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

# Adding a chapter
chapter_title = '1. Text and Fonts Embedding'
chapter_body = '''PDF files can embed text and fonts within the document, ensuring that the content displays the same way on any device, preserving the original formatting and appearance. This feature is particularly useful for documents that need to be distributed or viewed on various platforms and devices, as it ensures the integrity and readability of the document's content. Font embedding in PDFs includes not just the typeface but also the character encoding, which helps in displaying the text correctly even if the viewing system does not have the font installed.'''

pdf.chapter_title(chapter_title)
pdf.chapter_body(chapter_body)

pdf_file = os.path.join(output_dir, 'Text_and_Fonts_Embedding.pdf')
pdf.output(pdf_file)
print(f'PDF file has been created: {pdf_file}')