import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example - A simple black and white image
pbm_data = np.array([[1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0]])

pbm_header = "P1\n# This is a PBM example\n5 4\n"
pbm_path = './tmp/example.pbm'
with open(pbm_path, 'w') as f:
    f.write(pbm_header + '\n'.join(' '.join(str(pixel) for pixel in row) for row in pbm_data))

# PGM example - A grayscale image
pgm_data = np.array([[0, 50, 100, 150, 200],
                     [200, 150, 100, 50, 0],
                     [0, 50, 100, 150, 200],
                     [200, 150, 100, 50, 0]])

pgm_header = "P2\n# This is a PGM example\n5 4\n255\n"
pgm_path = './tmp/example.pgm'
with open(pgm_path, 'w') as f:
    f.write(pgm_header + '\n'.join(' '.join(str(pixel) for pixel in row) for row in pgm_data))

# PPM example - A colored image
ppm_data = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 255, 255]],
                     [[255, 255, 255], [255, 255, 0], [0, 0, 255], [0, 255, 0], [255, 0, 0]],
                     [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 255, 255]],
                     [[255, 255, 255], [255, 255, 0], [0, 0, 255], [0, 255, 0], [255, 0, 0]]])

ppm_header = "P3\n# This is a PPM example\n5 4\n255\n"
ppm_path = './tmp/example.ppm'
with open(ppm_path, 'w') as f:
    f.write(ppm_header + '\n'.join(' '.join(str(value) for value in pixel) for row in ppm_data for pixel in row))