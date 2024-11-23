from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from reportlab.lib.utils import ImageReader

# Function to create a QR code image
def create_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Function to create a PDF with a QR code that links to a multimedia content
def create_pdf_with_multimedia(output_filename, qr_code_image):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawString(100, 750, "Scan the QR code to view multimedia content.")
    
    # Include the QR code in the PDF
    qr_image = ImageReader(qr_code_image)
    c.drawImage(qr_image, 100, 600, width=200, height=200)
    
    c.save()

# Main execution
if __name__ == "__main__":
    multimedia_url = "https://example.com/multimedia-content"  # URL to multimedia content
    qr_code_filename = "./tmp/multimedia_qr.png"
    pdf_filename = "./tmp/multimedia_pdf.pdf"
    
    # Ensure the ./tmp/ directory exists
    import os
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    create_qr_code(multimedia_url, qr_code_filename)
    create_pdf_with_multimedia(pdf_filename, qr_code_filename)