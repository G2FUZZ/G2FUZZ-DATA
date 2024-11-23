import os

def create_pbm_file():
    pbm_content = "P1\n3 2\n1 0 1\n0 1 0"
    with open('./tmp/example.pbm', 'w') as file:
        file.write(pbm_content)

def create_pgm_file():
    pgm_content = "P2\n3 2\n255\n100 150 200\n50 75 125"
    with open('./tmp/example.pgm', 'w') as file:
        file.write(pgm_content)

def create_ppm_file():
    ppm_content = "P3\n3 2\n255\n100 0 0 0 150 0 0 0 200\n0 100 0 0 150 0 0 200 0"
    with open('./tmp/example.ppm', 'w') as file:
        file.write(ppm_content)

os.makedirs('./tmp', exist_ok=True)
create_pbm_file()
create_pgm_file()
create_ppm_file()