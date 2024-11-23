import numpy as np
import tifffile as tf

# Create a sample image
image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save the image as a TIFF file with 'deflate' compression
tf.imwrite('./tmp/sample_image.tiff', image, compress='deflate')

print("TIFF file with Deflate compression saved successfully.")