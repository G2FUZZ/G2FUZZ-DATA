import os
import random
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Create a new 100x100 image
width, height = 100, 100
image = Image.new('RGB', (width, height))

# Fill the image with random colors
for x in range(width):
    for y in range(height):
        # Generate a random color
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        image.putpixel((x, y), rand_color)

# Save the image as a BMP file
image.save('./tmp/random_colors.bmp')