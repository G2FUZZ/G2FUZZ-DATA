import os

def generate_tga_file(file_name):
    header = bytearray([0] * 18)
    header[2] = 2  # Image type: 2 for uncompressed true-color image
    header[12] = 128  # Image width (low byte)
    header[13] = 1  # Image width (high byte)
    header[14] = 96  # Image height (low byte)
    header[15] = 0  # Image height (high byte)
    header[16] = 24  # Pixel depth: 24 bits per pixel

    with open(file_name, 'wb') as f:
        f.write(header)

    print(f"TGA file '{file_name}' has been generated.")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = './tmp/example.tga'
generate_tga_file(file_name)