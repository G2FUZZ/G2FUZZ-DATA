import struct

def create_bmp_with_palette(width, height, palette_colors):
    # BMP file header
    file_header = b'BM'  # Signature
    file_header += struct.pack('<I', 14 + 40 + 4 * len(palette_colors) + width * height)  # File size
    file_header += b'\x00\x00\x00\x00'  # Reserved
    file_header += struct.pack('<I', 14 + 40 + 4 * len(palette_colors))  # Data offset

    # BMP info header
    info_header = struct.pack('<I', 40)  # Header size
    info_header += struct.pack('<I', width)  # Image width
    info_header += struct.pack('<I', height)  # Image height
    info_header += b'\x01\x00'  # Planes
    info_header += b'\x08\x00'  # Bits per pixel
    info_header += b'\x00\x00\x00\x00'  # Compression
    info_header += struct.pack('<I', width * height)  # Image size
    info_header += b'\x00\x00\x00\x00'  # X pixels per meter
    info_header += b'\x00\x00\x00\x00'  # Y pixels per meter
    info_header += struct.pack('<I', len(palette_colors))  # Colors used
    info_header += struct.pack('<I', len(palette_colors))  # Important colors

    # Palette
    palette = b''
    for color in palette_colors:
        palette += bytes(color)

    # Image data
    image_data = b''
    for i in range(height):
        for j in range(width):
            image_data += bytes([i % len(palette_colors)])  # Using the palette colors in the image

    # Write to file
    with open(f'./tmp/palette_image.bmp', 'wb') as f:
        f.write(file_header + info_header + palette + image_data)

# Define the palette colors (RGB format)
palette_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Create a BMP file with palette
create_bmp_with_palette(200, 200, palette_colors)