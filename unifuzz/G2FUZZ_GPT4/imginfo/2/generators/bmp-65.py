import struct
import os

def create_bmp(filename, width, height):
    # BMP file format constants
    file_type = b'BM'  # BM indicates a bitmap
    pixel_data_offset = 54  # Standard offset to pixel data for 24-bit BMPs
    header_size = 40  # DIB header size for BITMAPINFOHEADER
    planes = 1  # Number of color planes
    bits_per_pixel = 24  # 24-bit BMP
    compression = 0  # BI_RGB, no compression
    image_size = width * height * 3  # Size of the raw bitmap data
    x_pixels_per_meter = 2835  # Horizontal resolution: 72 DPI * 39.3701 inches per meter
    y_pixels_per_meter = 2835  # Vertical resolution: 72 DPI * 39.3701 inches per meter
    total_colors = 0  # Maximum number of colors (0 for 24-bit BMP)
    important_colors = 0  # All colors are important

    # Calculate the size of the file
    file_size = pixel_data_offset + image_size

    # Create a BMP header
    bmp_header = struct.pack('<2sIHHI', file_type, file_size, 0, 0, pixel_data_offset)

    # Create a DIB header
    dib_header = struct.pack('<IIIHHIIIIII', header_size, width, height, planes, bits_per_pixel,
                             compression, image_size, x_pixels_per_meter, y_pixels_per_meter,
                             total_colors, important_colors)

    # Open the file to write binary data
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)

        # Generate and write pixel data: simple blue-to-red gradient
        for y in range(height):
            for x in range(width):
                red = int(x / width * 255)
                green = 0
                blue = int((width - x) / width * 255)
                # BMP uses little-endian ordering
                f.write(struct.pack('<BBB', blue, green, red))
            # Pad each row to a multiple of 4 bytes
            padding = (4 - (width * 3) % 4) % 4
            f.write(b'\x00' * padding)

    print(f"{filename} created with dimensions {width}x{height}.")

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a BMP file
create_bmp('./tmp/complex_structure.bmp', 200, 100)