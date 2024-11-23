import os
import numpy as np

def generate_extended_pnm_file(file_path, width, height, max_pixel_value, num_images=1, comments=None):
    pixel_depth = 8

    if comments is None:
        comments = [
            "Extended PNM file with multiple images and comments",
            "Created using Python and numpy"
        ]

    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    for i in range(num_images):
        header = f'P3\n{width} {height}\n{max_pixel_value}\n'

        pixels = ''
        for i in range(height):
            row = ''
            for j in range(width):
                pixel_value = (i + j) % max_pixel_value  # Just an example of pixel value calculation
                row += f'{pixel_value} {pixel_value} {pixel_value} '
            pixels += row.strip() + '\n'

        with open(file_path + f'_{i}.pnm', 'w') as file:
            file.write(header)
            for comment in comments:
                file.write(f'# {comment}\n')
            file.write(pixels)

file_path = './tmp/extended_sample'
width = 10
height = 10
max_pixel_value = 255
generate_extended_pnm_file(file_path, width, height, max_pixel_value, num_images=3)