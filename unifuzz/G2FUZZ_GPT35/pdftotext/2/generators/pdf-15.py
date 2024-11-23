from fpdf import FPDF

# Create PDF file with Form Fields and OCR Feature
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Accessibility: PDF files can be tagged to enhance accessibility for users with disabilities.", ln=True)

# Add Form Fields
pdf.set_font("Arial", style='B', size=14)
pdf.ln(10)
pdf.cell(200, 10, "Form Fields: PDF files can include interactive form fields for data entry and submission.", ln=True)

# Add OCR Feature
pdf.set_font("Arial", style='I', size=12)
pdf.ln(10)
pdf.cell(200, 10, "OCR (Optical Character Recognition): PDF files can be created with OCR technology to make scanned text searchable and editable.", ln=True)

# Save PDF file with Form Fields and OCR Feature
pdf_output_path = "./tmp/accessibility_feature_with_form_fields_and_ocr.pdf"
pdf.output(name=pdf_output_path)