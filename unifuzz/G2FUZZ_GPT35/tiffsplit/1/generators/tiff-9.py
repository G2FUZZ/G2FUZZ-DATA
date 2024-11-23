import numpy as np
import tifffile as tf

# Create a sample image data
image_data = np.random.randint(0, 255, size=(100, 100)).astype(np.uint8)

# Save the image data as a TIFF file with lossless compression
output_file = './tmp/lossless_compression.tiff'
tf.imwrite(output_file, image_data, compress=9)  # Using zlib compression level 9

print(f'TIFF file with lossless compression saved at: {output_file}')