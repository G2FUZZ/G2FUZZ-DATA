from fpdf import FPDF

# Create PDF file with Form Fields
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Accessibility: PDF files can be tagged to enhance accessibility for users with disabilities.", ln=True)

# Add Form Fields
pdf.set_font("Arial", style='B', size=14)
pdf.ln(10)
pdf.cell(200, 10, "Form Fields: PDF files can include interactive form fields for data entry and submission.", ln=True)

# Save PDF file
pdf_output_path = "./tmp/accessibility_feature_with_form_fields.pdf"
pdf.output(name=pdf_output_path)