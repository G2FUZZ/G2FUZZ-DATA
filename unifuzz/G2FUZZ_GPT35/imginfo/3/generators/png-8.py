import numpy as np
from PIL import Image

# Create a sample image
image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with different compression levels
compression_levels = [0, 1, 5, 9]
for level in compression_levels:
    image.save(f'./tmp/compressed_image_{level}.png', compress_level=level)