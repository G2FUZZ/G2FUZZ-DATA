import numpy as np
from PIL import Image

# Create a sample image
data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Save the image as a JPEG file
image.save('./tmp/sample.jpg')