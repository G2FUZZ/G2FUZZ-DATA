import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate PBM file (monochrome)
pbm_data = "P1\n# This is a PBM file\n5 5\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1"
with open('./tmp/monochrome.pbm', 'w') as f:
    f.write(pbm_data)

# Generate PGM file (grayscale)
pgm_data = "P2\n# This is a PGM file\n5 5 255\n100 150 200 150 100\n150 200 250 200 150\n200 250 300 250 200\n150 200 250 200 150\n100 150 200 150 100"
with open('./tmp/grayscale.pgm', 'w') as f:
    f.write(pgm_data)

# Generate PPM file (color)
ppm_data = "P3\n# This is a PPM file\n2 2 255\n255 0 0  0 255 0\n0 0 255  255 255 0"
with open('./tmp/color.ppm', 'w') as f:
    f.write(ppm_data)