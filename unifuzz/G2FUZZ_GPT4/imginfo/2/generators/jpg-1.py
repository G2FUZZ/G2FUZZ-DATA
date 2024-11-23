import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image using numpy
# Create a 256x256 pixels image with 3 channels (RGB), with random colors
image_data = np.random.rand(256, 256, 3) * 255
formatted_image_data = image_data.astype('uint8')

# Create an image object
img = Image.fromarray(formatted_image_data)

# Save the image with lossy compression as JPEG
# The compression level can be adjusted with the 'quality' parameter.
# Lower quality values result in higher compression and smaller file size.
img.save('./tmp/random_image.jpg', 'JPEG', quality=85)  # Adjust quality for more or less compression