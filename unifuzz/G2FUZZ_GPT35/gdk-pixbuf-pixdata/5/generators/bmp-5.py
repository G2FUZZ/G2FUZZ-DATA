import struct

def generate_bmp_file(metadata):
    file_header = b'BM'  # BMP file signature
    file_size = 70  # File size in bytes (header + DIB header + metadata)
    reserved1 = 0
    reserved2 = 0
    pixel_data_offset = 70  # Offset to pixel data

    dib_header_size = 56  # DIB header size
    image_width = 100  # Image width in pixels
    image_height = 100  # Image height in pixels
    num_planes = 1
    bits_per_pixel = 24  # 24-bit color depth
    compression_method = 0  # No compression
    image_size = 0  # Image size in bytes (can be 0 for uncompressed images)
    x_resolution = 2835  # 72 DPI
    y_resolution = 2835  # 72 DPI
    num_colors = 0  # Number of colors in the color palette
    important_colors = 0  # All colors are important

    with open('./tmp/metadata.bmp', 'wb') as f:
        f.write(file_header)
        f.write(struct.pack('<I', file_size))
        f.write(struct.pack('<H', reserved1))
        f.write(struct.pack('<H', reserved2))
        f.write(struct.pack('<I', pixel_data_offset))

        f.write(struct.pack('<I', dib_header_size))
        f.write(struct.pack('<i', image_width))
        f.write(struct.pack('<i', image_height))
        f.write(struct.pack('<H', num_planes))
        f.write(struct.pack('<H', bits_per_pixel))
        f.write(struct.pack('<I', compression_method))
        f.write(struct.pack('<I', image_size))
        f.write(struct.pack('<i', x_resolution))
        f.write(struct.pack('<i', y_resolution))
        f.write(struct.pack('<I', num_colors))
        f.write(struct.pack('<I', important_colors))

        # Write metadata
        f.write(metadata.encode())

# Generate and save BMP file with metadata
metadata = "Image Resolution: 100x100\nColor Profile: RGB\nCreation Date: 2022-01-01"
generate_bmp_file(metadata)