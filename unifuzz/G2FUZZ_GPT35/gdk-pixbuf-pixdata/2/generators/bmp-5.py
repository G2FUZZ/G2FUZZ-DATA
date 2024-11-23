import numpy as np
import os

# Define the palette colors
palette = np.array([[255, 0, 0],  # Red
                     [0, 255, 0],  # Green
                     [0, 0, 255],  # Blue
                     [255, 255, 0],  # Yellow
                     [0, 255, 255]])  # Cyan

# Create a 10x10 indexed color image
image = np.random.randint(0, 5, (10, 10))

# Create the BMP file
file_header = np.array([66, 77, 54, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0])
dib_header = np.array([40, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
palette_data = palette.flatten()
image_data = image.flatten()

bmp_data = np.concatenate((file_header, dib_header, palette_data, image_data))

# Save the BMP file
output_path = './tmp/palette_example.bmp'
with open(output_path, 'wb') as f:
    bmp_data.astype(np.uint8).tofile(f)

print(f'BMP file saved at: {output_path}')