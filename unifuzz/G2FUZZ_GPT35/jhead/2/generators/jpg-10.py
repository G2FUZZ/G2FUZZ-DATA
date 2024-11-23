import numpy as np
from PIL import Image

# Generate a random image
width, height = 256, 256
data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Save the image with chroma subsampling
image.save('./tmp/image_with_chroma_subsampling.jpg', subsampling=0)