import numpy as np
from PIL import Image
import os

# Create a directory for storing the output if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a 24-bit color depth image
# Define image size
width, height = 800, 600

# Generate an array of random colors
# Using a 24-bit color depth means we can have RGB values, each ranging from 0-255
# Thus, we generate a WxHx3 array (for RGB) of random integers between 0 and 255
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image using PIL
image = Image.fromarray(image_data, 'RGB')

# Save the image as JPEG
image_file_path = os.path.join(output_dir, '24_bit_color_image.jpg')
image.save(image_file_path)

print(f"Generated 24-bit color depth image saved at {image_file_path}")