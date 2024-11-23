import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image size and the pattern size
width, height = 400, 400
pattern_height = 20  # Height of each simulated filter pattern

# Create an empty image with a white background
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Apply alternating "filter" patterns
for y in range(0, height, pattern_height * 2):
    # First pattern: A simple gradient
    for i in range(pattern_height):
        if y + i < height:
            image[y + i, :, :] = np.tile(np.linspace(0, 255, width, endpoint=True, dtype=np.uint8)[:, None], (1, 3))
    
    # Second pattern: Solid color blocks to simulate another type of filter effect
    if y + pattern_height < height:
        for i in range(pattern_height):
            image[y + pattern_height + i, :, :] = (i * 5) % 255

# Convert the array to an image
img = Image.fromarray(image)

# Save the image
img.save('./tmp/filter_demo.png')