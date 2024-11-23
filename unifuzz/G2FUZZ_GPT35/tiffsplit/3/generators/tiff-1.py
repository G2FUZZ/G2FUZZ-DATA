import numpy as np
import tifffile as tf

# Create a sample image
image = np.random.randint(0, 255, size=(100, 100)).astype(np.uint8)

# Save the image with different compression methods
compression_methods = ['zlib', 'jpeg', None]
for idx, method in enumerate(compression_methods):
    filename = f'./tmp/image_{idx}.tiff'
    tf.imwrite(filename, image, compress=method)