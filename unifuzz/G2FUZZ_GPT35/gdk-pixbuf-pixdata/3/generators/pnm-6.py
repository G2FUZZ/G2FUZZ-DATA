import numpy as np

def create_pnm_file(width, height, pixel_values, file_path):
    header = f'P1\n{width} {height}\n'
    data = ' '.join(str(val) for val in pixel_values)
    pnm_data = header + data

    with open(file_path, 'w') as file:
        file.write(pnm_data)

# Generate pixel values for a 4x4 image with binary data (0s and 1s)
pixel_values = np.random.randint(0, 2, size=(4, 4))
pixel_values = pixel_values.flatten()

file_path = './tmp/lossless_compression.pnm'
create_pnm_file(4, 4, pixel_values, file_path)