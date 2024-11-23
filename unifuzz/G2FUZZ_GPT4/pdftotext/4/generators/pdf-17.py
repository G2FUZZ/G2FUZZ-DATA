from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightgrey, black
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_pdf_with_forms_and_data_collection(output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    # Draw a background on every page
    c.setFillColor(lightgrey)
    c.rect(0, 0, width, height, fill=True, stroke=False)
    
    # Prepare to add a watermark
    c.setFont("Helvetica", 40)
    c.setFillColor(black)
    c.setStrokeColor(black)
    
    # Add the watermark text
    watermark_text = "CONFIDENTIAL"
    text_width = c.stringWidth(watermark_text, "Helvetica", 40)
    c.saveState()
    c.translate(width / 2.0, height / 2.0)
    c.rotate(45)
    c.drawCentredString(0, 0, watermark_text)
    c.restoreState()
    
    # Example content
    c.setFont("Helvetica", 12)
    c.setFillColor(black)
    text = "This PDF includes a form for data collection."
    c.drawString(72, 720, text)
    
    # Adding forms and data collection feature
    form_width = 400
    form_height = 20
    form_x_start = 100
    form_y_start = 650

    # Draw a form field for Name
    c.setStrokeColor(black)
    c.rect(form_x_start, form_y_start, form_width, form_height, fill=False, stroke=True)
    c.drawString(form_x_start, form_y_start + 25, "Name:")

    # Draw a form field for Email
    c.rect(form_x_start, form_y_start - 50, form_width, form_height, fill=False, stroke=True)
    c.drawString(form_x_start, form_y_start - 25, "Email:")

    # Draw a checkbox for receiving newsletters
    c.rect(form_x_start, form_y_start - 100, form_height, form_height, fill=False, stroke=True)
    c.drawString(form_x_start + 30, form_y_start - 95, "Subscribe to newsletter")

    # Inform users how to fill the form
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.darkgrey)
    c.drawString(form_x_start, form_y_start - 130, "Please fill out the form fields above.")

    c.showPage()
    c.save()

if __name__ == "__main__":
    output_path = "./tmp/form_data_collection_pdf.pdf"
    create_pdf_with_forms_and_data_collection(output_path)
    print(f"PDF with forms and data collection was saved to {output_path}")