import os

def create_complex_pnm_file(filename, width, height, max_val, data):
    with open(filename, 'w') as file:
        file.write("P3\n# Complex PNM file\n{} {}\n{}\n".format(width, height, max_val))
        for line in data:
            file.write(" ".join(map(str, line)) + "\n")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Creating a more complex PNM file with multiple color channels and variable dimensions
width = 4
height = 3
max_val = 255
image_data = [
    [255, 0, 0, 0, 255, 0, 0, 0, 255, 255],
    [0, 255, 0, 255, 0, 255, 0, 255, 0, 255],
    [0, 0, 255, 255, 255, 0, 0, 255, 0, 0]
]
create_complex_pnm_file('./tmp/complex_image.pnm', width, height, max_val, image_data)

print("PNM file with more complex features has been created and saved in './tmp/' directory.")