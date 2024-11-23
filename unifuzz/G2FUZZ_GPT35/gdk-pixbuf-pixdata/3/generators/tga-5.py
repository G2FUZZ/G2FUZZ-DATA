import struct

def create_tga_file(metadata):
    # TGA file header
    tga_header = bytearray([
        0,  # ID Length
        0,  # Color Map Type
        2,  # Image Type - Uncompressed True-Color Image
        0, 0, 0, 0, 0,  # Color Map Specification
        0, 0, 0, 0,  # Image Specification
        24,  # Pixel Depth - 24 bits per pixel
        32,  # Image Descriptor - Top-left origin
    ])

    # Metadata
    metadata_bytes = metadata.encode('utf-8')
    tga_header[0] = len(metadata_bytes)  # Update ID Length
    tga_data = tga_header + metadata_bytes

    # Save to file
    file_name = f'./tmp/metadata_example.tga'
    with open(file_name, 'wb') as f:
        f.write(tga_data)

# Create a TGA file with metadata
metadata = "Author: John Doe, Created: 2022-09-15"
create_tga_file(metadata)