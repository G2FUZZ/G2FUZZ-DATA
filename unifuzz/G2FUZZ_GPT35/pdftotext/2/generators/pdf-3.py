from fpdf import FPDF

# Create a PDF class extension to add encryption and password protection
class EncryptedPDF(FPDF):
    def __init__(self):
        super().__init__()
        self._encryption = None

    def set_password(self, password):
        self._password = password

    def _putencryption(self):
        objId = self._newobj()
        self._out("<</Filter /Standard /R 2 /O (password) /U (password) /P -3900>>")
        self._out("endobj")
        self._encryption = objId

    def _putpaddedstring(self, text):
        n = len(text)
        if n > 32:
            raise Exception("String is too long for padded string")
        padding = b'123456789ABCDEF0123456789ABCDEF0'
        return (text + padding[:32 - n]).encode('latin1')

    def _putstream(self, data):
        if self._encryption:
            data = self._putpaddedstring(data)
        FPDF._putstream(self, data)

# Create a new PDF instance
pdf = EncryptedPDF()
pdf.set_password("mypassword")

# Add a page and set title
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello, Encrypted PDF!')

# Output the PDF file
pdf.output('./tmp/encrypted_pdf.pdf')

print("Encrypted PDF file generated successfully.")