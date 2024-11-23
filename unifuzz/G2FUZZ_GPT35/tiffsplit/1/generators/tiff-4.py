import numpy as np
from PIL import Image

# Create a 100x100 RGBA image with random values
data = np.random.randint(0, 255, (100, 100, 4), dtype=np.uint8)
img = Image.fromarray(data, 'RGBA')

# Save the image with alpha channel as a TIFF file
img.save('./tmp/alpha_channel.tiff')