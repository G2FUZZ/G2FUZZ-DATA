import struct

def create_bmp_with_compression(filename, width, height, compression):
    # BMP header
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 54 + width * height)  # File size
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 54)  # Data offset

    # DIB header
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', width)  # Image width
    dib_header += struct.pack('<I', height)  # Image height
    dib_header += b'\x01\x00'  # Color planes
    dib_header += b'\x18\x00'  # Bits per pixel
    dib_header += struct.pack('<I', compression)  # Compression method
    dib_header += struct.pack('<I', 0)  # Image size (can be 0 for uncompressed)
    dib_header += struct.pack('<I', 2835)  # Horizontal resolution in pixels per meter
    dib_header += struct.pack('<I', 2835)  # Vertical resolution in pixels per meter
    dib_header += struct.pack('<I', 0)  # Number of colors in the palette
    dib_header += struct.pack('<I', 0)  # Number of important colors

    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(bmp_header + dib_header)

# Create uncompressed BMP
create_bmp_with_compression('uncompressed.bmp', 800, 600, 0)

# Create RLE compressed BMP
create_bmp_with_compression('rle_compressed.bmp', 800, 600, 1)