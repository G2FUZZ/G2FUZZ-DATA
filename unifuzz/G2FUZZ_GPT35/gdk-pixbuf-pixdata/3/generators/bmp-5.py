import struct

def create_bmp_with_metadata(file_path, width, height, resolution):
    # BMP file header
    file_header = b'BM'
    file_size = 54  # Header size (14 bytes) + DIB header size (40 bytes)
    reserved = 0
    offset = 54  # Offset to start of image data
    headers = struct.pack('<2sIHHI', file_header, file_size, reserved, reserved, offset)

    # DIB header
    dib_header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 24  # 3 bytes per pixel
    compression = 0
    image_size = 0  # Can be set to 0 for uncompressed images
    x_resolution = resolution
    y_resolution = resolution
    colors_in_palette = 0
    important_colors = 0
    dib_header = struct.pack('<IIIHHIIIIII', dib_header_size, image_width, image_height, planes, bits_per_pixel,
                             compression, image_size, x_resolution, y_resolution, colors_in_palette, important_colors)

    with open(file_path, 'wb') as bmp_file:
        # Write headers
        bmp_file.write(headers)
        bmp_file.write(dib_header)

        # Write metadata (dummy metadata for demonstration)
        metadata = 'Metadata: Image dimensions - {}x{}, Resolution - {}dpi'.format(width, height, resolution).encode('utf-8')
        bmp_file.write(metadata)

# Generate BMP file with metadata
create_bmp_with_metadata('./tmp/metadata_example.bmp', 800, 600, 300)