import os

def generate_pnm_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

content = "8. Widely Supported: PNM files are supported by a wide range of image processing software and libraries."

filename = './tmp/generated_file.pnm'
generate_pnm_file(content, filename)

print(f"File '{filename}' generated successfully.")