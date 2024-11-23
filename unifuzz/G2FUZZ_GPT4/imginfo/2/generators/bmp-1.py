import os

def create_bmp(filename, width, height, color):
    # BMP Header
    file_size = 54 + 3 * width * height  # 54 byte header + 3 bytes per pixel
    reserved = 0
    offset = 54  # where the pixel array can be found
    header_size = 40  # size of the header
    planes = 1  # number of color planes
    bits_per_pixel = 24  # RGB
    compression = 0  # no compression
    image_size = width * height * 3
    x_pixels_per_meter = 2835  # horizontal resolution
    y_pixels_per_meter = 2835  # vertical resolution
    total_colors = 0  # color palette not used
    important_colors = 0  # all colors are important

    # BMP Header
    bmp_header = bytearray([
        0x42, 0x4D,  # Signature 'BM'
        file_size & 0xFF, (file_size >> 8) & 0xFF, (file_size >> 16) & 0xFF, (file_size >> 24) & 0xFF,  # File size
        reserved & 0xFF, (reserved >> 8) & 0xFF, (reserved >> 16) & 0xFF, (reserved >> 24) & 0xFF,  # Reserved
        offset & 0xFF, (offset >> 8) & 0xFF, (offset >> 16) & 0xFF, (offset >> 24) & 0xFF,  # Offset
        header_size & 0xFF, (header_size >> 8) & 0xFF, (header_size >> 16) & 0xFF, (header_size >> 24) & 0xFF,  # Header size
        width & 0xFF, (width >> 8) & 0xFF, (width >> 16) & 0xFF, (width >> 24) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF, (height >> 16) & 0xFF, (height >> 24) & 0xFF,  # Height
        planes & 0xFF, (planes >> 8) & 0xFF,  # Planes
        bits_per_pixel & 0xFF, (bits_per_pixel >> 8) & 0xFF,  # Bits per pixel
        compression & 0xFF, (compression >> 8) & 0xFF, (compression >> 16) & 0xFF, (compression >> 24) & 0xFF,  # Compression
        image_size & 0xFF, (image_size >> 8) & 0xFF, (image_size >> 16) & 0xFF, (image_size >> 24) & 0xFF,  # Image size
        x_pixels_per_meter & 0xFF, (x_pixels_per_meter >> 8) & 0xFF, (x_pixels_per_meter >> 16) & 0xFF, (x_pixels_per_meter >> 24) & 0xFF,  # X pixels per meter
        y_pixels_per_meter & 0xFF, (y_pixels_per_meter >> 8) & 0xFF, (y_pixels_per_meter >> 16) & 0xFF, (y_pixels_per_meter >> 24) & 0xFF,  # Y pixels per meter
        total_colors & 0xFF, (total_colors >> 8) & 0xFF, (total_colors >> 16) & 0xFF, (total_colors >> 24) & 0xFF,  # Total colors
        important_colors & 0xFF, (important_colors >> 8) & 0xFF, (important_colors >> 16) & 0xFF, (important_colors >> 24) & 0xFF  # Important colors
    ])

    # Pixel Array (Bitmap Data)
    # Note: BMP files are stored from the bottom up
    bitmap = bytearray()
    for y in range(height):
        for x in range(width):
            bitmap += color
        # Padding for 4-byte alignment
        while len(bitmap) % 4 != 0:
            bitmap += b'\x00'

    # Combine header and bitmap
    bmp = bmp_header + bitmap

    # Write to file
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'wb') as f:
        f.write(bmp)

# Example usage:
create_bmp('./tmp/example.bmp', 100, 100, b'\x00\x00\xFF')  # Blue square