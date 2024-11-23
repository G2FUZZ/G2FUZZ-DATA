from fpdf import FPDF

class PDFWithFormCalculation(FPDF):
    def add_form_calculation_field(self, field_name, default_value=0):
        self.set_font("Arial", size=12)
        self.cell(200, 10, f"Form Calculations: {field_name}", ln=True)
        self.cell(200, 10, f"Default Value: {default_value}", ln=True)
    
pdf = PDFWithFormCalculation()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "PDF files can contain text data, which can be easily searched, selected, and copied.", ln=True)
pdf.add_form_calculation_field("Total", default_value=100)

# Save PDF file
pdf_output = "./tmp/pdf_with_form_calculation.pdf"
pdf.output(pdf_output)