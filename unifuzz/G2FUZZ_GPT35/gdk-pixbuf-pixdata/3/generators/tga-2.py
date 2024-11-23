import os

def create_tga_file(compression, filename):
    header = bytearray([0] * 18)
    header[2] = 10  # Image type: True-color, uncompressed
    header[16] = 640 % 256  # Image width
    header[17] = 640 // 256  # Image width
    header[12] = 480 % 256  # Image height
    header[13] = 480 // 256  # Image height
    header[17] = 32  # Pixel depth

    if compression == 'RLE':
        header[2] = 11  # Image type: True-color, RLE encoded

    with open(filename, 'wb') as f:
        f.write(header)

        # Write image data here...

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

create_tga_file('uncompressed', './tmp/uncompressed_image.tga')
create_tga_file('RLE', './tmp/compressed_image.tga')