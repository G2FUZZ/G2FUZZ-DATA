import numpy as np
import tifffile as tiff

# Generate a random 8-bit depth image
image_8bit = np.random.randint(0, 256, size=(256, 256), dtype=np.uint8)

# Save the image to a TIFF file
tiff.imwrite('./tmp/8bit_image.tiff', image_8bit)