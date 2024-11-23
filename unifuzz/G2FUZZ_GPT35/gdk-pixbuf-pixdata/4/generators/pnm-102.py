import os

def generate_complex_pnm_file(filename):
    with open(filename, 'w') as file:
        file.write("# This is a complex PNM file\n")
        file.write("P3\n")
        file.write("5 5\n")
        file.write("255\n")
        for i in range(5):
            for j in range(5):
                file.write(f"{i*50} {j*50} {(i+j)*25}\n")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_complex_pnm_file('./tmp/complex_image.pnm')