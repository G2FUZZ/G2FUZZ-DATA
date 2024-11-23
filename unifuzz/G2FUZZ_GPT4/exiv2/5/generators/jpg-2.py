import os
from PIL import Image
import numpy as np

# Create the ./tmp/ directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with 24-bit color depth
# Set the dimensions of the image
width, height = 800, 600

# Generate an array of random colors
# Each color has three components (R, G, B), each being an 8-bit value (0-255)
# Hence, the total color depth is 24 bits (8 bits for each channel)
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image from the array
image = Image.fromarray(image_data)

# Save the image
image_file_path = os.path.join(output_dir, '24_bit_color_depth_image.jpg')
image.save(image_file_path)

print(f'Image saved at {image_file_path}')