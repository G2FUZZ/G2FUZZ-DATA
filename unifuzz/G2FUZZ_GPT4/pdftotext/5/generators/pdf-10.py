from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    # Define custom page labels and numbering
    sections = [
        {"label": "Preface", "pages": 2, "numbering_style": "roman"},
        {"label": "Main Content", "pages": 5, "numbering_style": "arabic"},
        {"label": "Appendix", "pages": 3, "numbering_style": "alphabet"}
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

    c.save()

# Specify the path
path = "./tmp/custom_page_numbering.pdf"
create_pdf(path)