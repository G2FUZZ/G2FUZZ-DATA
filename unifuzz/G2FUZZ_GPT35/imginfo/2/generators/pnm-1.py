import os

def generate_pbm_file(filename):
    with open(filename, 'w') as file:
        file.write("P1\n")
        file.write("4 4\n")
        file.write("0 1 0 1\n")
        file.write("1 0 1 0\n")
        file.write("0 1 0 1\n")
        file.write("1 0 1 0\n")

def generate_pgm_file(filename):
    with open(filename, 'w') as file:
        file.write("P2\n")
        file.write("4 4\n")
        file.write("255\n")
        for _ in range(4):
            file.write("100 150 200 50\n")

def generate_ppm_file(filename):
    with open(filename, 'w') as file:
        file.write("P3\n")
        file.write("4 4\n")
        file.write("255\n")
        for _ in range(4):
            file.write("255 0 0 0 255 0 0 0 255 0 0 0\n")

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

generate_pbm_file('./tmp/test.pbm')
generate_pgm_file('./tmp/test.pgm')
generate_ppm_file('./tmp/test.ppm')