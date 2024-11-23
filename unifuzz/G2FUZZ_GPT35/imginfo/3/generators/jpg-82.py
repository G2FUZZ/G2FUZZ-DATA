import numpy as np
from PIL import Image

# Create a 100x100 red image with a green gradient
red_image = np.zeros((100, 100, 3), dtype=np.uint8)
red_image[:, :, 0] = 255  # Set red channel to maximum

# Add a green gradient to the image
green_vals = np.linspace(0, 255, 100, dtype=np.uint8)
red_image[:, :, 1] = green_vals.reshape(100, 1)

# Save the red image with green gradient as a JPEG file
red_image = Image.fromarray(red_image)
red_image.save('./tmp/red_image_with_green_gradient.jpg')