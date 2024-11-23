import struct

def create_tga_file_with_alpha_channel(filename):
    width = 100
    height = 100
    pixel_data = b'\xFF\x00\x00\x80' * (width * height)  # Red pixels with varying alpha values
    
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10,  # Image type - RLE compressed true-color image with alpha
        0, 0, 0, 0, 0,  # Color map specification
        0, 0, 0, 0,  # Image specification
        width & 0xFF, (width >> 8) & 0xFF,
        height & 0xFF, (height >> 8) & 0xFF,
        32,  # Pixel depth
        8  # Image descriptor
    ])

    with open(filename, 'wb') as f:
        f.write(header)
        f.write(pixel_data)

filename = './tmp/sample_with_alpha.tga'
create_tga_file_with_alpha_channel(filename)
print(f'TGA file with alpha channel created: {filename}')