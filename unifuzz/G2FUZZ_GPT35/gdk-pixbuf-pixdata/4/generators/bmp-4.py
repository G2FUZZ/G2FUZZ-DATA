import struct

def create_bmp_with_metadata(width, height, resolution, color_space, author):
    # BMP header
    bmp_header = b'BM'
    bmp_header += struct.pack('<I', 54 + len(author))  # File size
    bmp_header += b'\x00\x00\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 54)  # Data offset

    # DIB header
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', width)
    dib_header += struct.pack('<I', height)
    dib_header += b'\x01\x00'  # Color planes
    dib_header += b'\x18\x00'  # Bits per pixel
    dib_header += b'\x00\x00\x00\x00'  # Compression method
    dib_header += struct.pack('<I', width * height * 3)  # Image size
    dib_header += resolution  # Image resolution
    dib_header += color_space  # Color space
    dib_header += b'\x00\x00\x00\x00'  # Color palette
    dib_header += struct.pack('<I', len(author))  # Metadata size

    # Image data (dummy data for demonstration)
    image_data = b'\xFF\x00\x00' * (width * height)

    # Combine headers and data
    bmp_data = bmp_header + dib_header + author.encode() + image_data

    with open('./tmp/metadata.bmp', 'wb') as f:
        f.write(bmp_data)

# Generate a BMP file with metadata
create_bmp_with_metadata(256, 256, b'\x00\x00\x00\x01\x00\x00\x00\x01', b'\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01', 'Author: John Doe')