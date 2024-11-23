import os

def generate_complex_pnm_file(filename, width, height, channels, max_val):
    with open(filename, 'wb') as file:
        file.write(f'P{channels}\n'.encode())
        file.write(b'# This is a more complex PNM file\n')
        file.write(f'{width} {height}\n'.encode())
        file.write(f'{max_val}\n'.encode())
        
        for h in range(height):
            for w in range(width):
                for c in range(channels):
                    value = int((w / width) * max_val)  # Varying color values based on position
                    file.write(bytes([value]))

print('Generating a more complex PNM file...')
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a more complex PNM file with 5 color channels, 800x600 dimensions, and max color value of 255
generate_complex_pnm_file('./tmp/complex_file.pnm', 800, 600, 5, 255)

print('Complex PNM file generated and saved in ./tmp/')