import os

def generate_complex_pnm_file_extended(filename):
    with open(filename, 'w') as file:
        file.write("P3\n")
        file.write("10 10\n")
        file.write("255\n")
        
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
                  (128, 128, 128), (255, 128, 0), (0, 128, 255), (128, 0, 255)]
        
        for i in range(10):
            for j in range(10):
                color = colors[(i+j)%10]
                file.write(f"{color[0]} {color[1]} {color[2]} ")
            file.write("\n")

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

generate_complex_pnm_file_extended('./tmp/complex_test_extended.pnm')