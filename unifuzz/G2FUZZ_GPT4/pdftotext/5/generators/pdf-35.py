from fpdf import FPDF
import os

# Create a directory to save PDF files if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# PDF class with metadata, transparency, and color space support
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document with Metadata, Transparency, and Color Spaces', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def set_alpha(self, alpha, blend_mode='Normal'):
        """Set alpha for transparency support."""
        if alpha < 1:
            self._out(f'/GS gs /{blend_mode} BM')
        self._out(f'{alpha:.3f} gs')

    def set_color_space(self, color_space, colors):
        """Set color space and color for drawing."""
        if color_space == 'RGB':
            self.set_text_color(*colors)
        elif color_space == 'CMYK':
            c, m, y, k = colors
            # Convert CMYK to RGB as FPDF does not support CMYK for text directly
            r = 255 * (1-c) * (1-k)
            g = 255 * (1-m) * (1-k)
            b = 255 * (1-y) * (1-k)
            self.set_text_color(r, g, b)
        # Add more color spaces if needed

# Create PDF object
pdf = PDF()
pdf.add_page()

# Set metadata
pdf.set_title('Sample PDF with Transparency and Color Spaces')
pdf.set_author('John Doe')
pdf.set_subject('PDF Generation with Transparency and Color Spaces')
pdf.set_keywords('PDF, Python, Metadata, Transparency, Color Spaces')

# Add content with RGB color space
pdf.set_font("Arial", size=12)
pdf.set_color_space('RGB', (0, 102, 204))  # Set text color in RGB
pdf.cell(0, 10, 'This text is in RGB color space.', ln=True)

# Add content with CMYK color space
pdf.set_color_space('CMYK', (0, 0.439216, 0.803921, 0.196078))  # Set text color in CMYK
pdf.cell(0, 10, 'This text is simulated in CMYK color space.', ln=True)

# Add transparency support (for demonstration purposes, use it without an image here)
pdf.set_fill_color(200, 220, 255)  # Light blue background
pdf.set_alpha(0.5)  # 50% transparent
pdf.rect(50, 50, 100, 100, 'F')  # Draw semi-transparent rectangle

# Reset transparency for normal content
pdf.set_alpha(1)
pdf.set_font("Arial", size=12)
pdf.ln(110)  # Move below the transparent rectangle
pdf.cell(0, 10, 'Below the rectangle, transparency is reset to fully opaque.', ln=True)

# Save the PDF to a file
pdf_file_path = os.path.join(output_dir, "document_with_transparency_and_color_spaces.pdf")
pdf.output(pdf_file_path)

print(f"PDF with metadata, transparency, and color spaces has been created: {pdf_file_path}")