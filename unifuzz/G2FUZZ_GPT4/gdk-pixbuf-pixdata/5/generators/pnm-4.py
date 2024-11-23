import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Function to generate a PBM file
def generate_pbm(filename, width, height):
    with open(filename, 'w') as f:
        f.write("P1\n")  # Magic number for PBM
        f.write(f"{width} {height}\n")
        for _ in range(height):
            line = ' '.join(str(np.random.randint(0, 2)) for _ in range(width))
            f.write(line + '\n')

# Function to generate a PGM file
def generate_pgm(filename, width, height, maxval=255):
    with open(filename, 'w') as f:
        f.write("P2\n")  # Magic number for PGM
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for _ in range(height):
            line = ' '.join(str(np.random.randint(0, maxval + 1)) for _ in range(width))
            f.write(line + '\n')

# Function to generate a PPM file
def generate_ppm(filename, width, height, maxval=255):
    with open(filename, 'w') as f:
        f.write("P3\n")  # Magic number for PPM
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for _ in range(height):
            line = ' '.join(f"{np.random.randint(0, maxval + 1)} {np.random.randint(0, maxval + 1)} {np.random.randint(0, maxval + 1)}" for _ in range(width))
            f.write(line + '\n')

# Parameters for the image
width, height = 100, 100

# Generate PBM, PGM, and PPM files
generate_pbm("./tmp/example.pbm", width, height)
generate_pgm("./tmp/example.pgm", width, height)
generate_ppm("./tmp/example.ppm", width, height)