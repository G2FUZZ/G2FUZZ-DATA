from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfdoc
import os

def apply_redaction_and_color_management_with_incremental_updates(source_pdf_path, output_pdf_path, incremental_updates_path):
    reader = PdfReader(source_pdf_path)
    writer = PdfWriter()

    # Configure color management for PDF generation
    pdfdoc.PDFCatalog.OpenAction = '<</OutputIntents [ <</Info (sRGB IEC61966-2.1)\
    /OutputCondition (sRGB IEC61966-2.1)/S/GTS_PDFA1/Type/OutputIntent>> ]>>'

    for page_number, page in enumerate(reader.pages):
        overlay_pdf_path = f"./tmp/overlay_{page_number}.pdf"
        c = canvas.Canvas(overlay_pdf_path, pagesize=letter)
        
        # Set fill color to white for redaction overlay (or match the document's background color)
        c.setFillColorRGB(1, 1, 1)
        # Draw a rectangle over the area to "redact"
        c.rect(100, 705, 200, 10, fill=1)
        c.save()

        overlay_reader = PdfReader(overlay_pdf_path)
        overlay_page = overlay_reader.pages[0]
        page.merge_page(overlay_page)

        writer.add_page(page)

        os.remove(overlay_pdf_path)

    # Save the "redacted" and color-managed PDF
    with open(output_pdf_path, 'wb') as f_out:
        writer.write(f_out)

    # Apply Incremental Updates
    apply_incremental_updates(source_pdf_path, output_pdf_path, incremental_updates_path)

def apply_incremental_updates(source_pdf_path, output_pdf_path, incremental_updates_path):
    # Read the original PDF
    with open(source_pdf_path, 'rb') as f:
        original_pdf = f.read()

    # Read the updated PDF
    with open(output_pdf_path, 'rb') as f:
        updated_pdf = f.read()

    # Find the start of the original PDF's xref table
    original_xref_index = original_pdf.rfind(b'startxref')
    if original_xref_index == -1:
        print("No xref table found in the original PDF")
        return

    # Write the original PDF to the incremental update file
    with open(incremental_updates_path, 'wb') as f:
        f.write(original_pdf)
        
        # Append the new content (from the updated PDF) to the file
        f.write(b'\n')
        f.write(updated_pdf[original_xref_index:])

# Example usage
# apply_redaction_and_color_management_with_incremental_updates('source.pdf', 'output_with_color_management.pdf', 'output_incremental.pdf')