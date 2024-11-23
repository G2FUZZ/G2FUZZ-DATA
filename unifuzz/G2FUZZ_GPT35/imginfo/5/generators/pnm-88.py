import os

def generate_complex_pnm_file(file_path, width, height):
    with open(file_path, 'wb') as f:
        f.write(f'P6\n# Complex PNM File: This file contains multiple pixels and color gradients\n{width} {height}\n255\n'.encode())
        
        for y in range(height):
            for x in range(width):
                r = int((x / width) * 255)  # Red component based on x position
                g = int((y / height) * 255)  # Green component based on y position
                b = 128  # Constant blue component

                if x % 2 == 0 and y % 2 == 0:
                    r = 255  # Set red component to max for every other pixel
                elif x % 3 == 0 or y % 3 == 0:
                    g = 255  # Set green component to max for pixels divisible by 3

                f.write(bytes([r, g, b]))

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_path = './tmp/complex_example_extended.pnm'
width = 10
height = 10
generate_complex_pnm_file(file_path, width, height)
print(f'Complex PNM file with extended features generated at: {file_path}')