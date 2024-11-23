import os

def create_bmp_file(filename, width, height, color):
    """ Creates a simple BMP file with a given color.
    
    Args:
        filename: The name of the file to create.
        width: The width of the image.
        height: The height of the image.
        color: A tuple of (R, G, B) values.
    """
    # BMP Header
    file_size = 54 + 3 * width * height
    reserved = 0
    offset = 54
    header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = width * height * 3
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 0
    important_colors = 0

    header = bytearray([
        0x42, 0x4D,                   # BM
        file_size & 0xFF, (file_size >> 8) & 0xFF, (file_size >> 16) & 0xFF, (file_size >> 24) & 0xFF,
        reserved & 0xFF, (reserved >> 8) & 0xFF, (reserved >> 16) & 0xFF, (reserved >> 24) & 0xFF,
        offset & 0xFF, (offset >> 8) & 0xFF, (offset >> 16) & 0xFF, (offset >> 24) & 0xFF,
        header_size & 0xFF, (header_size >> 8) & 0xFF, (header_size >> 16) & 0xFF, (header_size >> 24) & 0xFF,
        width & 0xFF, (width >> 8) & 0xFF, (width >> 16) & 0xFF, (width >> 24) & 0xFF,
        height & 0xFF, (height >> 8) & 0xFF, (height >> 16) & 0xFF, (height >> 24) & 0xFF,
        planes & 0xFF, (planes >> 8) & 0xFF,
        bits_per_pixel & 0xFF, (bits_per_pixel >> 8) & 0xFF,
        compression & 0xFF, (compression >> 8) & 0xFF, (compression >> 16) & 0xFF, (compression >> 24) & 0xFF,
        image_size & 0xFF, (image_size >> 8) & 0xFF, (image_size >> 16) & 0xFF, (image_size >> 24) & 0xFF,
        x_pixels_per_meter & 0xFF, (x_pixels_per_meter >> 8) & 0xFF, (x_pixels_per_meter >> 16) & 0xFF, (x_pixels_per_meter >> 24) & 0xFF,
        y_pixels_per_meter & 0xFF, (y_pixels_per_meter >> 8) & 0xFF, (y_pixels_per_meter >> 16) & 0xFF, (y_pixels_per_meter >> 24) & 0xFF,
        total_colors & 0xFF, (total_colors >> 8) & 0xFF, (total_colors >> 16) & 0xFF, (total_colors >> 24) & 0xFF,
        important_colors & 0xFF, (important_colors >> 8) & 0xFF, (important_colors >> 16) & 0xFF, (important_colors >> 24) & 0xFF
    ])

    # Ensuring the tmp directory exists
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    with open(f'./tmp/{filename}', 'wb') as f:
        f.write(header)
        for y in range(height):
            for x in range(width):
                f.write(bytearray(color))
            # Padding for 4-byte alignment
            for _ in range((4 - (width * 3) % 4) % 4):
                f.write(bytearray([0]))

create_bmp_file('test.bmp', 100, 100, (255, 0, 0))  # Red BMP image