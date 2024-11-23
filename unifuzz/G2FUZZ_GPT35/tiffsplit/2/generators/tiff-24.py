import numpy as np
import tifffile as tf

# Create a numpy array with the given text
text = "Platform Independence: TIFF files are platform-independent and widely supported across different operating systems and applications."
additional_text = "Image Compression Options: TIFF files offer a range of compression options, including lossless and lossy compression algorithms."
image_editing_history = "Image Editing History: TIFF files can store information about the editing history of the image, allowing for non-destructive editing workflows."
data = np.array([[ord(char) for char in text] + [ord(char) for char in additional_text] + [ord(char) for char in image_editing_history]])

# Save the numpy array as a TIFF file
filename = './tmp/platform_independence_with_compression_and_editing_history.tiff'
tf.imwrite(filename, data)