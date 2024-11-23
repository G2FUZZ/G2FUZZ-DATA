import numpy as np
from PIL import Image

# Create a sample image
image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the original image
image.save('./tmp/original.jpg')

# Lossless rotation (90 degrees clockwise)
rotated_image = image.transpose(Image.ROTATE_90)
rotated_image.save('./tmp/rotated.jpg')