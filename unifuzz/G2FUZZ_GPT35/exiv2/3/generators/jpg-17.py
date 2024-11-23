import numpy as np
from PIL import Image
import os

# Create a sample image (e.g., a white image)
image = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Save the image as a JPG file with lossy compression
image.save('./tmp/lossy_compression_example.jpg', quality=80)

# Get the file size of the saved image
file_size = os.path.getsize('./tmp/lossy_compression_example.jpg')
print(f"File Size: {file_size} bytes")