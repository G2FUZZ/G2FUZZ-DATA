import numpy as np
from PIL import Image

# Create a simple TIFF image
data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image = Image.fromarray(data)

# Save the TIFF image to a file
image.save('./tmp/example.tiff')