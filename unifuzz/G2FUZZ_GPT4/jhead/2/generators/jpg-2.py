import numpy as np
from PIL import Image
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a JPG file with 24-bit color depth
# Define image size and color depth
width, height = 800, 600
color_depth = 24  # 24-bit color depth

# Generate a random array of pixels
pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image from the array of pixels
image = Image.fromarray(pixels, 'RGB')

# Save the image as a JPG file
image.save('./tmp/random_image.jpg')

print("Image saved in './tmp/random_image.jpg'")