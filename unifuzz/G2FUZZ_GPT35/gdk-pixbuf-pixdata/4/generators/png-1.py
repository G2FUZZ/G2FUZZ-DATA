import numpy as np
from PIL import Image

# Create a simple numpy array (e.g., an image)
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Convert the numpy array to an image
image = Image.fromarray(image_data)

# Save the image as a PNG file
image.save('./tmp/lossless_compression_example.png')

print("PNG file with lossless compression generated successfully.")