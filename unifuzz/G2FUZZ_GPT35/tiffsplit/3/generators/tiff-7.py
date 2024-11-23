import numpy as np
from PIL import Image

# Create a 1-bit TIFF file
data_1bit = np.random.randint(0, 2, size=(100, 100), dtype=np.uint8)  # Generating random 1-bit data
image_1bit = Image.fromarray(data_1bit)
image_1bit.save('./tmp/1bit_tiff.tiff')

# Create a 16-bit TIFF file
data_16bit = np.random.randint(0, 65535, size=(100, 100), dtype=np.uint16)  # Generating random 16-bit data
image_16bit = Image.fromarray(data_16bit)
image_16bit.save('./tmp/16bit_tiff.tiff')