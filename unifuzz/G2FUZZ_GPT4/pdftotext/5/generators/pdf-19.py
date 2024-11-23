from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def apply_redaction(pdf_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Overlay a white rectangle to cover sensitive information
    for page_number, page in enumerate(reader.pages):
        # Create a temporary PDF to draw the rectangle
        overlay_pdf_path = f"./tmp/overlay_{page_number}.pdf"
        c = canvas.Canvas(overlay_pdf_path, pagesize=letter)
        # Set fill color to white (or match the document's background color)
        c.setFillColorRGB(1, 1, 1)
        # Draw a rectangle over the area to "redact"
        # Adjust the coordinates as needed
        c.rect(100, 705, 200, 10, fill=1)
        c.save()

        # Merge the overlay PDF with the current page
        overlay_reader = PdfReader(overlay_pdf_path)
        overlay_page = overlay_reader.pages[0]
        page.merge_page(overlay_page)

        writer.add_page(page)

        # Clean up the temporary overlay PDF
        os.remove(overlay_pdf_path)

    # Save the "redacted" pdf
    with open(pdf_path, 'wb') as f_out:
        writer.write(f_out)