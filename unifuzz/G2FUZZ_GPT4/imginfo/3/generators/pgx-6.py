import os
from PIL import Image
import numpy as np

# Create a directory for storing the output if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the image size and create a sample image
image_size = (256, 256)  # Width and height in pixels
image_array = np.zeros((image_size[1], image_size[0]), dtype=np.uint16)

# Filling the image with a gradient for demonstration purposes
for y in range(image_size[1]):
    for x in range(image_size[0]):
        image_array[y, x] = int((x+y) / 2) % 256  # Example pattern, simple gradient

# Convert the numpy array to a PIL image
image = Image.fromarray(image_array)

# Save the image in PNG format
image_path = os.path.join(output_dir, 'example.png')
image.save(image_path, format='PNG')

print(f"PNG file saved at: {image_path}")