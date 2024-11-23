import numpy as np
from PIL import Image

# Create a white image
width, height = 100, 100
data = np.ones((height, width, 3), dtype=np.uint8) * 255
img = Image.fromarray(data, 'RGB')

# Save the image with high compression ratio
img.save("./tmp/high_compression_ratio.jpg", quality=10)