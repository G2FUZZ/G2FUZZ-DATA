import numpy as np
from PIL import Image

# Generate a random image
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a JPG file with lossy compression
image.save("./tmp/lossy_compression.jpg", quality=95)