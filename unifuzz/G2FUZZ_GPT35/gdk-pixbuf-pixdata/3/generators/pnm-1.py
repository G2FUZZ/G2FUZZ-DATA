import os

def generate_pbm_file():
    # PBM (Portable Bitmap) format
    with open('./tmp/image.pbm', 'w') as f:
        f.write("P1\n")
        f.write("4 4\n")
        f.write("0 1 0 1\n")
        f.write("1 0 1 0\n")
        f.write("0 1 0 1\n")
        f.write("1 0 1 0\n")

def generate_pgm_file():
    # PGM (Portable Graymap) format
    with open('./tmp/image.pgm', 'w') as f:
        f.write("P2\n")
        f.write("4 4\n")
        f.write("255\n")
        for _ in range(16):
            f.write("128 ")

def generate_ppm_file():
    # PPM (Portable Pixmap) format
    with open('./tmp/image.ppm', 'w') as f:
        f.write("P3\n")
        f.write("4 4\n")
        f.write("255\n")
        for _ in range(16):
            f.write("255 0 0 ")

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pbm_file()
generate_pgm_file()
generate_ppm_file()