import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple pattern for each PNM type
# PBM pattern - A simple checkerboard
pbm_data = np.zeros((10, 10), dtype=np.uint8)
pbm_data[1::2, ::2] = 1
pbm_data[::2, 1::2] = 1
pbm_path = './tmp/checkerboard.pbm'
with open(pbm_path, 'w') as f:
    f.write('P1\n10 10\n')
    np.savetxt(f, pbm_data, fmt='%i', delimiter=' ')

# PGM pattern - A gradient
pgm_data = np.tile(np.arange(10), (10, 1))
pgm_path = './tmp/gradient.pgm'
with open(pgm_path, 'w') as f:
    f.write('P2\n10 10\n255\n')
    np.savetxt(f, pgm_data, fmt='%i', delimiter=' ')

# PPM pattern - Simple RGB stripes
ppm_data = np.zeros((10, 10, 3), dtype=np.uint8)
ppm_data[:, :3, 0] = 255  # Red stripe
ppm_data[:, 3:6, 1] = 255  # Green stripe
ppm_data[:, 6:, 2] = 255  # Blue stripe
ppm_path = './tmp/stripes.ppm'
with open(ppm_path, 'w') as f:
    f.write('P3\n10 10\n255\n')
    for row in ppm_data:
        np.savetxt(f, row.reshape(-1, 3), fmt='%i', delimiter=' ')

print("PNM files generated in ./tmp/")