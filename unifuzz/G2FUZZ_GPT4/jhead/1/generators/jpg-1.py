import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 256x256 gradient image
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        image[i, j] = [i, j, 128]  # Example gradient in R and G channels

# Convert the numpy array to a PIL image
img = Image.fromarray(image, 'RGB')

# Save the image with a desired quality level to demonstrate lossy compression
# Lower quality values result in higher compression and more loss of details
img.save('./tmp/gradient_compressed.jpg', 'JPEG', quality=25)  # Adjust the quality as needed

print("Image generated and saved with lossy compression.")