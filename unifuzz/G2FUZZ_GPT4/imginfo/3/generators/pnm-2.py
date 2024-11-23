import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to save a PBM file
def save_pbm(filename, data):
    with open(filename, 'w') as f:
        f.write('P1\n')  # Magic number for PBM file format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        for row in data:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

# Function to save a PGM file
def save_pgm(filename, data):
    with open(filename, 'w') as f:
        f.write('P2\n')  # Magic number for PGM file format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write('255\n')  # Max value
        for row in data:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

# Function to save a PPM file
def save_ppm(filename, data):
    with open(filename, 'w') as f:
        f.write('P3\n')  # Magic number for PPM file format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write('255\n')  # Max value
        for row in data:
            for pixel in row:
                f.write(' '.join(str(channel) for channel in pixel) + ' ')
            f.write('\n')

# Generate a black and white image (PBM)
bw_data = np.random.randint(2, size=(100, 100))  # 100x100 pixels, values 0 or 1
save_pbm('./tmp/sample_bw.pbm', bw_data)

# Generate a grayscale image (PGM)
gray_data = np.random.randint(256, size=(100, 100))  # 100x100 pixels, values 0-255
save_pgm('./tmp/sample_gray.pgm', gray_data)

# Generate a full-color image (PPM)
color_data = np.random.randint(256, size=(100, 100, 3))  # 100x100 pixels, 3 channels (RGB), values 0-255
save_ppm('./tmp/sample_color.ppm', color_data)