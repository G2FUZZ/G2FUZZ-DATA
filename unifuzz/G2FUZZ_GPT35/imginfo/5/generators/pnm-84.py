import os

def generate_complex_pnm_file(file_path, width, height):
    with open(file_path, 'wb') as f:
        f.write(f'P6\n# Complex PNM File: This file contains multiple pixels and color gradients\n{width} {height}\n255\n'.encode())
        
        for y in range(height):
            for x in range(width):
                r = int((x / width) * 255)  # Red component based on x position
                g = int((y / height) * 255)  # Green component based on y position
                b = 128  # Constant blue component

                f.write(bytes([r, g, b]))

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_path = './tmp/complex_example.pnm'
width = 5
height = 5
generate_complex_pnm_file(file_path, width, height)
print(f'Complex PNM file generated at: {file_path}')