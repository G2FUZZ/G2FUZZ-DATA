import os

def create_bmp(filename, width, height, pixels_per_meter_horizontal, pixels_per_meter_vertical):
    # BMP Header
    bmp_header = bytearray([
        0x42, 0x4D,           # BM
        0x36, 0x28, 0x00, 0x00, # File size (will be set later)
        0x00, 0x00,           # Unused
        0x00, 0x00,           # Unused
        0x36, 0x00, 0x00, 0x00  # Offset where the pixel array (bitmap data) can be found
    ])

    # DIB Header (BITMAPINFOHEADER)
    dib_header = bytearray([
        0x28, 0x00, 0x00, 0x00, # Number of bytes in the DIB header (40 bytes)
        0x00, 0x00, 0x00, 0x00, # Width of the bitmap in pixels
        0x00, 0x00, 0x00, 0x00, # Height of the bitmap in pixels
        0x01, 0x00,             # Number of color planes being used
        0x18, 0x00,             # Number of bits per pixel
        0x00, 0x00, 0x00, 0x00, # BI_RGB, no pixel array compression used
        0x00, 0x00, 0x00, 0x00, # Size of the raw bitmap data (including padding)
        0x00, 0x00, 0x00, 0x00, # Print resolution of the image, in pixels per meter (horizontal)
        0x00, 0x00, 0x00, 0x00, # Print resolution of the image, in pixels per meter (vertical)
        0x00, 0x00, 0x00, 0x00, # Number of colors in the palette
        0x00, 0x00, 0x00, 0x00  # 0 means all colors are important
    ])

    # Set width and height in DIB header
    dib_header[4:8] = width.to_bytes(4, byteorder='little')
    dib_header[8:12] = height.to_bytes(4, byteorder='little')

    # Set the resolution in pixels per meter
    dib_header[24:28] = pixels_per_meter_horizontal.to_bytes(4, byteorder='little')
    dib_header[28:32] = pixels_per_meter_vertical.to_bytes(4, byteorder='little')

    # Pixel data (simple pattern just for demonstration)
    row_size = (width * 3 + 3) & ~3  # Row size must be a multiple of 4 bytes
    pixel_data_size = row_size * height
    pixel_data = bytearray([0xFF, 0xFF, 0xFF] * width * height)

    # Update file size in BMP header
    file_size = 14 + 40 + pixel_data_size  # BMP Header size + DIB Header size + Pixel data
    bmp_header[2:6] = file_size.to_bytes(4, byteorder='little')

    # Write the BMP file
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(pixel_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a BMP file with specific resolution
create_bmp('./tmp/test_image.bmp', 100, 100, 3780, 3780)  # 3780 pixels per meter is approximately 96 DPI