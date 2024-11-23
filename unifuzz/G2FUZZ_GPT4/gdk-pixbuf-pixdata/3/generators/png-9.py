import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate an example image to demonstrate the use of filters before compression
# For demonstration, we'll generate a simple gradient image
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for demonstration
for y in range(height):
    for x in range(width):
        image_data[y, x] = [x, y, (x+y) % 256]

# Convert the NumPy array to a PIL Image
image = Image.fromarray(image_data)

# Save the image with a specific filter
# PIL supports saving PNGs with different filters through the pnginfo parameter,
# but the exact control over the filter type per scanline is not exposed directly.
# Thus, we demonstrate saving a PNG which internally will use filters to optimize compression.
image.save("./tmp/filtered_image.png")

# Note: This script does not explicitly show setting PNG filters because the PIL library manages
# PNG filters internally during the save operation to optimize the file size.
# The example focuses on generating and saving an image that benefits from PNG's filter algorithms implicitly.