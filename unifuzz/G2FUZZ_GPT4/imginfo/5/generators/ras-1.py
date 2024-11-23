import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the features of the image file to be generated
width, height = 640, 480
color = (255, 0, 0)  # Red, change as needed

# Create a numpy array with the specified color
data = np.zeros((height, width, 3), dtype=np.uint8)
data[:] = color

# Convert the numpy array to a PIL image
image = Image.fromarray(data)

# Save the image in a supported format (e.g., PNG)
file_path = './tmp/generated_image.png'  # Changed file extension to .png
image.save(file_path, format='PNG')  # Changed format to 'PNG'

print(f'Image saved as {file_path}')