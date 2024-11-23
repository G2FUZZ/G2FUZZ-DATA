import os
import numpy as np
from PIL import Image, PngImagePlugin

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate an example image to demonstrate the use of more complex file features
width, height = 256, 256
image_data = np.zeros((height, width), dtype=np.uint8)

# Creating a circular gradient effect for a vivid demonstration
center_x, center_y = width // 2, height // 2
for y in range(height):
    for x in range(width):
        # Calculate the distance to the center of the image
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        # Scale the distance to fit within the 256 color range and assign it to the pixel
        image_data[y, x] = int((distance / np.sqrt(center_x**2 + center_y**2)) * 255)

# Apply a custom colormap to the gradient
# This step converts the grayscale image into an RGB image using a colormap
colormap = np.zeros((256, 3), dtype=np.uint8)
for i in range(256):
    colormap[i] = [(255-i), (i // 2), i]
colored_image_data = colormap[image_data]

# Convert the NumPy array to a PIL Image
image = Image.fromarray(colored_image_data, 'RGB')

# Adding metadata to the PNG
meta = PngImagePlugin.PngInfo()
meta.add_text("Author", "Your Name")
meta.add_text("Description", "A custom-generated image with a vivid circular gradient and metadata")

# Save the image
# Note: Pillow automatically selects the best filter for each scanline in the compression process
image.save("./tmp/complex_filtered_image.png", pnginfo=meta)

# Note: While the PIL/Pillow library does not allow direct control over the selection of PNG filters for each scanline,
# this script demonstrates how to enrich PNG files with additional features such as metadata and custom colormaps.