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

# Compression Algorithm Customization
# Define the quality of the image, the lower the number the higher the compression
quality = 85  # Adjust the quality here (1-100)

# Define subsampling option to control the tradeoff between quality and file size
# Options are -1, 0, 1, 2; where -1 is default, 0 is 4:4:4 (no subsampling), 
# 1 is 4:2:2, and 2 is 4:2:0
subsampling = -1  # Adjust subsampling here

# Save the image with customized compression
image_file_path = os.path.join(output_dir, '24_bit_color_depth_image_custom_compression.jpg')
image.save(image_file_path, quality=quality, subsampling=subsampling)

print(f'Image with custom compression saved at {image_file_path}')