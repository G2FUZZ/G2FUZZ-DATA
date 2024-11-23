import os
from struct import pack

def create_bmp_with_compression():
    # BMP file header
    file_header = b'BM'
    file_size = 154  # File size = image data size (144) + headers size (10)
    reserved = 0  # Convert bytes to integer
    data_offset = 154  # Offset to start of image data

    # BMP info header
    header_size = 40  # Size of info header
    img_width = 4
    img_height = 4
    planes = 1
    bits_per_pixel = 24  # 24-bit RGB
    compression = 3  # BI_BITFIELDS
    img_size = 144  # Image data size = 4x4 pixels * 3 bytes per pixel

    bmp_header = pack('<2sIHHI', file_header, file_size, reserved, data_offset, header_size)
    bmp_info = pack('<IIIHHIIIIII', header_size, img_width, img_height, planes, bits_per_pixel, compression,
                    img_size, 0, 0, 0, 0)

    # Image data
    image_data = bytearray([0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 0, 255,
                            255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0,
                            255, 255, 255, 255, 0, 0, 255, 0, 0, 0, 0, 0])

    # Create BMP file
    with open('./tmp/compressed_bmp.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(bmp_info)
        f.write(image_data)

# Create BMP file with compression
create_bmp_with_compression()