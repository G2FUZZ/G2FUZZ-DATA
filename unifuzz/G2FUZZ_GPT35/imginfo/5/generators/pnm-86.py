import os

def generate_complex_pnm_file_extended(file_name, features, width, height):
    with open(file_name, 'w') as f:
        f.write("P3\n")
        f.write("# " + features + "\n")
        f.write(str(width) + " " + str(height) + "\n")
        f.write("255\n")
        
        # Generating a gradient of colors with varying pixel sizes
        for i in range(height):
            for j in range(width):
                red = i * 25 % 255
                green = j * 25 % 255
                blue = (i + j) * 13 % 255
                pixel_size = (i + j) % 3 + 1  # Varying pixel sizes
                for _ in range(pixel_size):
                    for _ in range(pixel_size):
                        f.write("{r} {g} {b}  # Pixel ({x}, {y})\n".format(r=red, g=green, b=blue, x=i, y=j))

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = "./tmp/complex_extended_example.pnm"
features = "Complex Extended File Structure: This file contains a color gradient with varying pixel sizes and custom comments."
width = 15
height = 15
generate_complex_pnm_file_extended(file_name, features, width, height)