import os
import numpy as np

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to save a PBM file
def save_pbm(filename, data):
    with open(filename, 'w') as f:
        f.write('P1\n')  # Magic number for PBM plain format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        for row in data:
            f.write(' '.join(str(val) for val in row) + '\n')

# Function to save a PGM file
def save_pgm(filename, data):
    with open(filename, 'w') as f:
        f.write('P2\n')  # Magic number for PGM plain format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write('255\n')  # Max value
        for row in data:
            f.write(' '.join(str(val) for val in row) + '\n')

# Function to save a PPM file
def save_ppm(filename, data):
    with open(filename, 'w') as f:
        f.write('P3\n')  # Magic number for PPM plain format
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write('255\n')  # Max value
        for row in data:
            for pixel in row:
                f.write(' '.join(str(val) for val in pixel) + ' ')
            f.write('\n')

# Sample data for PBM (bitmaps)
pbm_data = np.random.randint(2, size=(5, 5))

# Sample data for PGM (grayscale images)
pgm_data = np.random.randint(256, size=(5, 5))

# Sample data for PPM (color images)
ppm_data = np.random.randint(256, size=(5, 5, 3))

# Saving files
save_pbm(os.path.join(output_dir, 'sample.pbm'), pbm_data)
save_pgm(os.path.join(output_dir, 'sample.pgm'), pgm_data)
save_ppm(os.path.join(output_dir, 'sample.ppm'), ppm_data)

print("PNM files have been generated and saved in './tmp/'.")