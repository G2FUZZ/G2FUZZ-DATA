import struct

def create_complex_bmp_file(width, height, compression, file_path, colors):
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
    colors_in_palette = len(colors)
    important_colors = 0

    # Create BMP data
    bmp_data = struct.pack('<2sIHHI', file_header, file_size, 0, 0, data_offset)  # File header
    bmp_data += struct.pack('<IIIHHIIIIII', dib_header_size, image_width, image_height, planes, bits_per_pixel,
                            compression_method, image_size, x_pixels_per_meter, y_pixels_per_meter,
                            colors_in_palette, important_colors)  # DIB header

    # Color palette data
    for color in colors:
        bmp_data += struct.pack('<BBBx', *color)  # Blue, Green, Red, 1 byte padding

    with open(file_path, 'wb') as file:
        file.write(bmp_data)

    print(f'Complex BMP file with compression method {compression} and {len(colors)} colors created at {file_path}')

# Create a complex BMP file with color palette
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255)   # Magenta
]

create_complex_bmp_file(200, 200, 0, './tmp/complex_bmp.bmp', colors)