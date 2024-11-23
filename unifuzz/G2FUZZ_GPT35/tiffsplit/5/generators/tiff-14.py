import numpy as np
from PIL import Image

# Create a numpy array with the text content
text = "Compatibility: TIFF files are widely supported by image editing software, making them a popular choice for storing high-quality images."
text_array = np.array([ord(char) for char in text], dtype=np.uint8)

# Reshape the array to a 2D shape
height, width = 10, len(text) // 10 + 1
text_array = np.resize(text_array, (height, width))

# Create an image from the numpy array
image = Image.fromarray(text_array)

# Adding Color Profiles feature
color_profiles = "Color Profiles: TIFF files can embed color profiles to ensure accurate color representation across different devices."
color_profiles_array = np.array([ord(char) for char in color_profiles], dtype=np.uint8)
color_profiles_array = np.resize(color_profiles_array, (height, width))
image.putdata(color_profiles_array.flatten())

# Save the image as a TIFF file
image.save("./tmp/compatibility_with_color_profiles.tiff")