from fpdf import FPDF

class PDFWithEncryption(FPDF):
    def set_encryption(self, user_pwd='', owner_pwd=None, use_128bit=True):
        if owner_pwd is None:
            owner_pwd = user_pwd
        super().set_encryption(user_pwd, owner_pwd, use_128bit)

# Create a PDF file with encryption
pdf = PDFWithEncryption()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "This is an encrypted PDF file", 0, 1)

output_file = "./tmp/encrypted_pdf_file.pdf"
pdf.output(output_file, "F")

print(f"Encrypted PDF file created: {output_file}")