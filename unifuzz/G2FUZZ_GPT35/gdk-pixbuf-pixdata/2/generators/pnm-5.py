import numpy as np
import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate PBM file
pbm_data = np.random.randint(0, 2, size=(10, 10))
with open('./tmp/example.pbm', 'w') as f:
    f.write("P1\n")
    f.write("# This is a PBM file\n")
    f.write("{} {}\n".format(pbm_data.shape[1], pbm_data.shape[0]))
    for row in pbm_data:
        f.write(" ".join(map(str, row)) + "\n")

# Generate PGM file
pgm_data = np.random.randint(0, 256, size=(10, 10))
with open('./tmp/example.pgm', 'w') as f:
    f.write("P2\n")
    f.write("# This is a PGM file\n")
    f.write("{} {}\n".format(pgm_data.shape[1], pgm_data.shape[0]))
    f.write("255\n")
    for row in pgm_data:
        f.write(" ".join(map(str, row)) + "\n")

# Generate PPM file
ppm_data = np.random.randint(0, 256, size=(10, 10, 3))
with open('./tmp/example.ppm', 'w') as f:
    f.write("P3\n")
    f.write("# This is a PPM file\n")
    f.write("{} {}\n".format(ppm_data.shape[1], ppm_data.shape[0]))
    f.write("255\n")
    for row in ppm_data:
        for pixel in row:
            f.write(" ".join(map(str, pixel)) + " ")
        f.write("\n")