import numpy as np
from PIL import Image

# Create a 100x100 random image
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image)

# Save the image as a JPG file with compression artifacts
image.save('./tmp/compression_artifacts.jpg')