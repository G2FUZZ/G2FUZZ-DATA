import os

def create_bmp(filename, width, height, color):
    # BMP file header (14 bytes)
    file_header = bytearray([
        0x42, 0x4D,             # Signature "BM"
        0x36, 0x28, 0x00, 0x00, # File size in bytes
        0x00, 0x00,             # Reserved
        0x00, 0x00,             # Reserved
        0x36, 0x00, 0x00, 0x00  # Start of pixel array
    ])

    # DIB header (BITMAPINFOHEADER, 40 bytes)
    dib_header = bytearray([
        0x28, 0x00, 0x00, 0x00, # Header size
        width & 0xFF, (width >> 8) & 0xFF, 0x00, 0x00, # Image width
        height & 0xFF, (height >> 8) & 0xFF, 0x00, 0x00, # Image height
        0x01, 0x00,             # Number of color planes
        0x18, 0x00,             # Bits per pixel (24bpp)
        0x00, 0x00, 0x00, 0x00, # Compression (no compression)
        0x00, 0x28, 0x00, 0x00, # Image size (no compression)
        0x12, 0x0B, 0x00, 0x00, # Horizontal resolution (2835 ppm)
        0x12, 0x0B, 0x00, 0x00, # Vertical resolution (2835 ppm)
        0x00, 0x00, 0x00, 0x00, # Colors in color table (0 = default to 2^n)
        0x00, 0x00, 0x00, 0x00  # Important colors (0 = all)
    ])

    # Create the pixel data
    pixels = bytearray()
    for y in range(height):
        for x in range(width):
            # Simple pattern: R, G, B values derived from coordinates
            pixels.append((x + y) % 256)  # Blue
            pixels.append(x % 256)       # Green
            pixels.append(y % 256)       # Red
        # Padding for 4-byte alignment
        while len(pixels) % 4 != 0:
            pixels.append(0)

    # Combine all parts
    bmp = file_header + dib_header + pixels

    # Write to file
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'wb') as f:
        f.write(bmp)

# Create a BMP file
create_bmp('./tmp/generated_image.bmp', 100, 100, (0, 0, 255))