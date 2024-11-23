import os

def create_bmp(filename, width, height):
    # Bitmap file header
    file_header = bytearray([
        0x42, 0x4D,         # BM
        0x7A, 0x00, 0x00, 0x00, # File size in bytes
        0x00, 0x00,         # Reserved
        0x00, 0x00,         # Reserved
        0x7A, 0x00, 0x00, 0x00  # Start of pixel array
    ])
    
    # DIB header (BITMAPINFOHEADER)
    dib_header = bytearray([
        0x6C, 0x00, 0x00, 0x00, # Header size
        width & 0xFF, (width >> 8) & 0xFF, 0x00, 0x00, # Image width
        height & 0xFF, (height >> 8) & 0xFF, 0x00, 0x00, # Image height
        0x01, 0x00,         # Number of color planes
        0x20, 0x00,         # Bits per pixel
        0x03, 0x00, 0x00, 0x00, # Compression (3 = BITFIELDS)
        0x00, 0x00, 0x00, 0x00, # Image size (can be 0 for BI_RGB bitmaps)
        0x13, 0x0B, 0x00, 0x00, # Horizontal resolution (pixels per meter)
        0x13, 0x0B, 0x00, 0x00, # Vertical resolution (pixels per meter)
        0x00, 0x00, 0x00, 0x00, # Colors in color table (0 = all colors)
        0x00, 0x00, 0x00, 0x00, # Important color count (0 = all colors)
        0x00, 0x00, 0xFF, 0x00, # Red channel bitmask (little endian)
        0x00, 0xFF, 0x00, 0x00, # Green channel bitmask (little endian)
        0xFF, 0x00, 0x00, 0x00, # Blue channel bitmask (little endian)
        0x00, 0x00, 0x00, 0xFF, # Alpha channel bitmask
        0x20, 0x6E, 0x69, 0x57  # LCS_WINDOWS_COLOR_SPACE
    ])

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Create a pattern for the image
    pixels = []
    for y in range(height):
        for x in range(width):
            # Checkerboard pattern
            if (x // 10) % 2 == (y // 10) % 2:
                pixels.append(0xFFFFFFFF)  # White pixel
            else:
                pixels.append(0x00000000)  # Black pixel

    # Convert pixel array to bytearray
    pixel_data = bytearray()
    for pixel in pixels:
        pixel_data += pixel.to_bytes(4, byteorder='little')

    # Write bitmap file
    with open(filename, 'wb') as bmp_file:
        bmp_file.write(file_header + dib_header + pixel_data)

# Generate a 100x100 checkerboard pattern BMP
create_bmp('./tmp/checkerboard.bmp', 100, 100)