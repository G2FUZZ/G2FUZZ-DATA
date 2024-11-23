import numpy as np
import tifffile as tf

# Create a numpy array with the given text
text = "Platform Independence: TIFF files are platform-independent and widely supported across different operating systems and applications."
data = np.array([[ord(char) for char in text]])

# Save the numpy array as a TIFF file
filename = './tmp/platform_independence.tiff'
tf.imwrite(filename, data)