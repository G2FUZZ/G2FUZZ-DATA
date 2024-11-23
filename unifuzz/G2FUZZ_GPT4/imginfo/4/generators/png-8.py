from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with a horizontal gradient
width, height = 256, 256
image = Image.new('RGB', (width, height))
pixels = image.load()

for x in range(image.width):
    for y in range(image.height):
        # Simple gradient: The intensity of the red channel increases with x
        pixels[x, y] = (x, 120, 155)  # RGB

# Before saving, let's apply a simple "filter" to demonstrate the concept.
# Note: This is a conceptual demonstration, not an actual PNG filter implementation.
filtered_image = np.array(image)
for x in range(1, width):
    for y in range(height):
        # Simple filter: Subtract the value of the previous pixel from the current pixel
        # This mimics the PNG Sub filter on a very basic level for the red channel
        filtered_image[y, x, 0] = (filtered_image[y, x, 0] - filtered_image[y, x-1, 0]) % 256

# Convert the numpy array back to an image
image_with_filter = Image.fromarray(filtered_image.astype('uint8'))

# Save the original and filtered images
image.save('./tmp/original_image.png')
image_with_filter.save('./tmp/filtered_image.png')