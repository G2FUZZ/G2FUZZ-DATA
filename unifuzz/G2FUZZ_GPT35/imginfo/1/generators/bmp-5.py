import struct

def generate_bmp_with_metadata(file_path, metadata):
    # BMP file header
    file_header = b'BM'
    file_size = 154  # Total size of the file
    reserved1 = 0
    reserved2 = 0
    pixel_data_offset = 122  # Offset to the start of pixel data

    # DIB header (BITMAPINFOHEADER)
    dib_header_size = 108
    image_width = 100
    image_height = 100
    color_planes = 1
    bits_per_pixel = 24
    compression_method = 0
    image_size = 0
    horizontal_resolution = 2835  # 72 DPI
    vertical_resolution = 2835  # 72 DPI
    colors_in_palette = 0
    important_colors = 0

    # Metadata
    metadata_length = len(metadata)
    metadata_header = b'META'
    
    with open(file_path, 'wb') as f:
        # Write BMP file header
        f.write(file_header)
        f.write(struct.pack('<I', file_size))
        f.write(struct.pack('<H', reserved1))
        f.write(struct.pack('<H', reserved2))
        f.write(struct.pack('<I', pixel_data_offset))

        # Write DIB header
        f.write(struct.pack('<I', dib_header_size))
        f.write(struct.pack('<i', image_width))
        f.write(struct.pack('<i', image_height))
        f.write(struct.pack('<H', color_planes))
        f.write(struct.pack('<H', bits_per_pixel))
        f.write(struct.pack('<I', compression_method))
        f.write(struct.pack('<I', image_size))
        f.write(struct.pack('<i', horizontal_resolution))
        f.write(struct.pack('<i', vertical_resolution))
        f.write(struct.pack('<I', colors_in_palette))
        f.write(struct.pack('<I', important_colors))

        # Write metadata
        f.write(metadata_header)
        f.write(struct.pack('<I', metadata_length))
        f.write(metadata)

# Generate a BMP file with metadata
metadata = b'This is metadata for the BMP file.'
file_path = './tmp/metadata.bmp'
generate_bmp_with_metadata(file_path, metadata)