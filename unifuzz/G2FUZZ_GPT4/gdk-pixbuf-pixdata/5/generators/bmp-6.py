import os

def create_bmp_file(path):
    # BMP File Header and Info Header (for a 24-bit BMP)
    bmp_header = [
        b'BM',  # ID field
        (54 + 3*10*10).to_bytes(4, byteorder='little'),  # Size of the BMP file
        (0).to_bytes(2, byteorder='little'),  # Application-specific
        (0).to_bytes(2, byteorder='little'),  # Application-specific
        (54).to_bytes(4, byteorder='little'),  # The offset where the bitmap data (pixels) can be found
        (40).to_bytes(4, byteorder='little'),  # The size of this header (40 bytes)
        (10).to_bytes(4, byteorder='little'),  # The bitmap width in pixels
        (10).to_bytes(4, byteorder='little'),  # The bitmap height in pixels
        (1).to_bytes(2, byteorder='little'),  # The number of color planes
        (24).to_bytes(2, byteorder='little'),  # The number of bits per pixel
        (0).to_bytes(4, byteorder='little'),  # The compression method being used
        (3*10*10).to_bytes(4, byteorder='little'),  # The image size
        (2835).to_bytes(4, byteorder='little'),  # The horizontal resolution of the image (pixel per meter)
        (2835).to_bytes(4, byteorder='little'),  # The vertical resolution of the image (pixel per meter)
        (0).to_bytes(4, byteorder='little'),  # The number of colors in the color palette
        (0).to_bytes(4, byteorder='little')   # The number of important colors used
    ]

    # Ensure the ./tmp/ directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb') as f:
        for item in bmp_header:
            f.write(item)
        
        # Create a simple image: 10x10 pixels, each pixel is red
        for _ in range(10*10):
            f.write((0).to_bytes(1, byteorder='little'))  # Blue
            f.write((0).to_bytes(1, byteorder='little'))  # Green
            f.write((255).to_bytes(1, byteorder='little'))  # Red

if __name__ == '__main__':
    bmp_path = './tmp/simple_image.bmp'
    create_bmp_file(bmp_path)
    print(f'BMP file created at {bmp_path}')