import numpy as np
from PIL import Image

# Create a numpy array with shape (100, 100, 4) for RGBA image
rgba_image = np.zeros((100, 100, 4), dtype=np.uint8)

# Fill the image with some color (e.g., white)
rgba_image[:, :, :3] = 255

# Add alpha channel with transparency values
alpha_channel = np.linspace(0, 255, 100).astype(np.uint8)
rgba_image[:, :, 3] = alpha_channel[:, np.newaxis]

# Create PIL Image from numpy array
image = Image.fromarray(rgba_image)

# Save image as TIFF file
image.save("./tmp/transparent_image.tiff")