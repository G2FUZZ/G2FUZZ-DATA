import os

def generate_pnm_file(file_name):
    header = "P3\n# Simple Structure: PNM files have a simple structure with a header containing format information followed by pixel data.\n2 2\n255\n"
    pixel_data = "255 0 0\n0 255 0\n0 0 255\n255 255 0\n"

    with open(file_name, 'w') as f:
        f.write(header)
        f.write(pixel_data)

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

file_name = './tmp/sample.pnm'
generate_pnm_file(file_name)
print(f'Generated PNM file: {file_name}')