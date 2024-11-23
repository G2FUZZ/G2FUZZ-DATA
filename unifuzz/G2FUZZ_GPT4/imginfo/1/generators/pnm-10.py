import os
import numpy as np

# Create the ./tmp/ directory if it does not exist
os.makedirs("./tmp/", exist_ok=True)

# Function to generate a PBM file
def generate_pbm(filename, width, height):
    # Create a checkerboard pattern
    data = np.zeros((height, width), dtype=bool)
    data[1::2, ::2] = 1
    data[::2, 1::2] = 1
    
    with open(filename, 'w') as f:
        f.write("P1\n")  # Magic number for PBM file format
        f.write(f"{width} {height}\n")
        for row in data:
            line = ' '.join(['1' if pixel else '0' for pixel in row])
            f.write(f"{line}\n")

# Function to generate a PGM file
def generate_pgm(filename, width, height):
    # Create a gradient pattern
    data = np.arange(width*height, dtype=np.uint8).reshape((height, width))
    
    with open(filename, 'w') as f:
        f.write("P2\n")  # Magic number for PGM file format
        f.write(f"{width} {height}\n")
        f.write("255\n")  # Max gray value
        for row in data:
            line = ' '.join(map(str, row))
            f.write(f"{line}\n")

# Function to generate a PPM file
def generate_ppm(filename, width, height):
    # Create an RGB pattern
    data = np.zeros((height, width, 3), dtype=np.uint8)
    data[:, :, 0] = np.arange(height).reshape((height, 1))  # Red gradient
    data[:, :, 1] = np.arange(width)  # Green gradient
    data[:, :, 2] = 128  # Constant blue
    
    with open(filename, 'w') as f:
        f.write("P3\n")  # Magic number for PPM file format
        f.write(f"{width} {height}\n")
        f.write("255\n")  # Max color value
        for row in data:
            for pixel in row:
                line = ' '.join(map(str, pixel))
                f.write(f"{line}\n")

# Generate files
generate_pbm("./tmp/checkerboard.pbm", 10, 10)
generate_pgm("./tmp/gradient.pgm", 10, 10)
generate_ppm("./tmp/rgb_gradient.ppm", 10, 10)