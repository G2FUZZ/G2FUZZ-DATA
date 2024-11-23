import numpy as np
from PIL import Image

# Create a dummy image
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a PNG file with lossless compression
image.save('./tmp/lossless_compression_example.png')