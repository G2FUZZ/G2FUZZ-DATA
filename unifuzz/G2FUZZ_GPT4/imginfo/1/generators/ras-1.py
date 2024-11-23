import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image size and color (RGB)
width, height = 100, 100  # Example size
color = (255, 0, 0)  # Red, green, blue (Here, it's red)

# Create an array of the specified color
image_data = np.full((height, width, 3), color, dtype=np.uint8)

# Create an Image object from the array
image = Image.fromarray(image_data)

# Save the image in a widely supported format (e.g., PNG)
file_path = './tmp/example.png'
image.save(file_path, format='PNG')

print(f"Successfully saved bitmap image in PNG format to '{file_path}'")