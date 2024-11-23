from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image 256x256 pixels
width, height = 256, 256
image = Image.new(mode="RGB", size=(width, height))

# Create a smooth color transition across the image
for x in range(width):
    for y in range(height):
        # Generating a color gradient
        r = (x + y) % 256  # Red channel will change across both x and y
        g = x % 256  # Green channel will change across x
        b = y % 256  # Blue channel will change across y
        image.putpixel((x, y), (r, g, b))

# Save the image
image_file_path = './tmp/color_gradient.jpg'
image.save(image_file_path, 'JPEG')

print(f"Image saved at {image_file_path}")