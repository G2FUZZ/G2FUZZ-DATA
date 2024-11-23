import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple PBM file (Black & White)
pbm_data = "P1\n# This is a simple PBM file\n4 4\n0 1 0 1\n1 0 1 0\n0 1 0 1\n1 0 1 0"
with open('./tmp/simple.pbm', 'w') as f:
    f.write(pbm_data)

# Create a simple PGM file (Grayscale)
pgm_data = "P2\n# This is a simple PGM file\n4 4\n255\n0 255 0 255\n255 0 255 0\n0 255 0 255\n255 0 255 0"
with open('./tmp/simple.pgm', 'w') as f:
    f.write(pgm_data)

# Create a simple PPM file (Color)
ppm_data = "P3\n# This is a simple PPM file\n4 4\n255\n255 0 0  0 255 0  0 0 255  255 255 0\n0 255 255  255 0 255  255 255 255  0 0 0\n255 0 0  0 255 0  0 0 255  255 255 0\n0 255 255  255 0 255  255 255 255  0 0 0"
with open('./tmp/simple.ppm', 'w') as f:
    f.write(ppm_data)

print("PNM files created in ./tmp/")