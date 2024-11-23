import os

def generate_pbm_file():
    content = "P1\n3 2\n1 0 1\n0 1 0"
    with open("./tmp/example.pbm", "w") as file:
        file.write(content)

def generate_pgm_file():
    content = "P2\n3 2\n255\n100 50 150\n200 75 225"
    with open("./tmp/example.pgm", "w") as file:
        file.write(content)

def generate_ppm_file():
    content = "P3\n3 2\n255\n100 50 150 200 75 225 50 100 200\n200 75 225 100 50 150 75 225 100"
    with open("./tmp/example.ppm", "w") as file:
        file.write(content)

if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

generate_pbm_file()
generate_pgm_file()
generate_ppm_file()