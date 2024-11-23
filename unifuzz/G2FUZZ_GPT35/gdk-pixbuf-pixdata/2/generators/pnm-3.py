import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate PBM file
pbm_content = "P1\n# This is a PBM file\n3 2\n1 0 1\n0 1 0"
with open('./tmp/example.pbm', 'w') as pbm_file:
    pbm_file.write(pbm_content)

# Generate PGM file
pgm_content = "P2\n# This is a PGM file\n3 2\n255\n100 50 150\n200 75 25"
with open('./tmp/example.pgm', 'w') as pgm_file:
    pgm_file.write(pgm_content)

# Generate PPM file
ppm_content = "P3\n# This is a PPM file\n3 2\n255\n100 50 150 200 75 25\n50 100 200 25 75 175"
with open('./tmp/example.ppm', 'w') as ppm_file:
    ppm_file.write(ppm_content)