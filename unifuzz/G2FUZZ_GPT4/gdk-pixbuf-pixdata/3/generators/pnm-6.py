import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a PBM file (Portable Bitmap)
pbm_data = "P1\n# This is a PBM file\n5 5\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0"
with open('./tmp/example.pbm', 'w') as f:
    f.write(pbm_data)

# Generate a PGM file (Portable Graymap)
pgm_data = "P2\n# This is a PGM file\n5 5\n255\n0 255 0 255 0\n255 0 255 0 255\n0 255 0 255 0\n255 0 255 0 255\n0 255 0 255 0"
with open('./tmp/example.pgm', 'w') as f:
    f.write(pgm_data)

# Generate a PPM file (Portable Pixmap)
ppm_data = "P3\n# This is a PPM file\n5 5\n255\n255 0 0 0 255 0 0 255 0 0 0 255\n0 255 0 255 0 0 0 255 0 255 0 0\n255 0 0 0 255 0 0 255 0 0 0 255\n0 255 0 255 0 0 0 255 0 255 0 0"
with open('./tmp/example.ppm', 'w') as f:
    f.write(ppm_data)