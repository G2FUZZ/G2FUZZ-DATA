import os

def generate_complex_pnm_file(filename):
    with open(filename, 'w') as file:
        file.write("P3\n")
        file.write("6 6\n")
        file.write("255\n")
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        for i in range(6):
            for j in range(6):
                color = colors[(i+j)%6]
                file.write(f"{color[0]} {color[1]} {color[2]} ")
            file.write("\n")

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

generate_complex_pnm_file('./tmp/complex_test.pnm')