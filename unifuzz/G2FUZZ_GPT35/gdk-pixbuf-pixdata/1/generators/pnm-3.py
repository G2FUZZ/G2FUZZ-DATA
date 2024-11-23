import numpy as np
import os

def create_pbm_file():
    image_data = np.random.randint(0, 2, size=(10, 10), dtype=np.uint8)  # Generating random black and white image
    with open('./tmp/image.pbm', 'w') as f:
        f.write("P1\n")  # Magic number for PBM file
        f.write("10 10\n")  # Image width and height
        for row in image_data:
            f.write(" ".join(str(pix) for pix in row) + "\n")

def create_pgm_file():
    image_data = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)  # Generating random grayscale image
    with open('./tmp/image.pgm', 'w') as f:
        f.write("P2\n")  # Magic number for PGM file
        f.write("10 10\n")  # Image width and height
        f.write("255\n")  # Max grayscale value
        for row in image_data:
            f.write(" ".join(str(pix) for pix in row) + "\n")

def create_ppm_file():
    image_data = np.random.randint(0, 256, size=(10, 10, 3), dtype=np.uint8)  # Generating random color image
    with open('./tmp/image.ppm', 'w') as f:
        f.write("P3\n")  # Magic number for PPM file
        f.write("10 10\n")  # Image width and height
        f.write("255\n")  # Max color value
        for row in image_data:
            f.write(" ".join(str(pix) for pix in row.flatten()) + "\n")

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create PBM, PGM, and PPM files
create_pbm_file()
create_pgm_file()
create_ppm_file()