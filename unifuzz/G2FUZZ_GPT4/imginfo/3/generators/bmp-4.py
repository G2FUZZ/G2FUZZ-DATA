import os
import struct
import random

def create_bmp_file(filename, width, height):
    # BMP File Header (14 bytes)
    bfType = 19778  # BM
    bfSize = 14 + 40 + (width * height * 3)  # File header + Info header + Pixel data
    bfReserved1 = 0
    bfReserved2 = 0
    bfOffBits = 14 + 40  # File header + Info header

    # BMP Image Header (40 bytes)
    biSize = 40
    biWidth = width
    biHeight = height
    biPlanes = 1
    biBitCount = 24
    biCompression = 0
    biSizeImage = width * height * 3
    biXPelsPerMeter = 0
    biYPelsPerMeter = 0
    biClrUsed = 0
    biClrImportant = 0

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        # Writing the BMP file header
        f.write(struct.pack('<HL2HL', bfType, bfSize, bfReserved1, bfReserved2, bfOffBits))

        # Writing the BMP image header
        f.write(struct.pack('<3I2H6I', biSize, biWidth, biHeight, biPlanes, biBitCount, 
                            biCompression, biSizeImage, biXPelsPerMeter, biYPelsPerMeter, biClrUsed, biClrImportant))

        # Writing the pixel data
        for y in range(height):
            for x in range(width):
                # Generating a random color for each pixel
                b = random.randint(0, 255)
                g = random.randint(0, 255)
                r = random.randint(0, 255)
                f.write(struct.pack('BBB', b, g, r))

        # BMP files are padded to be a multiple of 4 bytes wide. No padding needed for 24 bits per pixel and width of 100.

# Generate a BMP file
bmp_filename = './tmp/random_colors.bmp'
create_bmp_file(bmp_filename, 100, 100)
print(f'BMP file created at {bmp_filename}')