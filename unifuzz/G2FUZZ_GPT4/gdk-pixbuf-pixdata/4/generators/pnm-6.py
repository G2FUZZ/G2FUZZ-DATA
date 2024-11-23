import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example - simple black and white image
pbm_data = "P1\n# This is a PBM example\n2 2\n0 1\n1 0\n"
pbm_path = './tmp/example.pbm'
with open(pbm_path, 'w') as file:
    file.write(pbm_data)

# PGM example - simple grayscale image
pgm_data = "P2\n# This is a PGM example\n2 2\n255\n0 255\n255 0\n"
pgm_path = './tmp/example.pgm'
with open(pgm_path, 'w') as file:
    file.write(pgm_data)

# PPM example - simple color image
ppm_data = "P3\n# This is a PPM example\n2 2\n255\n255 0 0  0 255 0\n0 0 255  255 255 0\n"
ppm_path = './tmp/example.ppm'
with open(ppm_path, 'w') as file:
    file.write(ppm_data)

print("PNM files created successfully in ./tmp/")