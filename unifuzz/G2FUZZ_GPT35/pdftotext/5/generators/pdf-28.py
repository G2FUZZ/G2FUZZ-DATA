from fpdf import FPDF

class ComplexPDFGenerator(FPDF):
    def add_complex_content(self):
        # Page 1
        self.add_page()
        self.set_font("Arial", style="B", size=16)
        self.set_text_color(0, 0, 255)
        self.cell(200, 10, "Welcome to Complex PDF Generator", ln=True, align='C')
        
        # Page 2
        self.add_page()
        self.set_font("Times", style="I", size=14)
        self.set_text_color(255, 0, 0)
        self.multi_cell(0, 10, "This PDF file demonstrates the capabilities of Complex PDF Generator class.", 0, 'J')
        
        # Page 3
        self.add_page()
        self.set_font("Courier", style="U", size=12)
        self.set_text_color(0, 128, 0)
        self.multi_cell(0, 10, "You can customize fonts, colors, alignments, and add multiple pages.", 0, 'L')
        
    def generate_pdf(self, output_file):
        self.add_complex_content()
        self.output(output_file)

pdf_generator = ComplexPDFGenerator()
pdf_generator.generate_pdf("./tmp/complex_pdf_file.pdf")