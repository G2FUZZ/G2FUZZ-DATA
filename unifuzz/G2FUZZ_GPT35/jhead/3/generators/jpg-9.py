import numpy as np
from PIL import Image

# Create a random image
width, height = 400, 300
data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Save the image as jpg with quality set to 95
image.save("./tmp/random_image.jpg", quality=95)