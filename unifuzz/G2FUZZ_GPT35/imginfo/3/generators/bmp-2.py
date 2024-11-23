import numpy as np
import os

def create_bmp_file(file_path, width, height, image_data):
    # BMP file header
    bmp_header = np.array([66, 77, 54, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0], dtype=np.uint8)

    # BMP file info header
    dib_header = np.array([40, 0, 0, 0, width % 256, width // 256, 0, 0, height % 256, height // 256, 1, 0, 24, 0], dtype=np.uint8)

    # Create the final image array
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    image_array[:, :, 0] = image_data
    image_array[:, :, 1] = image_data
    image_array[:, :, 2] = image_data

    # Write the data to the file
    with open(file_path, 'wb') as file:
        file.write(bmp_header.tobytes())
        file.write(dib_header.tobytes())
        file.write(image_array.tobytes())

# Create a directory to store the BMP files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample BMP file
width = 100
height = 100
image_data = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
create_bmp_file('./tmp/sample.bmp', width, height, image_data)