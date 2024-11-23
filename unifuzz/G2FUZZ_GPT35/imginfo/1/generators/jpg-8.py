import numpy as np
from PIL import Image

# Create a random image
image_array = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_array)

# Save the image as a JPG file with high compression
image.save('./tmp/compression_artifacts.jpg', quality=10)