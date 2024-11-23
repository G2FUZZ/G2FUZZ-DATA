import numpy as np
from PIL import Image

# Create a white image
img = np.ones((100, 100, 3), dtype=np.uint8) * 255
img = Image.fromarray(img)

# Save the image with high quality
img.save("./tmp/high_compression_ratio.jpg", quality=95)