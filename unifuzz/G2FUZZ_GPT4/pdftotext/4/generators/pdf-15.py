from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightgrey, black

def create_pdf_with_watermark_and_background(output_filename):
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
    text = "This is an example of a PDF with a watermark and a background."
    c.drawString(72, 720, text)
    
    c.showPage()
    c.save()

if __name__ == "__main__":
    output_path = "./tmp/watermarked_background_pdf.pdf"
    create_pdf_with_watermark_and_background(output_path)
    print(f"PDF with watermark and background was saved to {output_path}")