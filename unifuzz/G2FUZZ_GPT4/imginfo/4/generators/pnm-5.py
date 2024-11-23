import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple black and white image for PBM
pbm_data = np.array([[1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1]])
pbm_path = './tmp/sample.pbm'
with open(pbm_path, 'w') as f:
    f.write('P1\n')  # Magic number for PBM
    f.write(f'{pbm_data.shape[1]} {pbm_data.shape[0]}\n')
    for row in pbm_data:
        f.write(' '.join(str(val) for val in row) + '\n')

# Create a simple grayscale image for PGM
pgm_data = np.array([[100, 150, 200, 150, 100],
                     [150, 200, 250, 200, 150],
                     [100, 150, 200, 150, 100]])
pgm_path = './tmp/sample.pgm'
with open(pgm_path, 'w') as f:
    f.write('P2\n')  # Magic number for PGM
    f.write(f'{pgm_data.shape[1]} {pgm_data.shape[0]}\n')
    f.write('255\n')  # Max value
    for row in pgm_data:
        f.write(' '.join(str(val) for val in row) + '\n')

# Create a simple color image for PPM
ppm_data = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                     [[0, 255, 0], [0, 0, 255], [255, 0, 0]],
                     [[0, 0, 255], [255, 0, 0], [0, 255, 0]]])
ppm_path = './tmp/sample.ppm'
with open(ppm_path, 'w') as f:
    f.write('P3\n')  # Magic number for PPM
    f.write(f'{ppm_data.shape[1]} {ppm_data.shape[0]}\n')
    f.write('255\n')  # Max value
    for row in ppm_data:
        for pixel in row:
            f.write(' '.join(str(value) for value in pixel) + ' ')
        f.write('\n')