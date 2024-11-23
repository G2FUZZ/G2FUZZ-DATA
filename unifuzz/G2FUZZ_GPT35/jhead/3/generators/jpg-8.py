import numpy as np
from PIL import Image

# Create a sample image
image_data = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as jpg
image.save("./tmp/sample.jpg")