import struct

def generate_bmp_with_metadata(width, height, metadata):
    # BMP header
    file_size = width * height * 3 + 54
    bmp_header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)

    # Metadata payload
    metadata_payload = metadata.encode('utf-8')

    with open(f'./tmp/metadata_{width}x{height}.bmp', 'wb') as f:
        f.write(bmp_header)
        f.write(metadata_payload)

# Generate a BMP file with metadata
width = 640
height = 480
metadata = "Image created with custom metadata"

generate_bmp_with_metadata(width, height, metadata)