import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image dimensions (e.g., a large image)
width, height = 8000, 8000  # This will create a large file

# Generate an array of random colors
# Using np.uint8 to ensure the array matches the expected byte format for images
image_data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

# Create an image object from the array
image = Image.fromarray(image_data)

# Save the image as a BMP file
file_path = './tmp/large_image.bmp'
image.save(file_path)

print(f"Image saved to {file_path}.")