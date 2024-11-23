import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a PBM file (Black & White image)
pbm_data = "P1\n# This is a PBM file\n5 5\n1 1 1 1 1\n1 0 0 0 1\n1 0 1 0 1\n1 0 0 0 1\n1 1 1 1 1\n"
with open('./tmp/sample.pbm', 'w') as file:
    file.write(pbm_data)

# Generate a PGM file (Grayscale image)
pgm_data = "P2\n# This is a PGM file\n5 5\n255\n255 255 255 255 255\n255 100 100 100 255\n255 100 255 100 255\n255 100 100 100 255\n255 255 255 255 255\n"
with open('./tmp/sample.pgm', 'w') as file:
    file.write(pgm_data)

# Generate a PPM file (Colored image)
ppm_data = "P3\n# This is a PPM file\n5 5\n255\n255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n255 0 0 0 255 0 0 255 0 0 255 0 255 0 0\n255 0 0 0 255 0 255 255 255 0 255 0 255 0 0\n255 0 0 0 255 0 0 255 0 0 255 0 255 0 0\n255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n"
with open('./tmp/sample.ppm', 'w') as file:
    file.write(ppm_data)