import numpy as np
import os

# Function to create a BMP file
def create_bmp_file(file_path, width, height, color):
    bmp_header = bytearray(b'BM')
    bmp_header += (width * height * 3 + 54).to_bytes(4, byteorder='little')  # File size
    bmp_header += bytearray(b'\x00\x00\x00\x00')  # Reserved
    bmp_header += (54).to_bytes(4, byteorder='little')  # Data offset
    bmp_header += (40).to_bytes(4, byteorder='little')  # Info Header size
    bmp_header += width.to_bytes(4, byteorder='little')  # Image width
    bmp_header += height.to_bytes(4, byteorder='little')  # Image height
    bmp_header += (1).to_bytes(2, byteorder='little')  # Planes
    bmp_header += (24).to_bytes(2, byteorder='little')  # Bits per pixel
    bmp_header += (0).to_bytes(4, byteorder='little')  # Compression (0 = BI_RGB)
    bmp_header += (width * height * 3).to_bytes(4, byteorder='little')  # Image size
    bmp_header += (0).to_bytes(4, byteorder='little')  # X pixels per meter
    bmp_header += (0).to_bytes(4, byteorder='little')  # Y pixels per meter
    bmp_header += (0).to_bytes(4, byteorder='little')  # Colors used
    bmp_header += (0).to_bytes(4, byteorder='little')  # Important colors

    with open(file_path, 'wb') as file:
        file.write(bmp_header)
        for _ in range(height):
            for _ in range(width):
                file.write(bytes(color))

# Create ./tmp/ directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample BMP file
width, height = 100, 100
color = (255, 0, 0)  # RGB color (red)
create_bmp_file('./tmp/sample.bmp', width, height, color)