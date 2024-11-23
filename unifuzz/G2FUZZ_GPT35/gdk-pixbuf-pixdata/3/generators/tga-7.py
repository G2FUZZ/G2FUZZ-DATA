import struct
import os

def create_tga_file(file_path, width, height):
    # TGA Header
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, (width & 0x00FF), (width & 0xFF00) >> 8, (height & 0x00FF), (height & 0xFF00) >> 8, 24, 0])

    with open(file_path, 'wb') as f:
        f.write(header)

        # Color correction data
        gamma = 2.2
        gamma_int = min(255, max(0, int(gamma * 255)))  # Ensure gamma value is within range
        f.write(bytearray([gamma_int] * 256))  # Gamma values

        for i in range(256):  # Color map entries
            f.write(bytearray([i, i, i]))

        # Image data (dummy data)
        for _ in range(width * height):
            f.write(bytearray([0, 255, 0]))  # RGB pixel data

# Create tmp directory if not exists
os.makedirs('tmp', exist_ok=True)

# Generate TGA file with color correction features
create_tga_file('./tmp/color_correction.tga', 128, 128)