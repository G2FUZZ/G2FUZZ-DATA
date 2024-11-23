import os

def create_bmp(filename, width, height, color):
    """Create a simple BMP file with a single color."""
    # BMP Header
    file_size = 54 + width * height * 3
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

    bmp_header = [
        b'BM',  # Signature
        file_size.to_bytes(4, byteorder='little'),  # File size
        (0).to_bytes(4, byteorder='little'),  # Reserved
        offset.to_bytes(4, byteorder='little'),  # Data offset
        header_size.to_bytes(4, byteorder='little'),  # Header size
        width.to_bytes(4, byteorder='little'),  # Width
        height.to_bytes(4, byteorder='little'),  # Height
        planes.to_bytes(2, byteorder='little'),  # Planes
        bits_per_pixel.to_bytes(2, byteorder='little'),  # Bits per pixel
        compression.to_bytes(4, byteorder='little'),  # Compression
        image_size.to_bytes(4, byteorder='little'),  # Image size
        x_pixels_per_meter.to_bytes(4, byteorder='little'),  # X pixels per meter
        y_pixels_per_meter.to_bytes(4, byteorder='little'),  # Y pixels per meter
        total_colors.to_bytes(4, byteorder='little'),  # Total colors
        important_colors.to_bytes(4, byteorder='little')  # Important colors
    ]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        for part in bmp_header:
            f.write(part)

        # Pixel data
        for y in range(height):
            for x in range(width):
                f.write(color)
            # BMP rows must be a multiple of 4 bytes in size
            padding = (4 - (width * 3) % 4) % 4
            f.write(b'\x00' * padding)

# Generate a BMP file
create_bmp('./tmp/device_independence.bmp', 100, 100, b'\x00\xFF\x00')  # Green background