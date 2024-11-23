import numpy as np
from PIL import Image
from tifffile import imwrite

# Define bit depth (e.g., 16-bit per channel for higher precision)
bit_depth = 16

# Generate a random image with specified bit depth
image_data = np.random.randint(0, 2**bit_depth, size=(512, 512), dtype=np.uint16)
image = Image.fromarray(image_data)

# Add metadata to the image
metadata = {'Author': 'John Doe', 'Description': 'Random TIFF Image', 'Date': '2022-09-15'}

# Save the generated image with metadata as a compressed TIFF file
imwrite('./tmp/extended_tiff_example.tiff', image_data, metadata=metadata, compress=6)