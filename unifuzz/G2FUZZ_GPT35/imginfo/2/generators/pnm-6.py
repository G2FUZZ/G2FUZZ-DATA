import numpy as np

def generate_pbm(width, height):
    data = np.random.randint(0, 2, (height, width), dtype=np.uint8)
    return data

def save_pbm(data, filename):
    with open(filename, 'wb') as file:
        file.write(b'P4\n')
        file.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        np.packbits(data, axis=1).tofile(file)

def generate_pgm(width, height):
    data = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    return data

def save_pgm(data, filename):
    with open(filename, 'wb') as file:
        file.write(b'P5\n')
        file.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        file.write(b'255\n')
        data.tofile(file)

def generate_ppm(width, height):
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return data

def save_ppm(data, filename):
    with open(filename, 'wb') as file:
        file.write(b'P6\n')
        file.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        file.write(b'255\n')
        data.tofile(file)

# Generate and save PBM file
width, height = 10, 10
pbm_data = generate_pbm(width, height)
pbm_filename = './tmp/image.pbm'
save_pbm(pbm_data, pbm_filename)

# Generate and save PGM file
pgm_data = generate_pgm(width, height)
pgm_filename = './tmp/image.pgm'
save_pgm(pgm_data, pgm_filename)

# Generate and save PPM file
ppm_data = generate_ppm(width, height)
ppm_filename = './tmp/image.ppm'
save_ppm(ppm_data, ppm_filename)