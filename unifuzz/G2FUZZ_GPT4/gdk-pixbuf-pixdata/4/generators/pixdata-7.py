import numpy as np
import os
from PIL import Image

# Create a directory for the output if it does not exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image with an alpha channel (RGBA)
width, height = 200, 200
data = np.zeros((height, width, 4), dtype=np.uint8)

# Fill the image with a gradient and varying alpha values
for y in range(height):
    for x in range(width):
        data[y, x] = [255, 105, 180, int(255 * (x / width))]  # Pink color with gradient in alpha

# Create an image object
image = Image.fromarray(data, 'RGBA')

# Save the image
file_path = os.path.join(output_dir, 'pixdata_alpha_channel.png')
image.save(file_path)
print(f'Image with alpha channel saved to {file_path}')