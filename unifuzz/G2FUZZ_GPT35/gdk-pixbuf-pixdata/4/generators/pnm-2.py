import numpy as np
import os

def save_pbm(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(b'P4\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        np.packbits(data, axis=1).tofile(f)

def save_pgm(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(b'P5\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        f.write(b'255\n')
        data.astype(np.uint8).tofile(f)

def save_ppm(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(b'P6\n')
        f.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        f.write(b'255\n')
        data.astype(np.uint8).tofile(f)

# Create temporary directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate example data
data_pbm = np.random.randint(0, 2, size=(100, 100))  # Random binary data for PBM
data_pgm = np.random.randint(0, 256, size=(100, 100))  # Random grayscale data for PGM
data_ppm = np.random.randint(0, 256, size=(100, 100, 3))  # Random color data for PPM

# Save generated data into .tmp directory
save_pbm('./tmp/example.pbm', data_pbm)
save_pgm('./tmp/example.pgm', data_pgm)
save_ppm('./tmp/example.ppm', data_ppm)