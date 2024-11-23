import os

def create_bmp_file_with_compression(compression_type):
    # BMP file header
    bmp_header = b'BM'  # Signature
    file_size = 300  # Placeholder value, actual size will be calculated later
    reserved1 = 0
    reserved2 = 0
    pixel_data_offset = 54  # Offset to start of pixel data

    # DIB header
    dib_header_size = 40  # DIB header size for Windows V3
    image_width = 10
    image_height = 10
    planes = 1
    bits_per_pixel = 24  # 24-bit RGB
    compression = 0 if compression_type == 'uncompressed' else 1  # 0 for uncompressed, 1 for RLE compression
    image_size = 0  # Placeholder value for image size
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    colors_in_palette = 0
    important_colors = 0

    # Pixel data (RGB values for a 10x10 image)
    pixels = b'\xFF\x00\x00' * 100  # Red pixels

    # Calculate image size and file size
    image_size = len(pixels)
    file_size = pixel_data_offset + image_size

    # Create the BMP file
    with open(f'./tmp/image_{compression_type}.bmp', 'wb') as bmp_file:
        # Write BMP file header
        bmp_file.write(bmp_header)
        bmp_file.write(file_size.to_bytes(4, byteorder='little'))
        bmp_file.write(reserved1.to_bytes(2, byteorder='little'))
        bmp_file.write(reserved2.to_bytes(2, byteorder='little'))
        bmp_file.write(pixel_data_offset.to_bytes(4, byteorder='little'))

        # Write DIB header
        bmp_file.write(dib_header_size.to_bytes(4, byteorder='little'))
        bmp_file.write(image_width.to_bytes(4, byteorder='little'))
        bmp_file.write(image_height.to_bytes(4, byteorder='little'))
        bmp_file.write(planes.to_bytes(2, byteorder='little'))
        bmp_file.write(bits_per_pixel.to_bytes(2, byteorder='little'))
        bmp_file.write(compression.to_bytes(4, byteorder='little'))
        bmp_file.write(image_size.to_bytes(4, byteorder='little'))
        bmp_file.write(x_pixels_per_meter.to_bytes(4, byteorder='little'))
        bmp_file.write(y_pixels_per_meter.to_bytes(4, byteorder='little'))
        bmp_file.write(colors_in_palette.to_bytes(4, byteorder='little'))
        bmp_file.write(important_colors.to_bytes(4, byteorder='little'))

        # Write pixel data
        bmp_file.write(pixels)

# Create BMP files with uncompressed and RLE compressed formats
create_bmp_file_with_compression('uncompressed')
create_bmp_file_with_compression('compressed')