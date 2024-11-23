from reportlab.pdfgen import canvas

# Create a PDF file with encryption
c = canvas.Canvas("./tmp/encrypted_pdf.pdf", encrypt="password")
c.drawString(100, 700, "This is an encrypted PDF file.")
c.save()