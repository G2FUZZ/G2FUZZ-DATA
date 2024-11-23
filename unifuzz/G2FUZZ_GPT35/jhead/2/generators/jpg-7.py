import numpy as np
from PIL import Image

# Create a sample image
image_width = 400
image_height = 300
image = np.random.randint(0, 255, (image_height, image_width, 3), dtype=np.uint8)

# Save the original image as jpg
original_image_path = './tmp/original.jpg'
Image.fromarray(image).save(original_image_path)

# Perform lossless rotation (90 degrees clockwise) and save the rotated image
rotated_image = np.rot90(image, k=1, axes=(0, 1))
rotated_image_path = './tmp/rotated.jpg'
Image.fromarray(rotated_image).save(rotated_image_path)