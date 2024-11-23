import numpy as np
import os

def create_pbm(filename, width, height):
    """Create a simple PBM file with alternating black and white pixels."""
    data = np.zeros((height, width), dtype=np.bool_)
    data[::2, ::2] = 1  # Set every other pixel to white
    data[1::2, 1::2] = 1
    np.savetxt(filename, data, fmt='%i', header='P1\n# PBM example\n{} {}'.format(width, height), comments='')

def create_pgm(filename, width, height):
    """Create a simple PGM file with a gradient from black to white."""
    data = np.tile(np.arange(height, dtype=np.uint8), (width, 1)).T
    np.savetxt(filename, data, fmt='%i', header='P2\n# PGM example\n{} {}\n255'.format(width, height), comments='')

def create_ppm(filename, width, height):
    """Create a simple PPM file with red, green, and blue vertical stripes."""
    data = np.zeros((height, width, 3), dtype=np.uint8)
    data[:, :width // 3, 0] = 255  # Red stripe
    data[:, width // 3: 2 * width // 3, 1] = 255  # Green stripe
    data[:, 2 * width // 3:, 2] = 255  # Blue stripe
    header = 'P3\n# PPM example\n{} {}\n255\n'.format(width, height)
    with open(filename, 'w') as f:
        f.write(header)
        for row in data:
            np.savetxt(f, row.reshape(-1, 3), fmt='%i')

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create PNM files
create_pbm('./tmp/example.pbm', 10, 10)
create_pgm('./tmp/example.pgm', 10, 10)
create_ppm('./tmp/example.ppm', 10, 10)

print("PNM files generated successfully.")