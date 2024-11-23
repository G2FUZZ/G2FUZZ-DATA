import numpy as np
from PIL import Image

# Create a random RGB image
width, height = 300, 200
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the original image
image.save('./tmp/original.jpg')

# Perform lossless rotation (90 degrees) and save the rotated image
rotated_image = image.transpose(Image.ROTATE_90)
rotated_image.save('./tmp/rotated.jpg')