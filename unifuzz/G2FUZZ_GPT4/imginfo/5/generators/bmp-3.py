import os

def create_bmp_with_rle_compression(filename):
    # BMP Header (14 bytes)
    bmp_header = bytes([
        0x42, 0x4D,  # Signature "BM"
        0x76, 0x00, 0x00, 0x00,  # File size in bytes (118 bytes here)
        0x00, 0x00,  # Reserved
        0x00, 0x00,  # Reserved
        0x36, 0x00, 0x00, 0x00  # Start of pixel array (54 bytes offset)
    ])

    # DIB Header (BITMAPINFOHEADER, 40 bytes)
    dib_header = bytes([
        0x28, 0x00, 0x00, 0x00,  # DIB Header size (40 bytes)
        0x08, 0x00, 0x00, 0x00,  # Width: 8 pixels
        0x08, 0x00, 0x00, 0x00,  # Height: 8 pixels (positive for bottom-to-top)
        0x01, 0x00,  # Planes: 1
        0x08, 0x00,  # Bits per pixel: 8 (256 colors)
        0x01, 0x00, 0x00, 0x00,  # Compression: RLE 8-bit/pixel
        0x40, 0x00, 0x00, 0x00,  # Size of the raw data in the pixel array (including padding)
        0x13, 0x0B, 0x00, 0x00,  # Horizontal resolution: 2835 pixels/meter (72 DPI)
        0x13, 0x0B, 0x00, 0x00,  # Vertical resolution: 2835 pixels/meter (72 DPI)
        0x00, 0x00, 0x00, 0x00,  # Number of colors in the palette: 0 (default to 256)
        0x00, 0x00, 0x00, 0x00   # Important colors: 0 (all)
    ])

    # Color Palette: Simple grayscale palette (256 colors)
    color_palette = bytes([item for i in range(256) for item in [i, i, i, 0]])

    # Pixel Data with simple RLE compression
    pixel_data = bytes([
        0x08, 0x00,  # Row 1: 8 pixels of color 0
        0x08, 0x07,  # Row 2: 8 pixels of color 7
        0x08, 0x0F,  # Row 3: 8 pixels of color 15
        0x08, 0x17,  # Row 4: 8 pixels of color 23
        0x08, 0x1F,  # Row 5: 8 pixels of color 31
        0x08, 0x27,  # Row 6: 8 pixels of color 39
        0x08, 0x2F,  # Row 7: 8 pixels of color 47
        0x08, 0x37,  # Row 8: 8 pixels of color 55
        0x00, 0x00,  # End of line
        0x00  # End of RLE bitmap
    ])

    # Ensure the target directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Write the BMP file
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(color_palette)
        f.write(pixel_data)

# Create a BMP with RLE compression
create_bmp_with_rle_compression('./tmp/rle_compressed.bmp')