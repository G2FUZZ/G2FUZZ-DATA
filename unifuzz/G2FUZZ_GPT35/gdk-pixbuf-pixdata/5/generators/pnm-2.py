import os

def create_pbm_file():
    with open('./tmp/monochrome_image.pbm', 'w') as f:
        f.write("P1\n")
        f.write("3 3\n")
        f.write("0 1 0\n")
        f.write("1 0 1\n")
        f.write("0 1 0\n")

def create_pgm_file():
    with open('./tmp/grayscale_image.pgm', 'w') as f:
        f.write("P2\n")
        f.write("3 3\n")
        f.write("255\n")
        f.write("100 150 200\n")
        f.write("50 75 125\n")
        f.write("25 175 230\n")

def create_ppm_file():
    with open('./tmp/rgb_image.ppm', 'w') as f:
        f.write("P3\n")
        f.write("3 3\n")
        f.write("255\n")
        f.write("255 0 0 0 255 0 0 0 255\n")
        f.write("0 255 0 0 0 255 0 255 0\n")
        f.write("0 0 255 255 0 0 255 0 0\n")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

create_pbm_file()
create_pgm_file()
create_ppm_file()