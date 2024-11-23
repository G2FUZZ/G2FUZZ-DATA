from fpdf import FPDF
import os

# Create a directory to save PDF files if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF class with metadata and transparency support
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document with Metadata and Transparency', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def set_alpha(self, alpha, blend_mode='Normal'):
        """Set alpha for transparency support."""
        if alpha < 1:
            self._out(f'/GS gs /{blend_mode} BM')
        self._out(f'{alpha:.3f} gs')

# Create PDF object
pdf = PDF()
pdf.add_page()

# Set metadata
pdf.set_title('Sample PDF with Transparency')
pdf.set_author('John Doe')
pdf.set_subject('PDF Generation with Transparency')
pdf.set_keywords('PDF, Python, Metadata, Transparency')

# Add content
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, 'This PDF contains document metadata, such as author, title, subject, and keywords. It also supports transparency.', ln=True)

# Add transparency support (for demonstration purposes, we use it without an image here)
pdf.set_fill_color(200, 220, 255)  # Light blue background
pdf.set_alpha(0.5)  # 50% transparent
pdf.rect(50, 50, 100, 100, 'F')  # Draw semi-transparent rectangle

# Reset transparency for normal content
pdf.set_alpha(1)
pdf.set_font("Arial", size=12)
pdf.ln(110)  # Move below the transparent rectangle
pdf.cell(0, 10, 'Below the rectangle, transparency is reset to fully opaque.', ln=True)

# Save the PDF to a file
pdf_file_path = os.path.join(output_dir, "document_with_transparency.pdf")
pdf.output(pdf_file_path)

print(f"PDF with metadata and transparency has been created: {pdf_file_path}")