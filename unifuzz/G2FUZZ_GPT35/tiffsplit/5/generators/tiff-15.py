import numpy as np
from PIL import Image

# Create a numpy array with the text content
text = "Compatibility: TIFF files are widely supported by image editing software, making them a popular choice for storing high-quality images.\nLayers and Masks: TIFF files can contain layers and masks for advanced editing capabilities in software that supports them."
text_array = np.array([ord(char) for char in text], dtype=np.uint8)

# Reshape the array to a 2D shape
height, width = 10, len(text) // 10 + 1
text_array = np.resize(text_array, (height, width))

# Create an image from the numpy array
image = Image.fromarray(text_array)

# Save the image as a TIFF file
image.save("./tmp/compatibility_with_layers_and_masks.tiff")