import os
import struct
import random

def write_bmp(filename, width, height, pixels):
    with open(filename, 'wb') as f:
        # BMP Header
        f.write(b'BM')  # File type
        size = 14 + 40 + (width * height * 3)  # File size
        f.write(struct.pack('<I', size))  # Size of the file in bytes
        f.write(b'\x00\x00')  # Reserved 1 (not used)
        f.write(b'\x00\x00')  # Reserved 2 (not used)
        f.write(b'\x36\x00\x00\x00')  # Offset where the pixel array can be found

        # DIB Header
        f.write(b'\x28\x00\x00\x00')  # Number of bytes in the DIB header (40 bytes)
        f.write(struct.pack('<I', width))  # Width of the bitmap in pixels
        f.write(struct.pack('<I', height))  # Height of the bitmap in pixels
        f.write(b'\x01\x00')  # Number of color planes being used
        f.write(b'\x18\x00')  # Number of bits per pixel
        f.write(b'\x00\x00\x00\x00')  # BI_RGB, no pixel array compression used
        f.write(b'\x00\x00\x00\x00')  # Size of the raw data in the pixel array (including padding)
        f.write(b'\x13\x0B\x00\x00')  # Print resolution of the image, 72 DPI x 39.3701 inches per meter yields 2835 pixels/meter horizontally
        f.write(b'\x13\x0B\x00\x00')  # Print resolution of the image vertically
        f.write(b'\x00\x00\x00\x00')  # Number of colors in the palette
        f.write(b'\x00\x00\x00\x00')  # 0 means all colors are important

        # Bitmap Data
        for y in range(height):
            for x in range(width):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                f.write(struct.pack('BBB', b, g, r))
            # Padding for 4-byte alignment
            padding = (4 - (width * 3) % 4) % 4
            f.write(b'\x00' * padding)
            
# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the BMP file
width, height = 100, 100
pixels = []  # In a real application, you'd populate this with pixel data
write_bmp('./tmp/generated_image.bmp', width, height, pixels)