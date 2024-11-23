import os
import numpy as np
from PIL import Image, PngImagePlugin

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate an example image with more complex patterns and an alpha channel for transparency
width, height = 512, 512  # Increased size for more detail
image_data = np.zeros((height, width, 4), dtype=np.uint8)  # Note the 4th channel for alpha

# Creating a more complex gradient effect with transparency
for y in range(height):
    for x in range(width):
        # Gradient for RGB, varies with x and y to create a visually appealing pattern
        image_data[y, x, 0] = (x % 256)  # Red channel varies with x
        image_data[y, x, 1] = (y % 256)  # Green channel varies with y
        image_data[y, x, 2] = ((x + y) % 256)  # Blue channel is a mix of x and y
        # Alpha channel gradient (transparency), max in the center
        image_data[y, x, 3] = int(255 - np.sqrt((x - width/2)**2 + (y - height/2)**2) % 255)

# Convert the NumPy array to a PIL Image
image = Image.fromarray(image_data)  # Corrected variable name here

# Adding metadata to the PNG
meta = PngImagePlugin.PngInfo()
meta.add_text("Author", "Your Name")
meta.add_text("Description", "A complex PNG with gradients, transparency, and metadata.")

# Save the image including the metadata
image.save("./tmp/complex_filtered_image.png", pnginfo=meta)

# Note: This script explicitly demonstrates adding an alpha channel for transparency and embedding
# metadata within the PNG file. While the PIL library still manages the PNG filters internally during
# the save operation, these additional features showcase more advanced usage of the PNG format.