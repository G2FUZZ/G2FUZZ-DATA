from fpdf import FPDF, HTMLMixin
import os

class MyPDF(FPDF, HTMLMixin):
    pass

def create_interactive_pdf():
    # Ensure the tmp directory exists
    os.makedirs("./tmp", exist_ok=True)
    
    pdf = MyPDF()
    pdf.add_page()
    
    # Adding a hyperlink
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'U', 12)
    pdf.write(10, 'Click here to go to Google', 'http://www.google.com')
    
    # Unfortunately, adding more complex interactive elements like form fields and buttons directly 
    # requires more advanced libraries such as ReportLab or integrating with PDF forms features from other tools.
    # This example focuses on the hyperlink as an interactive element, which is supported by FPDF.
    
    pdf.output('./tmp/interactive_pdf.pdf')

if __name__ == '__main__':
    create_interactive_pdf()