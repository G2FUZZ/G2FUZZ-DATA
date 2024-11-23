import numpy as np
from PIL import Image

# Create a 100x100 red image
red_image = np.zeros((100, 100, 3), dtype=np.uint8)
red_image[:, :, 0] = 255  # Set red channel to maximum

# Save the red image as a JPEG file
red_image = Image.fromarray(red_image)
red_image.save('./tmp/red_image.jpg')