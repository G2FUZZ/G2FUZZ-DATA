import os
import numpy as np

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the image dimensions and color (RGB)
width, height = 100, 100
color = (0, 255, 0)  # Green

# Create an array representing the image
# Since PNM (PPM for colored images) format in this context, we use RGB model
image_array = np.zeros((height, width, 3), dtype=np.uint8) + color

# Define the path for the output file
output_path = os.path.join(output_dir, 'image.ppm')

# Write the PPM file (P3 format: ASCII encoding)
with open(output_path, 'w') as f:
    f.write(f'P3\n{width} {height}\n255\n')
    for row in image_array:
        for pixel in row:
            f.write(f'{pixel[0]} {pixel[1]} {pixel[2]} ')
        f.write('\n')