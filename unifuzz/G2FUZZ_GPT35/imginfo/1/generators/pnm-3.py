import numpy as np

def create_pbm_file(filename, width, height):
    data = np.random.randint(0, 2, (height, width), dtype=np.uint8)
    with open(filename, 'wb') as f:
        f.write(b'P1\n')
        f.write(f'{width} {height}\n'.encode())
        np.savetxt(f, data, fmt='%d')

def create_pgm_file(filename, width, height):
    data = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    with open(filename, 'wb') as f:
        f.write(b'P2\n')
        f.write(f'{width} {height}\n'.encode())
        f.write(b'255\n')
        np.savetxt(f, data, fmt='%d')

def create_ppm_file(filename, width, height):
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    with open(filename, 'wb') as f:
        f.write(b'P3\n')
        f.write(f'{width} {height}\n'.encode())
        f.write(b'255\n')
        np.savetxt(f, data.reshape(-1, 3), fmt='%d')

import os

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_pbm_file('./tmp/image_pbm.pbm', 10, 10)
create_pgm_file('./tmp/image_pgm.pgm', 10, 10)
create_ppm_file('./tmp/image_ppm.ppm', 10, 10)