import os

def generate_pbm_file():
    content = "P1\n3 3\n0 1 0\n1 0 1\n0 1 0\n"
    with open('./tmp/test_pbm.pbm', 'w') as file:
        file.write(content)

def generate_pgm_file():
    content = "P2\n3 3\n255\n0 127 255\n127 0 127\n0 127 0\n"
    with open('./tmp/test_pgm.pgm', 'w') as file:
        file.write(content)

def generate_ppm_file():
    content = "P3\n3 3\n255\n255 0 0 0 255 0 0 0 255\n0 255 0 255 0 0 0 0 255\n0 0 255 0 0 0 255 0 0\n"
    with open('./tmp/test_ppm.ppm', 'w') as file:
        file.write(content)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pbm_file()
generate_pgm_file()
generate_ppm_file()