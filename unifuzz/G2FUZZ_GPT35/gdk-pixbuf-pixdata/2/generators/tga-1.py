import numpy as np
import struct

def create_tga_file(width, height, color_depth, file_path):
    # Define TGA header
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, color_depth, 0])

    # Generate random pixel data based on color depth
    if color_depth == 8:
        pixel_data = np.random.randint(256, size=(height, width), dtype=np.uint8)
    elif color_depth == 16:
        pixel_data = np.random.randint(65536, size=(height, width), dtype=np.uint16)
    elif color_depth == 24:
        pixel_data = np.random.randint(256, size=(height, width, 3), dtype=np.uint8)
    elif color_depth == 32:
        pixel_data = np.random.randint(256, size=(height, width, 4), dtype=np.uint8)

    # Write pixel data to file
    with open(file_path, 'wb') as f:
        f.write(header)
        if color_depth == 8 or color_depth == 16:
            f.write(pixel_data.tobytes())
        elif color_depth == 24 or color_depth == 32:
            f.write(pixel_data.transpose(1, 0, 2).tobytes())

# Generate and save TGA files
create_tga_file(256, 256, 8, './tmp/8bit_grayscale.tga')
create_tga_file(256, 256, 16, './tmp/16bit_grayscale.tga')
create_tga_file(256, 256, 24, './tmp/24bit_rgb.tga')
create_tga_file(256, 256, 32, './tmp/32bit_rgba.tga')