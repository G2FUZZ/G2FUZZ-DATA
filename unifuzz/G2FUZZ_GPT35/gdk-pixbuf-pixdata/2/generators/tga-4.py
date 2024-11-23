import struct

def create_tga_file(metadata):
    header = bytearray(18)
    header[2] = 2  # image type (uncompressed true-color image)
    header[12:16] = struct.pack('<HH', 1, 1)  # image dimensions (1x1)
    header[17] = 24  # bits per pixel

    with open(f'./tmp/{metadata}.tga', 'wb') as f:
        f.write(header)
        # Write metadata as a comment in the TGA file
        metadata_str = f'# Metadata: {metadata}'.encode('ascii')
        f.write(metadata_str)

# Create a TGA file with metadata
metadata = 'Author: John Doe, Date: 2022-01-01, Comments: This is a sample TGA file.'
create_tga_file(metadata)