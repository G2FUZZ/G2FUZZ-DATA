from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Features - Compression and Layer Visibility', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

title1 = 'Compression'
body1 = 'PDF files support various compression methods to reduce file size without compromising quality.'

title2 = 'Layer Visibility'
body2 = 'PDF files can contain layers with adjustable visibility settings for organizing content and presenting information selectively.'

pdf.chapter_title(title1)
pdf.chapter_body(body1)

pdf.add_page()
pdf.chapter_title(title2)
pdf.chapter_body(body2)

pdf.output('./tmp/compression_layer_visibility_features.pdf')