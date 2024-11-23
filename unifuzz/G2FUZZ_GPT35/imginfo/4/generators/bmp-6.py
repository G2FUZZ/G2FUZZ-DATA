import struct

# Function to generate BMP file with metadata
def generate_bmp_with_metadata():
    # BMP header
    bmp_header = b'BM'  # Signature
    file_size = 300  # File size (replace with actual size)
    bmp_header += struct.pack('<I', file_size)  # File size
    bmp_header += b'\x00\x00\x00\x00'  # Reserved
    bmp_header += b'\x36\x00\x00\x00'  # Offset to image data

    # Image data
    image_data = b'\xFF\x00\x00' * 100  # Sample image data

    # Metadata (example metadata)
    metadata = b'Metadata: Resolution=300dpi, Color Profile=sRGB'

    # Write data to BMP file
    with open('./tmp/metadata.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(metadata)
        f.write(image_data)

# Generate BMP file with metadata
generate_bmp_with_metadata()