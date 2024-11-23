import os

def generate_pnm_file(file_path, width, height, max_value, pixel_values):
    with open(file_path, 'w') as file:
        file.write(f'P3\n{width} {height}\n{max_value}\n')
        for row in pixel_values:
            for pixel in row:
                file.write(' '.join(map(str, pixel)) + '\n')

def save_pnm_files():
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Define pixel values for the PNM file
    width = 3
    height = 2
    max_value = 255
    pixel_values = [
        [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
        [(255, 255, 0), (255, 0, 255), (0, 255, 255)]
    ]
    
    generate_pnm_file('./tmp/image1.pnm', width, height, max_value, pixel_values)
    generate_pnm_file('./tmp/image2.pnm', width, height, max_value, pixel_values)

save_pnm_files()