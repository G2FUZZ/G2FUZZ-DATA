from fpdf import FPDF

# Create PDF file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Accessibility: PDF files can be tagged to enhance accessibility for users with disabilities.", ln=True)

# Save PDF file
pdf_output_path = "./tmp/accessibility_feature.pdf"
pdf.output(name=pdf_output_path)