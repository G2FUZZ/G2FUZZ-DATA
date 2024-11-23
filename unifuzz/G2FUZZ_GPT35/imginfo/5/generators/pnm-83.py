import os

def generate_complex_pnm_file(file_name, features):
    with open(file_name, 'w') as f:
        f.write("P3\n")
        f.write("# " + features + "\n")
        f.write("10 10\n")
        f.write("255\n")
        
        # Generating a gradient of colors
        for i in range(10):
            for j in range(10):
                red = i * 25
                green = j * 25
                blue = (i + j) * 13 % 255
                f.write("{r} {g} {b}  # Pixel ({x}, {y})\n".format(r=red, g=green, b=blue, x=i, y=j))

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = "./tmp/complex_extended_example.pnm"
features = "Complex Extended File Structure: This file contains a color gradient and pixel coordinates."
generate_complex_pnm_file(file_name, features)