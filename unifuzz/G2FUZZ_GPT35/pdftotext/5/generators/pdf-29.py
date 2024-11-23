from reportlab.pdfgen import canvas
from reportlab.lib.colors import green

class CustomLayeredPDFGenerator:
    def add_background_layer(self, c):
        c.setFillColorRGB(0.8, 0.8, 0.8)
        c.rect(0, 0, 400, 400, fill=1, stroke=0)
        c.drawString(10, 380, "Background Layer")

    def add_foreground_layer(self, c):
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.rect(50, 50, 300, 300, fill=1, stroke=0)
        c.drawString(60, 320, "Foreground Layer")

    def add_watermark(self, c, text):
        c.setFont("Helvetica", 36)
        c.setFillAlpha(0.3)
        c.saveState()
        c.rotate(45)
        c.drawString(200, 200, text)
        c.restoreState()

    def add_digital_signature(self, c, text):
        c.setStrokeColor(green)
        c.setLineWidth(2)
        c.line(100, 100, 300, 100)
        c.drawString(100, 80, f"Digital Signature: {text}")

    def generate_layered_pdf_with_watermark_and_signature(self, file_name, watermark_text, signature_text):
        c = canvas.Canvas(f'./tmp/{file_name}.pdf')
        self.add_background_layer(c)
        self.add_foreground_layer(c)
        self.add_watermark(c, watermark_text)
        self.add_digital_signature(c, signature_text)
        c.save()

pdf_generator = CustomLayeredPDFGenerator()
pdf_generator.generate_layered_pdf_with_watermark_and_signature('custom_layered_pdf', 'Confidential', 'Jane Doe')