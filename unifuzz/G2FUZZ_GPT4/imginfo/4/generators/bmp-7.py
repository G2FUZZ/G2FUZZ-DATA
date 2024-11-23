import os

def create_bmp_file(filename, width, height):
    # BMP Header
    file_size = 54 + 3 * width * height  # Header size (54 bytes) + pixel data
    offset = 54  # Data offset
    header = [
        b'BM',  # File type (always "BM")
        file_size.to_bytes(4, byteorder='little'),  # File size in bytes
        (0).to_bytes(4, byteorder='little'),  # Reserved
        offset.to_bytes(4, byteorder='little'),  # Start of pixel array
        (40).to_bytes(4, byteorder='little'),  # Header size
        width.to_bytes(4, byteorder='little'),  # Image width
        height.to_bytes(4, byteorder='little'),  # Image height
        (1).to_bytes(2, byteorder='little'),  # Planes
        (24).to_bytes(2, byteorder='little'),  # Bits per pixel
        (0).to_bytes(4, byteorder='little'),  # Compression (no compression)
        (0).to_bytes(4, byteorder='little'),  # Image size (can be 0 for uncompressed images)
        (11811).to_bytes(4, byteorder='little'),  # X pixels per meter (arbitrary value)
        (11811).to_bytes(4, byteorder='little'),  # Y pixels per meter (arbitrary value)
        (0).to_bytes(4, byteorder='little'),  # Colors in color table (0 = use default)
        (0).to_bytes(4, byteorder='little'),  # Important colors (0 = all)
    ]

    # Generate pixel data
    pixels = []
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                pixels.append((0, 0, 0))  # Black pixel
            else:
                pixels.append((255, 255, 255))  # White pixel
        # Padding for 4-byte alignment
        while len(pixels) % width != 0:
            pixels.append((0, 0, 0))  # Black padding

    # Write to file
    with open(filename, 'wb') as f:
        for item in header:
            f.write(item)
        for pixel in pixels:
            f.write(bytes(pixel))

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create BMP file
create_bmp_file('./tmp/checkerboard.bmp', 100, 100)