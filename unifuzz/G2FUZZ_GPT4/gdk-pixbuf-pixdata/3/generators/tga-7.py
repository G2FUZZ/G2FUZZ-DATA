import os

def create_tga_file(width, height, color):
    header = bytes([
        0,  # ID length
        0,  # Color map type
        2,  # Image type (2 for uncompressed true color)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin (low-high)
        0, 0,  # Y-origin (low-high)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (low-high)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (low-high)
        32,  # Pixel depth (32 bits per pixel)
        0  # Image descriptor (bit 5: 0 = non-interleaved)
    ])

    pixels = [color for _ in range(width * height)]
    data = bytearray()
    for pixel in pixels:
        # Assuming color is in RGBA format
        data.extend([
            pixel[2],  # Blue
            pixel[1],  # Green
            pixel[0],  # Red
            pixel[3]   # Alpha
        ])

    file_path = './tmp/example.tga'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(data)

# Example usage
# Create a 100x100 image, each pixel is red with full opacity
create_tga_file(100, 100, (255, 0, 0, 255))