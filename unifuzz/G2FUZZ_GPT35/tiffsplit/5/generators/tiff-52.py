import numpy as np
from PIL import Image

# Create a numpy array with the text content
text = "Compatibility: TIFF files are widely supported by image editing software, making them a popular choice for storing high-quality images."
text_array = np.array([ord(char) for char in text], dtype=np.uint8)

# Reshape the array to a 2D shape
height, width = 10, len(text) // 10 + 1
text_array = np.resize(text_array, (height, width))

# Create an image from the numpy array
image = Image.fromarray(text_array)

# Additional complex file features
compression_type = 'tiff_lzw'  # Set compression type to LZW
dpi = (300, 300)  # Set DPI resolution to 300

# Save the image as a TIFF file with compression and DPI settings
image.save("./tmp/compatibility_extended.tiff", compression=compression_type, dpi=dpi)