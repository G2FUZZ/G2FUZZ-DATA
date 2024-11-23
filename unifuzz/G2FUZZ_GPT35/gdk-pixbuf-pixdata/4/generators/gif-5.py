import numpy as np
from PIL import Image

# Create a simple image with random pixel values
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image in GIF format with lossless compression
image.save("./tmp/lossless_compression.gif", "GIF")

print("GIF file with lossless compression saved successfully.")