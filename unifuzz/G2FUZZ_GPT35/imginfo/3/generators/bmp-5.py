import struct

def create_bmp_with_metadata(width, height, metadata):
    # BMP header
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 54 + len(metadata))  # File size
    bmp_header += b'\x00\x00\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 54 + len(metadata))  # Data offset

    # DIB header
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', width)  # Image width
    dib_header += struct.pack('<I', height)  # Image height
    dib_header += b'\x01\x00'  # Color planes
    dib_header += b'\x18\x00'  # Bits per pixel
    dib_header += b'\x00\x00\x00\x00'  # Compression method
    dib_header += struct.pack('<I', len(metadata))  # Size of raw image data
    dib_header += b'\x13\x0B\x00\x00'  # Horizontal resolution
    dib_header += b'\x13\x0B\x00\x00'  # Vertical resolution
    dib_header += b'\x00\x00\x00\x00'  # Number of colors in the palette
    dib_header += b'\x00\x00\x00\x00'  # Number of important colors

    # Create BMP file
    with open(f'./tmp/image_with_metadata.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(metadata.encode())

# Define image dimensions and metadata
image_width = 100
image_height = 100
metadata = "Resolution: 300dpi\nColor Profile: sRGB\nAuthor: John Doe"

# Create BMP file with metadata
create_bmp_with_metadata(image_width, image_height, metadata)