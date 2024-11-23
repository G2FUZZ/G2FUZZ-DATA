import os

def create_pbm_file():
    header = "P1\n# This is a PBM file\n2 2\n"
    data = "0 1\n1 0\n"
    with open('./tmp/sample.pbm', 'w') as file:
        file.write(header + data)

def create_pgm_file():
    header = "P2\n# This is a PGM file\n2 2\n255\n"
    data = "255 128\n128 0\n"
    with open('./tmp/sample.pgm', 'w') as file:
        file.write(header + data)

def create_ppm_file():
    header = "P3\n# This is a PPM file\n2 2\n255\n"
    data = "255 0 0\n0 255 0\n0 0 255\n"
    with open('./tmp/sample.ppm', 'w') as file:
        file.write(header + data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

create_pbm_file()
create_pgm_file()
create_ppm_file()