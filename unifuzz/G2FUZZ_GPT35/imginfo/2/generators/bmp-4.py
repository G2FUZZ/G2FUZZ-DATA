import struct

def create_bmp_file_with_compression(width, height, compression, file_path):
    # BMP file header
    file_header = b'BM'
    file_size = 54 + width * height * 3  # Header size (54 bytes) + image data size
    reserved_bytes = b'\x00\x00\x00\x00'
    data_offset = 54

    # DIB header
    dib_header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 24
    compression_method = compression
    image_size = width * height * 3
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    colors_in_palette = 0
    important_colors = 0

    # Create BMP data
    bmp_data = struct.pack('<2sIHHI', file_header, file_size, 0, 0, data_offset)  # File header
    bmp_data += struct.pack('<IIIHHIIIIII', dib_header_size, image_width, image_height, planes, bits_per_pixel,
                            compression_method, image_size, x_pixels_per_meter, y_pixels_per_meter,
                            colors_in_palette, important_colors)  # DIB header

    with open(file_path, 'wb') as file:
        file.write(bmp_data)

    print(f'BMP file with compression method {compression} created at {file_path}')

# Create uncompressed BMP file
create_bmp_file_with_compression(100, 100, 0, './tmp/uncompressed.bmp')

# Create RLE compressed BMP file
create_bmp_file_with_compression(100, 100, 1, './tmp/rle_compressed.bmp')