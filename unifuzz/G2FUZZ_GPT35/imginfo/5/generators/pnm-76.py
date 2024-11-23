import os

def generate_complex_pnm_file(file_path, width, height, pixels):
    with open(file_path, 'wb') as f:
        f.write(f'P6\n# Complex PNM File: This PNM file contains multiple pixels with different colors\n{width} {height}\n255\n'.encode())
        for pixel in pixels:
            for color in pixel:
                f.write(bytes([color]))

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_path = './tmp/complex_example.pnm'
width = 2
height = 2
pixels = [
    [255, 0, 0],  # Red pixel
    [0, 255, 0],  # Green pixel
    [0, 0, 255],  # Blue pixel
    [255, 255, 0],  # Yellow pixel
]

generate_complex_pnm_file(file_path, width, height, pixels)
print(f'Complex PNM file generated at: {file_path}')