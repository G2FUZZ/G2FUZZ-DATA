import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM (Portable BitMap) - A simple black and white image
pbm_data = "P1\n# This is a minimal PBM file with a 2x2 bitmap.\n2 2\n0 1\n1 0"
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# PGM (Portable GrayMap) - A simple grayscale image
pgm_data = "P2\n# This is a minimal PGM file with a 2x2 grayscale bitmap.\n2 2\n255\n0 255\n255 0"
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)

# PPM (Portable PixMap) - A simple color image
ppm_data = "P3\n# This is a minimal PPM file with a 2x2 color bitmap.\n2 2\n255\n255 0 0   0 255 0\n0 0 255   255 255 255"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)

print("PNM files have been generated in ./tmp/")