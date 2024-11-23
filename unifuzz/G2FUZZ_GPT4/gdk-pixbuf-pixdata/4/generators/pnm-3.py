import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to save a PBM file (1 bit per pixel)
def save_pbm(filename, image):
    with open(filename, 'w') as f:
        f.write('P1\n')
        f.write(f'{image.shape[1]} {image.shape[0]}\n')
        for row in image:
            f.write(' '.join(str(p) for p in row) + '\n')

# Function to save a PGM file (8 bits per pixel)
def save_pgm(filename, image):
    with open(filename, 'w') as f:
        f.write('P2\n')
        f.write(f'{image.shape[1]} {image.shape[0]}\n255\n')
        for row in image:
            f.write(' '.join(str(p) for p in row) + '\n')

# Function to save a PPM file (16 bits per pixel)
def save_ppm(filename, image):
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{image.shape[1]} {image.shape[0]}\n65535\n')
        for row in image:
            for pixel in row:
                f.write(' '.join(str(channel) for channel in pixel) + ' ')
            f.write('\n')

# Generate a simple PBM image (binary image)
pbm_image = np.random.randint(0, 2, (5, 5), dtype=np.uint8)
save_pbm('./tmp/sample.pbm', pbm_image)

# Generate a simple PGM image (grayscale image)
pgm_image = np.random.randint(0, 256, (5, 5), dtype=np.uint8)
save_pgm('./tmp/sample.pgm', pgm_image)

# Generate a simple PPM image (color image with 3 channels, 16-bit depth)
ppm_image = np.random.randint(0, 65536, (5, 5, 3), dtype=np.uint16)
save_ppm('./tmp/sample.ppm', ppm_image)

print('PNM files have been generated and saved in ./tmp/')