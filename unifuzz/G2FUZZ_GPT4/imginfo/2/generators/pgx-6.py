from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple grayscale image
width, height = 256, 256
image = Image.fromarray(np.uint8(np.linspace(0, 255, width*height).reshape((height, width))))

# Save the image as JPEG 2000 which is compatible with the JPEG 2000 standard
# Note: This is a workaround since direct PGX file generation might not be straightforward in Python
image.save('./tmp/simple_image.jp2', 'JPEG2000')

print("Image saved successfully.")