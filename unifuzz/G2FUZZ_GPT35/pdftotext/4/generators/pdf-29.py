from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_with_complex_features(file_path):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    header = Paragraph("Sample PDF with Complex Features", styles['Heading1'])
    elements.append(header)

    # Add an image
    try:
        logo = Image('logo.png')
        elements.append(logo)
    except Exception as e:
        print(f"Error adding image to PDF: {e}")

    # Add a table
    data = [['Name', 'Age', 'Country'],
            ['Alice', '25', 'USA'],
            ['Bob', '30', 'Canada']]
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
    elements.append(table)

    # Add styled text
    text = "This PDF file includes images, tables, and styled text."
    styled_text = Paragraph(text, styles['Normal'])
    elements.append(styled_text)

    try:
        doc.build(elements)
    except Exception as e:
        print(f"Error building PDF: {e}")

# Generate PDF file with complex features
file_path = "./tmp/complex_features.pdf"
create_pdf_with_complex_features(file_path)
print(f"PDF file with complex features generated at: {file_path}")