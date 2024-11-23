import numpy as np
from PIL import Image

# Define the dimensions of the image
width = 300
height = 200

# Create a blank RGB image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with random RGB values
image[:, :, 0] = np.random.randint(0, 256, (height, width))  # Red channel
image[:, :, 1] = np.random.randint(0, 256, (height, width))  # Green channel
image[:, :, 2] = np.random.randint(0, 256, (height, width))  # Blue channel

# Create a PIL image from the numpy array
image = Image.fromarray(image)

# Save the image to a file
image.save('./tmp/colorful_image.jpg')

print("Image saved successfully.")