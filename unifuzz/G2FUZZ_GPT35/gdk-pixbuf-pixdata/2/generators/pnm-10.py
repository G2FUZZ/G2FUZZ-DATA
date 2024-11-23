import numpy as np

def save_pnm_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def create_pbm(width, height, data):
    encoded_data = bytearray()
    encoded_data += f"P1\n{width} {height}\n".encode()
    for row in data:
        encoded_data += " ".join(str(pixel) for pixel in row).encode() + b'\n'
    return encoded_data

def create_pgm(width, height, max_val, data):
    encoded_data = bytearray()
    encoded_data += f"P2\n{width} {height}\n{max_val}\n".encode()
    for row in data:
        encoded_data += " ".join(str(pixel) for pixel in row).encode() + b'\n'
    return encoded_data

def create_ppm(width, height, max_val, data):
    encoded_data = bytearray()
    encoded_data += f"P3\n{width} {height}\n{max_val}\n".encode()
    for row in data:
        encoded_data += " ".join(str(val) for pixel in row for val in pixel).encode() + b'\n'
    return encoded_data

# Creating sample data
width = 5
height = 5
max_val = 255
pbm_data = np.random.randint(0, 2, (height, width))  # Random binary data for PBM
pgm_data = np.random.randint(0, max_val + 1, (height, width))  # Random gray scale data for PGM
ppm_data = np.random.randint(0, max_val + 1, (height, width, 3))  # Random RGB data for PPM

# Saving PNM files
save_pnm_file('./tmp/sample.pbm', create_pbm(width, height, pbm_data))
save_pnm_file('./tmp/sample.pgm', create_pgm(width, height, max_val, pgm_data))
save_pnm_file('./tmp/sample.ppm', create_ppm(width, height, max_val, ppm_data))