import numpy as np

def generate_pnm_file(width, height, max_val, pixel_data, file_path):
    with open(file_path, 'w') as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n")
        file.write(f"{max_val}\n")

        for row in pixel_data:
            for pixel in row:
                file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}\n")

width = 100
height = 100
max_val = 255
pixel_data = np.random.randint(0, max_val + 1, size=(height, width, 3))

file_path = "./tmp/generated_image.pnm"
generate_pnm_file(width, height, max_val, pixel_data, file_path)