import os
import numpy as np
from PIL import Image

# Create a directory for saving the generated bmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample image
width, height = 100, 100
image_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(image_array)

# Save the uncompressed image
image.save('./tmp/uncompressed_image.bmp')

# Save the compressed image
image.save('./tmp/compressed_image.bmp', compression="tiff_lzw")