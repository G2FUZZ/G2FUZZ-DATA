import os
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to save PBM file
def save_pbm(filename, data):
    with open(filename, 'w') as f:
        f.write('P1\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        for row in data:
            f.write(' '.join(str(val) for val in row) + '\n')

# Function to save PGM file with specified max_val (bit depth)
def save_pgm(filename, data, max_val=255):
    with open(filename, 'w') as f:
        f.write('P2\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write(str(max_val) + '\n')
        for row in data:
            f.write(' '.join(str(val) for val in row) + '\n')

# Function to save PPM file
def save_ppm(filename, data):
    max_val = 255
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n')
        f.write(str(max_val) + '\n')
        for row in data:
            for val in row:
                f.write(' '.join(str(channel) for channel in val) + ' ')
            f.write('\n')

# Create a simple PBM image
pbm_data = np.random.randint(0, 2, (5, 5))
save_pbm('./tmp/sample.pbm', pbm_data)

# Create a PGM image with a bit depth of 16 (max value 65535)
pgm_data = np.random.randint(0, 65536, (5, 5))
save_pgm('./tmp/sample_16bit.pgm', pgm_data, max_val=65535)

# Create a simple PPM image
ppm_data = np.random.randint(0, 256, (5, 5, 3))
save_ppm('./tmp/sample.ppm', ppm_data)