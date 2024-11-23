import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a PBM file
def generate_pbm(filename, width, height):
    data = np.random.choice([0, 1], (height, width))
    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        for row in data:
            row_str = ' '.join(str(val) for val in row)
            f.write(row_str + '\n')

# Function to generate a PGM file
def generate_pgm(filename, width, height, maxval):
    data = np.random.randint(0, maxval + 1, (height, width), dtype=np.uint16 if maxval > 255 else np.uint8)
    with open(filename, 'wb') as f:
        f.write(f"P5\n{width} {height}\n{maxval}\n".encode('ascii'))
        f.write(data.tobytes())

# Function to generate a PPM file
def generate_ppm(filename, width, height, maxval):
    data = np.random.randint(0, maxval + 1, (height, width, 3), dtype=np.uint16 if maxval > 255 else np.uint8)
    with open(filename, 'wb') as f:
        f.write(f"P6\n{width} {height}\n{maxval}\n".encode('ascii'))
        f.write(data.tobytes())

# Generate and save the files
generate_pbm('./tmp/sample.pbm', 100, 100)  # PBM file, 1 bit depth
generate_pgm('./tmp/sample_8bit.pgm', 100, 100, 255)  # PGM file, 8 bits depth
generate_pgm('./tmp/sample_16bit.pgm', 100, 100, 65535)  # PGM file, 16 bits depth
generate_ppm('./tmp/sample_8bit.ppm', 100, 100, 255)  # PPM file, 8 bits depth per channel
generate_ppm('./tmp/sample_16bit.ppm', 100, 100, 65535)  # PPM file, 16 bits depth per channel

print("PNM files generated successfully.")