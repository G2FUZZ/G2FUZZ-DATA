import struct

def create_complex_bmp(filename, width, height, compression, palette_colors):
    # BMP header
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 54 + width * height + len(palette_colors) * 4)  # File size
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 54 + len(palette_colors) * 4)  # Data offset

    # DIB header
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', width)  # Image width
    dib_header += struct.pack('<I', height)  # Image height
    dib_header += b'\x01\x00'  # Color planes
    dib_header += b'\x08\x00'  # Bits per pixel (8-bit for color palette)
    dib_header += struct.pack('<I', compression)  # Compression method
    dib_header += struct.pack('<I', 0)  # Image size (can be 0 for uncompressed)
    dib_header += struct.pack('<I', 2835)  # Horizontal resolution in pixels per meter
    dib_header += struct.pack('<I', 2835)  # Vertical resolution in pixels per meter
    dib_header += struct.pack('<I', len(palette_colors))  # Number of colors in the palette
    dib_header += struct.pack('<I', 0)  # Number of important colors

    # Color palette
    palette_data = b''
    for color in palette_colors:
        palette_data += bytes(color)

    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(bmp_header + dib_header + palette_data)

# Create a BMP with a color palette
palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Example palette colors (RGB format)
create_complex_bmp('color_palette.bmp', 400, 300, 0, palette)