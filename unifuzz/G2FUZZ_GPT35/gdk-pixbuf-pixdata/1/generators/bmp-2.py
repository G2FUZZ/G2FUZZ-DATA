import struct

def write_bmp_with_compression(width, height, compression_type, file_path):
    # BMP file header
    bmp_header = b'BM'
    bmp_size = 54 + 3 * width * height  # Size of the BMP file
    bmp_reserved = 0
    bmp_offset = 54  # Offset to start of image data

    # DIB header
    dib_size = 40  # Size of the DIB header
    dib_width = width
    dib_height = height
    dib_planes = 1
    dib_bpp = 24  # 24 bits per pixel
    dib_compression = compression_type
    dib_image_size = 3 * width * height
    dib_x_ppm = 0
    dib_y_ppm = 0
    dib_colors = 0
    dib_important_colors = 0

    with open(file_path, 'wb') as file:
        # Write BMP file header
        file.write(bmp_header)
        file.write(struct.pack('<i', bmp_size))
        file.write(struct.pack('<H', bmp_reserved))
        file.write(struct.pack('<H', bmp_reserved))
        file.write(struct.pack('<i', bmp_offset))

        # Write DIB header
        file.write(struct.pack('<i', dib_size))
        file.write(struct.pack('<i', dib_width))
        file.write(struct.pack('<i', dib_height))
        file.write(struct.pack('<H', dib_planes))
        file.write(struct.pack('<H', dib_bpp))
        file.write(struct.pack('<i', dib_compression))
        file.write(struct.pack('<i', dib_image_size))
        file.write(struct.pack('<i', dib_x_ppm))
        file.write(struct.pack('<i', dib_y_ppm))
        file.write(struct.pack('<i', dib_colors))
        file.write(struct.pack('<i', dib_important_colors))

        # Write image data
        for y in range(height):
            for x in range(width):
                file.write(bytes([0, 0, 255]))  # RGB color (blue)

# Generate and save BMP file with RLE compression
write_bmp_with_compression(100, 100, 1, './tmp/compressed_bmp_rle.bmp')

# Generate and save BMP file without compression
write_bmp_with_compression(100, 100, 0, './tmp/uncompressed_bmp.bmp')