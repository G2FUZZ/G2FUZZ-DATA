import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name here

# Generate an image with a smooth color transition
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a smooth gradient for each RGB component
for i in range(height):
    r = i % 256  # Red channel will repeat every 256 rows
    g = (255 * i // height) % 256  # Green channel smoothly transitions over the height
    b = (255 * (height - i - 1) // height) % 256  # Blue channel is the inverse of green
    image[i, :, 0] = r
    image[i, :, 1] = g
    image[i, :, 2] = b

# Create the image with PIL and save as JPG
img = Image.fromarray(image, 'RGB')
img.save('./tmp/gradient_image.jpg')
print("Image saved successfully.")