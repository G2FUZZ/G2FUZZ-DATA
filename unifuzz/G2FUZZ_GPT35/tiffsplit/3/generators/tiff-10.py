import numpy as np
from PIL import Image

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create alpha channel data (transparency values)
alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Save the image data and alpha channel data as a TIFF file with alpha channel
image_with_alpha = Image.fromarray(np.dstack((image_data, alpha_data)))
image_with_alpha.save('./tmp/alpha_channel.tiff', compression='tiff_deflate', tile=(128, 128))