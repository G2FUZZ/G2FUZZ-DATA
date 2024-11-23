from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
from reportlab.pdfbase import pdfdoc

# Create a PDF file with annotations and file attachments
def create_pdf_with_annotations_and_attachments(file_path, attachment_path):
    c = canvas.Canvas(file_path)
    c.drawString(100, 700, "This is a PDF file with annotations and file attachments.")
    c.drawString(100, 600, "Users can add comments, highlights, and annotations to this document.")
    c.drawString(100, 500, "Enjoy annotating!")
    
    # Add file attachment
    c.setPageCompression(True)
    c.setEncrypt(pdfencrypt.StandardEncryption("password"))
    
    try:
        with open(attachment_path, "rb") as file:
            attachment = file.read()
            c._doc.addAttachment("Additional Document", attachment)
    except FileNotFoundError:
        print(f"Error: File '{attachment_path}' not found.")

    c.showPage()
    c.save()

# Save the PDF file with annotations and file attachments
file_name = "./tmp/pdf_with_annotations_and_attachments.pdf"
attachment_file_path = "./attachments/sample_attachment.pdf"
create_pdf_with_annotations_and_attachments(file_name, attachment_file_path)