from fpdf import FPDF
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Text, Fonts, Attachments, Non-rectangular Links, and Mobile Optimization Embedding', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_attachment(self, file_path):
        # Placeholder for attachment embedding functionality
        pass

    def add_non_rectangular_link(self, link, x, y, w, h):
        # This method simulates adding a non-rectangular link by using an invisible rectangle for demonstration purposes.
        self.set_text_color(0,0,255)  # Set text color to blue for the link
        self.set_font('Arial', 'U', 12)
        self.text(x,y,link)
        self.link(x, y - 10, w, h, link)

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_title("Text, Fonts, Attachments, Non-rectangular Links, and Mobile Optimization Embedding")

# Add a chapter for Text and Fonts Embedding
pdf.chapter_title("Chapter 1: Introduction to Fonts Embedding")
pdf.chapter_body("PDF files can encapsulate not only the textual content but also the specific fonts used, ensuring that documents appear the same on any device or software platform. This feature is crucial for preserving the document's intended appearance, regardless of where or how it's viewed. Embedding fonts within PDFs ensures that text is displayed consistently, maintaining the design and layout integrity of the document.")

# Add a chapter for Attachments
pdf.chapter_title("Chapter 2: Attachments")
pdf.chapter_body("PDFs can include other files as attachments within the document, allowing for the bundling of related documents and resources. This facilitates the distribution of comprehensive information packets that include supplementary materials like data sheets, terms and conditions, or other pertinent documents. However, incorporating attachments directly into PDFs requires features not supported by the FPDF library used in this script, necessitating alternative solutions or libraries.")

# Add a chapter for Non-rectangular Links
pdf.chapter_title("Chapter 3: Non-rectangular Links")
pdf.chapter_body("Non-rectangular Links: They support links and hotspots that are not just rectangular but can be of any shape, enhancing the flexibility of interactive elements in PDF documents. This feature allows for more dynamic and interactive documents, providing users with the ability to interact with content in a more intuitive and engaging manner. However, creating truly non-rectangular links requires more advanced PDF features not supported by FPDF, necessitating alternative approaches or libraries for full implementation.")

# Add a chapter for Mobile Optimization
pdf.chapter_title("Chapter 4: Mobile Optimization")
pdf.chapter_body("Mobile Optimization: Some PDFs are optimized for mobile viewing, ensuring that they are easily readable on smaller screens with limited resources. Optimizing PDFs for mobile devices is crucial in today's digital world, where a significant portion of users access content via smartphones and tablets. This optimization includes considerations like reduced file size, responsive design, and readability on smaller screens to ensure the best possible user experience.")

# Demonstration of adding a "non-rectangular" link (simplified)
pdf.add_non_rectangular_link("Click here for more information", 10, 50, 100, 10)

# Save the pdf file
pdf.output(f"{output_dir}text_fonts_attachments_non_rectangular_links_and_mobile_optimization_embedding.pdf")