from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import black
import os

def mobile_optimized_canvas(cnv, mobile_optimized=True):
    if mobile_optimized:
        mobile_page_size = landscape(A4)
        cnv.setPageSize(mobile_page_size)

def create_article_threads(cnv):
    cnv.bookmarkPage("1")
    cnv.addOutlineEntry("Article Thread starts here", "1", level=0, closed=False)
    cnv.setStrokeColor(black)
    cnv.setLineWidth(1)
    cnv.line(100, 650, 300, 650)
    cnv.line(300, 650, 300, 450)
    cnv.drawString(100, 660, "Start of Article Thread")
    cnv.drawString(100, 450, "End of Article Thread")

def include_pdf_vt_feature(cnv):
    # This is a placeholder representation for the PDF/VT feature.
    # ReportLab does not directly support PDF/VT; you would typically
    # use it with variable data printing software or customize the output
    # to comply with PDF/VT standards in a production environment.
    cnv.drawString(100, 400, "6. PDF/VT: Support for variable and transactional printing.")

output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, "vector_graphics_with_article_threads_and_pdfvt.pdf")

c = canvas.Canvas(file_path, pagesize=A4)

mobile_optimized_canvas(c, mobile_optimized=True)

create_article_threads(c)

c.rect(100, 500, 200, 100, stroke=1, fill=0)

c.circle(300, 400, 50, stroke=1, fill=0)

c.setFont("Helvetica", 12)
c.drawString(100, 550, "Rectangle and Circle (Vector Graphics)")
c.drawString(100, 530, "9. Mobile Optimization: PDF files optimized for mobile devices.")
c.drawString(100, 430, "15. Article Threads: PDFs can define article threads that allow readers to follow a logical reading order.")

include_pdf_vt_feature(c)

c.save()