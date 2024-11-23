from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import PCMYKColor

# Define the PDF file path
pdf_file_path = './tmp/multimedia_color_pdf.pdf'

# Create a canvas
c = canvas.Canvas(pdf_file_path, pagesize=LETTER)

# Add some text to introduce the link
c.drawString(100, 750, 'Click below to view the video:')

# Embed a hyperlink to a video (or any multimedia content)
video_url = 'http://www.example.com/path/to/your/video.mp4'
c.drawString(100, 730, video_url)

# You can also use the linkURL method from reportlab to make the text act as a hyperlink
c.linkURL(url=video_url, rect=(100, 720, 300, 735), thickness=0, relative=1)

# Device-independent Color feature
# Here we use CMYK color for drawing shapes or text, which is device-independent
# Drawing a rectangle with CMYK color
c.setFillColor(PCMYKColor(0, 100, 100, 0))  # Cyan color
c.rect(100, 600, 200, 100, fill=1)

# Adding text with a different CMYK Color
c.setFillColor(PCMYKColor(0, 0, 100, 0))  # Yellow Color
c.drawString(100, 580, 'Device-independent Color: CMYK example')

# Save the PDF
c.save()