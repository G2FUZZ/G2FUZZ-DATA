import os

class MIFGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contents = []

    def add_header(self, version="9.00"):
        self.contents.append(f"<MIFFile {version}>")
        self.contents.append("<Units Ucm>")

    def start_text_flow(self, id, tag='Body'):
        self.contents.append(f"<TextFlow <ID {id}> <TFTag `{tag}'>")

    def end_text_flow(self):
        self.contents.append("> # End TextFlow")

    def add_paragraph(self, text, style='BodyText'):
        self.contents.append(f"    <Para <PgfTag `{style}'>")
        self.contents.append(f"        <String `{text}'> >")

    def add_hyperlink(self, text_before, url, text_after, new_win='No'):
        self.contents.append(f"        <String `{text_before}'>")
        self.contents.append("        <Hypertext")
        self.contents.append(f"            <AType `GoToURL'>")
        self.contents.append(f"            <URL `{url}'>")
        self.contents.append(f"            <NewWin {new_win}> >")
        self.contents.append(f"        <String `{text_after}'> >")

    def add_page(self, id, attributes=''):
        self.contents.append(f"<Page <ID {id}> {attributes}")
        self.contents.append("> # End Page")

    def add_image(self, image_path, width, height):
        self.contents.append("    <Frame")
        self.contents.append(f"        <ImportObject")
        self.contents.append(f"            <DIFile `{image_path}'>")
        self.contents.append(f"            <Dpi 300>")
        self.contents.append(f"            <BRect {width} {height} 0 0>")
        self.contents.append("        > # End ImportObject")
        self.contents.append("    > # End Frame")

    def save(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        # Save the content to a .mif file
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(self.contents).strip())

        print(f'MIF file created at: {self.file_path}')

# Usage example
file_path = './tmp/complex_example.mif'
mif_generator = MIFGenerator(file_path)

mif_generator.add_header()
mif_generator.start_text_flow(1)
mif_generator.add_paragraph("Welcome to our documentation.", "Heading1")
mif_generator.add_hyperlink("For detailed info, visit ", "http://www.example.com", "our site.", "Yes")
mif_generator.end_text_flow()

mif_generator.start_text_flow(2, "Info")
mif_generator.add_paragraph("This document is generated.", "InfoText")
mif_generator.end_text_flow()

mif_generator.add_page(1, "# First page attributes here")
mif_generator.add_image("./images/logo.png", "5 cm", "2 cm")
mif_generator.add_page(2, "# Second page attributes here")

mif_generator.save()