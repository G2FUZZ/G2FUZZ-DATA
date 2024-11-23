from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    # Define custom page labels and numbering
    sections = [
        {"label": "Preface", "pages": 2, "numbering_style": "roman"},
        {"label": "Main Content", "pages": 5, "numbering_style": "arabic"},
        {"label": "Appendix", "pages": 3, "numbering_style": "alphabet"},
        {"label": "Viewing Options", "pages": 1, "numbering_style": "arabic"}  # Added section for Viewing Options
    ]

    page_counter = 1
    for section in sections:
        for i in range(section["pages"]):
            c.drawString(100, height - 100, f"Section: {section['label']}")
            
            if section["numbering_style"] == "roman":
                page_number = str(page_counter).upper()  # Simple conversion to Roman numerals for demonstration
            elif section["numbering_style"] == "alphabet":
                # Simple conversion to letters. This example will not go beyond 26 pages for simplicity.
                page_number = chr(64 + page_counter) if page_counter <= 26 else "Z"
            else:
                page_number = str(page_counter)
                
            c.drawString(width - 100, 100, f"Page {page_number}")
            c.showPage()
            page_counter += 1

        # After finishing each section, check if it's the Viewing Options section to add its content
        if section["label"] == "Viewing Options":
            # Here you can add anything specific to the Viewing Options section
            # For simplicity, we'll just add a generic description
            c.drawString(100, height / 2, "Viewing Options allow customization of the viewing experience, including:")
            c.drawString(100, height / 2 - 20, "- Single page")
            c.drawString(100, height / 2 - 40, "- Continuous scroll")
            c.drawString(100, height / 2 - 60, "- Two-page facing")
            c.drawString(100, height / 2 - 80, "- Presentation modes")
            page_counter += 1  # Increment the page counter if additional pages are added here
            c.showPage()  # Show the new page with Viewing Options content

    c.save()

# Specify the path
path = "./tmp/custom_page_numbering_with_viewing_options.pdf"
create_pdf(path)