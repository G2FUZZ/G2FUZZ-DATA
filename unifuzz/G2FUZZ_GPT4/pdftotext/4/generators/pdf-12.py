from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.lib.units import inch

# Define the document
class MyDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)
        template = PageTemplate('normal', [Frame(0.5*inch, 0.5*inch, 7*inch, 10*inch, id='F1')])
        self.addPageTemplates(template)

    def afterFlowable(self, flowable):
        "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1':
                self.notify('TOCEntry', (0, text, self.page))
            elif style == 'Heading2':
                self.notify('TOCEntry', (1, text, self.page))

# Create a function to build the document
def build_pdf(filename):
    doc = MyDocTemplate(filename)
    styles = getSampleStyleSheet()
    Story = []
    
    toc = TableOfContents()
    # Customise the level styles (optional)
    toc.levelStyles = [
        ParagraphStyle(fontName='Times-Bold', fontSize=14, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=5, leading=16),
        ParagraphStyle(fontName='Times-Roman', fontSize=12, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),
    ]
    Story.append(toc)
    Story.append(PageBreak())
    
    # Add some headings and text
    for i in range(1, 4):
        heading = Paragraph(f'Chapter {i} Heading', styles['Heading1'])
        Story.append(heading)
        for j in range(1, 4):
            sub_heading = Paragraph(f'Section {j} Heading', styles['Heading2'])
            Story.append(sub_heading)
            text = Paragraph('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.', styles['BodyText'])
            Story.append(text)
        Story.append(PageBreak())
    
    doc.build(Story)

# Specify the filename and path
filename = './tmp/structured_document.pdf'
build_pdf(filename)