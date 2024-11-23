import numpy as np
from PIL import Image

# Create a random image with color information
width, height = 400, 300
image = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

# Save the image with chroma subsampling
image_pil = Image.fromarray(image)
image_pil.save('./tmp/chroma_subsampling.jpg', subsampling=0)