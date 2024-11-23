import numpy as np
from PIL import Image

# Create an array with random pixel values
width, height = 100, 100
pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create PIL image from the pixel array
image = Image.fromarray(pixels)

# Save the image as a JPG file
image.save('./tmp/generated_image.jpg')

# Confirming the editing limitations message
print("Editing limitations: JPG files are lossy, so repeated edits and saves can degrade image quality.")