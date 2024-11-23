import os

def generate_pbm_file():
    filename = './tmp/test_pbm.pbm'
    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write("4 4\n")
        f.write("1 0 1 0\n")
        f.write("0 1 0 1\n")
        f.write("1 0 1 0\n")
        f.write("0 1 0 1\n")
    print(f"Generated PBM file: {filename}")

def generate_pgm_file():
    filename = './tmp/test_pgm.pgm'
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write("4 4\n")
        f.write("255\n")
        for i in range(4):
            for j in range(4):
                f.write(f"{i*16+j*16} ")
            f.write("\n")
    print(f"Generated PGM file: {filename}")

def generate_ppm_file():
    filename = './tmp/test_ppm.ppm'
    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write("4 4\n")
        f.write("255\n")
        for i in range(4):
            for j in range(4):
                f.write(f"{i*16} 0 {j*16}\n")
    print(f"Generated PPM file: {filename}")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pbm_file()
generate_pgm_file()
generate_ppm_file()