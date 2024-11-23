import numpy as np
import os

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a PBM file (monochrome bitmap)
def generate_pbm(filename):
    header = b"P4\n# PBM Example\n5 5\n"
    data = np.array([[1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1]], dtype=bool)
    with open(filename, 'wb') as f:
        f.write(header)
        for row in data:
            byte = 0
            for bit in row:
                byte = (byte << 1) | bit
            f.write(bytearray([byte]))

# Function to generate a PGM file (grayscale)
def generate_pgm(filename):
    header = b"P5\n# PGM Example\n5 5\n255\n"
    data = np.array([[255, 127, 63, 127, 255],
                     [127, 63, 31, 63, 127],
                     [63, 31, 15, 31, 63],
                     [127, 63, 31, 63, 127],
                     [255, 127, 63, 127, 255]], dtype=np.uint8)
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data.tobytes())

# Function to generate a PPM file (color)
def generate_ppm(filename):
    header = b"P6\n# PPM Example\n5 5\n255\n"
    data = np.zeros((5, 5, 3), dtype=np.uint8)
    # Fill with a simple pattern: red and green stripes
    data[:, ::2, 0] = 255  # Red channel
    data[:, 1::2, 1] = 255  # Green channel
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data.tobytes())

# Generate and save the files
generate_pbm(os.path.join(output_dir, 'example.pbm'))
generate_pgm(os.path.join(output_dir, 'example.pgm'))
generate_ppm(os.path.join(output_dir, 'example.ppm'))