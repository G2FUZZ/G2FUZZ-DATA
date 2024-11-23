import os

def create_pbm_file():
    image_data = "P1\n# This is a PBM file\n3 2\n1 0 1\n0 1 0"
    with open('./tmp/image.pbm', 'w') as file:
        file.write(image_data)

def create_pgm_file():
    image_data = "P2\n# This is a PGM file\n3 2\n255\n100 150 200\n50 75 125"
    with open('./tmp/image.pgm', 'w') as file:
        file.write(image_data)

def create_ppm_file():
    image_data = "P3\n# This is a PPM file\n2 2\n255\n255 0 0 0 255 0\n0 255 255 255 0 255"
    with open('./tmp/image.ppm', 'w') as file:
        file.write(image_data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

create_pbm_file()
create_pgm_file()
create_ppm_file()