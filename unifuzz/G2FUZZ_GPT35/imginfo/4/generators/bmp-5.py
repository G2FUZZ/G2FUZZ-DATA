import struct

def generate_bmp_with_palette():
    # BMP File Header
    bf_type = b'BM'
    bf_size = 154
    bf_reserved1 = 0
    bf_reserved2 = 0
    bf_offset = 54

    # BMP Info Header
    bi_size = 40
    bi_width = 2
    bi_height = 2
    bi_planes = 1
    bi_bit_count = 8  # 8 bits per pixel for indexed color image
    bi_compression = 0
    bi_size_image = 0
    bi_x_pels_per_meter = 0
    bi_y_pels_per_meter = 0
    bi_clr_used = 256  # Number of colors in the palette
    bi_clr_important = 0

    # Color Palette (256 colors)
    palette = []
    for i in range(256):
        palette.extend([i, i, i, 0])  # grayscale palette

    # Pixel Data
    pixels = [
        0, 1,
        2, 3
    ]

    # Write BMP file
    with open('./tmp/generated_palette.bmp', 'wb') as f:
        # Write BMP File Header
        f.write(struct.pack('<2sIHHI', bf_type, bf_size, bf_reserved1, bf_reserved2, bf_offset))

        # Write BMP Info Header
        f.write(struct.pack('<IIIHHIIIIII', bi_size, bi_width, bi_height, bi_planes, bi_bit_count,
                            bi_compression, bi_size_image, bi_x_pels_per_meter, bi_y_pels_per_meter,
                            bi_clr_used, bi_clr_important))

        # Write Color Palette
        for color in palette:
            f.write(struct.pack('<B', color))

        # Write Pixel Data
        for pixel in pixels:
            f.write(struct.pack('<B', pixel))

    print("BMP file with color palette generated successfully.")


generate_bmp_with_palette()