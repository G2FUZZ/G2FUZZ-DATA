import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an example image data
# For demonstration, we'll create a simple image with random pixels
width, height = 100, 100
data = np.random.rand(height, width, 3) * 255  # Generate random colors

# Convert the numpy array data to uint8, PIL expects integers
data = data.astype(np.uint8)

# Create an image object
image = Image.fromarray(data)

# Save the image as a PNG file
image.save('./tmp/example.png')