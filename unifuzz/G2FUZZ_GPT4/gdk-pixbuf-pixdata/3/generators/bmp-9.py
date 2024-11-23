from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with specific features related to "No Data Loss"
# For demonstration, let's create a 100x100 pixel image with a gradient demonstrating high-quality, lossless storage.

# Create a 100x100 image with a horizontal gradient
width, height = 100, 100
image_data = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient from left (black) to right (white)
for x in range(width):
    for y in range(height):
        # Gradient - R, G, and B channels get the same value to create a grayscale image
        value = int((x / (width - 1)) * 255)
        image_data[y, x] = [value, value, value]

# Create the image using PIL
image = Image.fromarray(image_data, 'RGB')

# Save the image as BMP to ensure no data loss
image.save('./tmp/no_data_loss.bmp')