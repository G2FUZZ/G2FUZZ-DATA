import struct
import os

def create_tga_file(image_origin, file_name):
    header = bytearray([0]*18)
    header[2] = 2  # Image type: Uncompressed RGB
    header[12:14] = struct.pack('<H', image_origin[0])
    header[14:16] = struct.pack('<H', image_origin[1])
    header[16] = 24  # Pixel depth: 24 bits per pixel

    with open(file_name, 'wb') as f:
        f.write(header)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

image_origin = (10, 10)
file_name = './tmp/image.tga'
create_tga_file(image_origin, file_name)