import os

def create_bmp_file(filename, width, height, color):
    # BMP Header
    file_type = b'BM'  # BM indicates a BMP file
    reserved_1 = reserved_2 = 0
    offset = 54  # where the pixel data starts
    file_size = offset + width * height * 3  # header size + pixel data
    planes = 1  # number of color planes
    bits_per_pixel = 24  # color depth
    compression = 0  # no compression
    image_size = width * height * 3  # pixel data size
    ppm_x = ppm_y = 2835  # pixels per meter
    total_colors = used_colors = 0  # color count

    # BMP Image Header
    header_size = 40  # header size
    image_width = width
    image_height = height

    # Create the BMP file header
    file_header = bytearray(file_type + file_size.to_bytes(4, byteorder='little') + 
                            reserved_1.to_bytes(2, byteorder='little') + 
                            reserved_2.to_bytes(2, byteorder='little') + 
                            offset.to_bytes(4, byteorder='little'))

    # Create the BMP image header
    image_header = bytearray(header_size.to_bytes(4, byteorder='little') + 
                             image_width.to_bytes(4, byteorder='little') + 
                             image_height.to_bytes(4, byteorder='little') + 
                             planes.to_bytes(2, byteorder='little') + 
                             bits_per_pixel.to_bytes(2, byteorder='little') + 
                             compression.to_bytes(4, byteorder='little') + 
                             image_size.to_bytes(4, byteorder='little') + 
                             ppm_x.to_bytes(4, byteorder='little') + 
                             ppm_y.to_bytes(4, byteorder='little') + 
                             total_colors.to_bytes(4, byteorder='little') + 
                             used_colors.to_bytes(4, byteorder='little'))

    # Pixel data
    pixel_data = bytearray([color[2], color[1], color[0]] * width * height)

    # Combine headers and pixel data
    bmp_data = file_header + image_header + pixel_data

    # Write to file
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    with open(f'./tmp/{filename}', 'wb') as f:
        f.write(bmp_data)

# Example usage
create_bmp_file('example.bmp', 100, 100, (192, 192, 192))  # Light gray color