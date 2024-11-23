import os

def generate_pnm_file(file_name, content):
    file_path = f"./tmp/{file_name}.pnm"
    with open(file_path, 'w') as file:
        file.write(content)

def create_pnm_file_with_textual_representation():
    pnm_content = """P3
# This is a PNM file with textual representation
3 2
255
255 0 0   0 255 0   0 0 255
255 255 255 255 255 0 255 0 255"""
    
    generate_pnm_file("textual_representation", pnm_content)

if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

create_pnm_file_with_textual_representation()