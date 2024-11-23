import numpy as np
from PIL import Image

# Create a random image data with 8-bit depth
data = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
image = Image.fromarray(data)

# Save the image as a TIFF file with 8-bit depth
image.save("./tmp/8bit_depth.tiff")

# Create a random image data with 32-bit depth (float)
data_float = np.random.rand(256, 256).astype(np.float32)
image_float = Image.fromarray(data_float)

# Save the image as a TIFF file with 32-bit depth
image_float.save("./tmp/32bit_depth.tiff")