from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Create a new PDF with ReportLab
c = canvas.Canvas(os.path.join(output_dir, "interactive_form_with_rich_text_elements.pdf"), pagesize=letter)
c.drawString(100, 750, "Interactive Form with Articles and Rich Text Elements")

# Define an article with two threads in a single page document for demonstration
c.drawString(100, 700, "Article Start: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
c.drawString(100, 685, "Continues on page 2...")

# Save the current state and start a new page
c.showPage()
c.drawString(100, 750, "Article Continuation")
c.drawString(100, 700, "Continuation: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
c.drawString(100, 685, "End of Article.")

# Now, demonstrating Rich Text Elements
text = '''<para autoLeading="off" fontSize=12>
<b>This is a title in bold</b>
<br/><font color=red>This is some red text.</font>
<br/><b><font color=blue>This is some blue and bold text.</font></b>
<br/><u>This is underlined text.</u>
<br/><bullet>&bull;</bullet> A bullet point.
</para>'''

# Create a Frame to hold the Paragraph
styles = getSampleStyleSheet()
story = [Paragraph(text, style=styles["Normal"])]
frame = Frame(100, 400, 400, 200, showBoundary=1)

# Save the current state, add the rich text, and restore the state
c.saveState()
frame.addFromList(story, c)
c.restoreState()

# Save the canvas
c.save()

print(f"Interactive PDF form with articles and rich text elements has been created at: {os.path.join(output_dir, 'interactive_form_with_rich_text_elements.pdf')}")