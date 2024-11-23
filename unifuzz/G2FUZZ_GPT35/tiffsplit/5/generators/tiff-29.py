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

# Add Custom Color Spaces feature
custom_color_space_info = "Custom Color Spaces: TIFF files can support custom color spaces or color models beyond the standard RGB, CMYK, or grayscale, allowing for specialized color representations."
custom_color_space_array = np.array([ord(char) for char in custom_color_space_info], dtype=np.uint8)
custom_color_space_height, custom_color_space_width = 2, len(custom_color_space_info) // 2 + 1
custom_color_space_array = np.resize(custom_color_space_array, (custom_color_space_height, custom_color_space_width))

# Resize the text_array to match the number of columns in custom_color_space_array
text_array = np.resize(text_array, (custom_color_space_height, custom_color_space_width))

# Combine the text array and custom color space array
combined_array = np.vstack((text_array, custom_color_space_array))

# Create an image from the combined array
image_with_custom_color_space = Image.fromarray(combined_array)

# Save the image with custom color space as a TIFF file
image_with_custom_color_space.save("./tmp/compatibility_with_custom_color_space.tiff")