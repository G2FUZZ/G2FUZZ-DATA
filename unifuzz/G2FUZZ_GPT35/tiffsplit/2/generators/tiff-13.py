import numpy as np
import tifffile as tf

# Create a numpy array with the given text
text = "Platform Independence: TIFF files are platform-independent and widely supported across different operating systems and applications."
additional_text = "Image Compression Options: TIFF files offer a range of compression options, including lossless and lossy compression algorithms."
data = np.array([[ord(char) for char in text] + [ord(char) for char in additional_text]])

# Save the numpy array as a TIFF file
filename = './tmp/platform_independence_with_compression.tiff'
tf.imwrite(filename, data)