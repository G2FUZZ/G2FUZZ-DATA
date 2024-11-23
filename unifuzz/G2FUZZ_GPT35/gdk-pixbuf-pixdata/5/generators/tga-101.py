import numpy as np
import struct

def generate_complex_tga_file(file_name):
    width = 640
    height = 480
    image_data = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)

    color_map = np.random.randint(0, 256, size=(256, 3), dtype=np.uint8)
    gamma_correction = np.random.uniform(0.5, 2.0)

    with open(file_name, 'wb') as f:
        f.write(b'\x00\x00\x02')  # Image type - color-mapped image
        f.write(b'\x00\x00\x01')  # Color map type - no color map included
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')  # Image specification - no color map
        f.write(color_map.tobytes())  # Color map data
        f.write(struct.pack('f', gamma_correction))  # Gamma correction value

        # Add image data
        for y in range(height):
            for x in range(width):
                f.write(bytes(image_data[y, x]))

# Generate a sample TGA file with more complex file structures
file_name = './tmp/sample_complex_tga.tga'
generate_complex_tga_file(file_name)
print(f'TGA file with more complex file structures generated: {file_name}')