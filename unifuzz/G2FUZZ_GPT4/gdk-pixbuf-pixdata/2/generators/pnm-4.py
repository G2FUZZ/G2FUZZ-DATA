import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example (Portable Bitmap) - A simple black and white image
pbm_data = "P1\n# This is a PBM file\n2 2\n1 0\n0 1"
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# PGM example (Portable Graymap) - A simple grayscale image
pgm_data = "P2\n# This is a PGM file\n2 2\n255\n255 0\n120 135"
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)

# PPM example (Portable Pixmap) - A simple colored image
ppm_data = "P3\n# This is a PPM file\n2 2\n255\n255 0 0  0 255 0\n0 0 255  255 255 0"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)