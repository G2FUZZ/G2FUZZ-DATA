import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM file generation (Bit depth: 1)
pbm_data = "P1\n# This is a PBM file\n4 4\n0 1 0 1\n1 0 1 0\n0 1 0 1\n1 0 1 0\n"
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# PGM file generation (Bit depth: up to 16 bits, here we use 8 bit)
pgm_data = "P2\n# This is a PGM file\n4 4\n255\n0 255 0 255\n255 100 255 100\n0 255 0 255\n255 100 255 100\n"
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)

# PPM file generation (Bit depth: up to 16 bits, here we use 8 bit for each RGB channel)
ppm_data = "P3\n# This is a PPM file\n4 4\n255\n255 0 0 0 255 0 0 0 255 255 0 0\n0 255 0 255 0 0 0 255 0 255 0 0\n255 0 0 0 255 0 0 0 255 255 0 0\n0 255 0 255 0 0 0 255 0 255 0 0\n"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)