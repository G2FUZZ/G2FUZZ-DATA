def create_tga():
    width, height = 100, 100  # Image dimensions
    pixels = [255, 0, 0] * width * height  # A red image

    header = bytes([
        0,  # ID length
        0,  # No color map
        2,  # Uncompressed, true-color image
        0, 0, 0, 0,  # Color map specification
        0,  # First entry index (2 bytes)
        0, 0, 0, 0,  # Color map length and entry size (5 bytes)
        0, 0,  # X-origin (2 bytes)
        0, 0,  # Y-origin (2 bytes)
        width & 0xFF, (width >> 8) & 0xFF,  # Image width
        height & 0xFF, (height >> 8) & 0xFF,  # Image height
        24,  # Pixel depth
        0  # Image descriptor
    ])

    with open('./tmp/example.tga', 'wb') as f:
        f.write(header)
        for pixel in pixels:
            f.write(pixel.to_bytes(1, 'little'))

if __name__ == '__main__':
    create_tga()