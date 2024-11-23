import os
import numpy as np

def ensure_dir(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)

def generate_pbm(file_path, data):
    """Generate a PBM file from a numpy array."""
    header = f"P1\n{data.shape[1]} {data.shape[0]}\n"
    body = '\n'.join(' '.join(str(val) for val in row) for row in data)
    with open(file_path, 'w') as file:
        file.write(header + body)

def generate_pgm(file_path, data):
    """Generate a PGM file from a numpy array."""
    header = f"P2\n{data.shape[1]} {data.shape[0]}\n255\n"
    body = '\n'.join(' '.join(str(val) for val in row) for row in data)
    with open(file_path, 'w') as file:
        file.write(header + body)

def generate_ppm(file_path, data):
    """Generate a PPM file from a numpy array."""
    header = f"P3\n{data.shape[1]} {data.shape[0]}\n255\n"
    body = '\n'.join(' '.join(str(value) for value in pixel) for row in data for pixel in row)
    with open(file_path, 'w') as file:
        file.write(header + body.replace('] [', ' ') + '\n')

# Directory for generated files
directory = './tmp/'
ensure_dir(directory)

# Create a simple black and white image for PBM
pbm_data = np.array([[1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1]])
generate_pbm(directory + 'sample.pbm', pbm_data)

# Create a simple grayscale image for PGM
pgm_data = np.array([[100, 150, 200, 150, 100],
                     [150, 200, 250, 200, 150],
                     [100, 150, 200, 150, 100]])
generate_pgm(directory + 'sample.pgm', pgm_data)

# Create a simple color image for PPM
ppm_data = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                     [[0, 255, 0], [0, 0, 255], [255, 0, 0]],
                     [[0, 0, 255], [255, 0, 0], [0, 255, 0]]])
generate_ppm(directory + 'sample.ppm', ppm_data)