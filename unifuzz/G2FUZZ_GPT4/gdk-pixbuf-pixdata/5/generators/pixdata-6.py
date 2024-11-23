from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA channels (Red, Green, Blue, Alpha for transparency)
width, height = 100, 100
image_data = np.zeros((height, width, 4), dtype=np.uint8)

# Fill the image with a blue color and a gradient alpha channel
for x in range(width):
    for y in range(height):
        # Blue color
        image_data[y, x, 0] = 0    # Red
        image_data[y, x, 1] = 0    # Green
        image_data[y, x, 2] = 255  # Blue
        # Gradient alpha channel
        image_data[y, x, 3] = int(255 * (x / width))

# Create an Image object
image = Image.fromarray(image_data)

# Save the image
image.save('./tmp/alpha_channel_example.pixdata', 'PNG')