import os

def generate_pbm_file():
    content = "P1\n3 3\n1 0 1\n0 1 0\n1 0 1"
    filename = "./tmp/image.pbm"
    with open(filename, "w") as file:
        file.write(content)

def generate_pgm_file():
    content = "P2\n3 3\n255\n100 150 200\n50 75 100\n25 30 40"
    filename = "./tmp/image.pgm"
    with open(filename, "w") as file:
        file.write(content)

def generate_ppm_file():
    content = "P3\n3 3\n255\n255 0 0 0 255 0 0 0 255\n0 255 0 255 0 0 0 0 255\n0 0 255 255 255 0 255 0 255"
    filename = "./tmp/image.ppm"
    with open(filename, "w") as file:
        file.write(content)

if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

generate_pbm_file()
generate_pgm_file()
generate_ppm_file()