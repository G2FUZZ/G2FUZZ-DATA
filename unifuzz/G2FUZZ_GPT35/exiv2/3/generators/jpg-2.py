import numpy as np
from PIL import Image

# Create a sample image (e.g., a white image)
image = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Save the image as a JPG file with lossy compression
image.save('./tmp/lossy_compression_example.jpg', quality=80)