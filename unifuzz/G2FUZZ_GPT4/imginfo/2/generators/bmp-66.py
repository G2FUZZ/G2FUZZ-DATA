import struct
import os

def create_mono_bmp(filename, width, height):
    # Constants for a 1-bit BMP
    file_type = b'BM'
    pixel_data_offset = 62  # 54 for the headers + 8 for the color palette
    header_size = 40
    planes = 1
    bits_per_pixel = 1
    compression = 0
    image_size = ((width + 31) // 32) * 4 * height  # Rounded up to nearest multiple of 32 bits (4 bytes) per row
    x_pixels_per_meter = 2835
    y_pixels_per_meter = 2835
    total_colors = 2  # Black and White
    important_colors = 2
    file_size = pixel_data_offset + image_size
    bmp_header = struct.pack('<2sIHHI', file_type, file_size, 0, 0, pixel_data_offset)
    dib_header = struct.pack('<IIIHHIIIIII', header_size, width, height, planes, bits_per_pixel,
                             compression, image_size, x_pixels_per_meter, y_pixels_per_meter,
                             total_colors, important_colors)
    # Black and White color palette
    color_palette = b'\x00\x00\x00\x00' + b'\xFF\xFF\xFF\x00'  # Black and White

    # Create pixel data
    pixel_data = bytearray(image_size)
    for y in range(35, 65):
        for x in range(35, 65):
            index = x + y * width
            byte_index = index // 8
            bit_index = 7 - (index % 8)
            pixel_data[byte_index] |= 1 << bit_index

    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(color_palette)
        f.write(pixel_data)

def create_rgb_bmp(filename, width, height, color, square_color):
    # Constants for a 24-bit BMP
    file_type = b'BM'
    pixel_data_offset = 54
    header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = width * height * 3
    x_pixels_per_meter = 2835
    y_pixels_per_meter = 2835
    total_colors = 0
    important_colors = 0
    file_size = pixel_data_offset + image_size
    bmp_header = struct.pack('<2sIHHI', file_type, file_size, 0, 0, pixel_data_offset)
    dib_header = struct.pack('<IIIHHIIIIII', header_size, width, height, planes, bits_per_pixel,
                             compression, image_size, x_pixels_per_meter, y_pixels_per_meter,
                             total_colors, important_colors)

    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)

        # Generate and write pixel data
        for y in range(height):
            for x in range(width):
                if 35 <= x < 65 and 35 <= y < 65:
                    f.write(struct.pack('<BBB', square_color[2], square_color[1], square_color[0]))
                else:
                    f.write(struct.pack('<BBB', color[2], color[1], color[0]))
            padding = (4 - (width * 3) % 4) % 4
            f.write(b'\x00' * padding)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 1-bit monochrome BMP
create_mono_bmp('./tmp/monochrome_muted.bmp', 100, 100)

# Create a 24-bit true color BMP
create_rgb_bmp('./tmp/truecolor_24bit_muted.bmp', 100, 100, (135, 206, 235), (255, 0, 0))  # skyblue and red

# The 32-bit true color with alpha BMP creation is omitted as the BMP format in its basic form does not support alpha channels in a straightforward manner without utilizing newer BMP versions or compression techniques.