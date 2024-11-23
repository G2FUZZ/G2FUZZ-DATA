import struct
import os

def create_bmp_with_palette(width, height, palette_colors):
    # BMP file header (14 bytes)
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 14 + 40 + len(palette_colors) * 4 + width * height)  # File size
    bmp_header += b'\x00\x00\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 14 + 40 + len(palette_colors) * 4)  # Data offset

    # DIB header (40 bytes)
    dib_header = struct.pack('<I', 40)  # Header size
    dib_header += struct.pack('<I', width)  # Image width
    dib_header += struct.pack('<I', height)  # Image height
    dib_header += b'\x01\x00'  # Planes
    dib_header += b'\x08\x00'  # Bits per pixel (8-bit indexed color)
    dib_header += b'\x00\x00\x00\x00'  # Compression
    dib_header += struct.pack('<I', width * height)  # Image size
    dib_header += b'\x00\x00\x00\x00'  # X pixels per meter
    dib_header += b'\x00\x00\x00\x00'  # Y pixels per meter
    dib_header += struct.pack('<I', len(palette_colors))  # Colors in palette
    dib_header += b'\x00\x00\x00\x00'  # Important colors

    # Palette (4 bytes per color)
    palette = b''
    for color in palette_colors:
        palette += struct.pack('<BBBB', color[0], color[1], color[2], 0)

    # Image data (grayscale gradient)
    image_data = bytes([(i // width) % 256 for i in range(width * height)])

    # Create BMP file
    with open('./tmp/test_palette.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(palette)
        f.write(image_data)

# Define palette colors (R, G, B)
palette_colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255)   # Blue
]

# Generate BMP file with palette
create_bmp_with_palette(100, 100, palette_colors)