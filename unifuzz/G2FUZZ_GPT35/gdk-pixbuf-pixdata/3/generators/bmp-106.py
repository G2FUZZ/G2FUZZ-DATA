import os
from struct import pack

def create_advanced_bmp_file():
    # BMP file header
    file_header = b'BM'
    file_size = 170  # File size = image data size (144) + headers size (26)
    reserved = 0  # Convert bytes to integer
    data_offset = 170  # Offset to start of image data

    # BMP info header
    header_size = 108  # Size of info header
    img_width = 8
    img_height = 8
    planes = 1
    bits_per_pixel = 32  # 32-bit RGBA
    compression = 3  # BI_BITFIELDS
    img_size = 256  # Image data size = 8x8 pixels * 4 bytes per pixel

    # Color palette
    color_palette = bytearray([255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 0, 255, 255, 255, 0])  # RGBA values

    bmp_header = pack('<2sIHHI', file_header, file_size, reserved, data_offset, header_size)
    bmp_info = pack('<IIIHHIIIIII', header_size, img_width, img_height, planes, bits_per_pixel, compression,
                    img_size, 0, 0, 0, 0)

    # Image data with transparency
    image_data = bytearray([255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255,
                            255, 255, 255, 255, 0, 0, 0, 0, 0, 255, 255, 0,
                            255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255,
                            255, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255,
                            255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255, 255,
                            255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255,
                            255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0])

    # Create BMP file with advanced features
    with open('./tmp/advanced_bmp.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(bmp_info)
        f.write(color_palette)
        f.write(image_data)

# Create advanced BMP file
create_advanced_bmp_file()