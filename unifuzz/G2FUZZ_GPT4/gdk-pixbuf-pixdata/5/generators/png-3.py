import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate a 48-bit truecolor image (16 bits per channel, RGB)
width, height = 256, 256

# Create an array of shape (height, width, 3). Each color channel can take values from 0 to 65535 (16-bit)
# For demonstration, create a gradient effect for each color channel
x = np.linspace(0, 65535, width)
y = np.linspace(0, 65535, height)
xx, yy = np.meshgrid(x, y)

# Creating a blank array with zeros and then filling in with gradient values for demonstration
img_array = np.zeros((height, width, 3), dtype=np.uint16)

# Fill in the image with gradient values
# Channel 1 (Red): Horizontal Gradient
# Channel 2 (Green): Vertical Gradient
# Channel 3 (Blue): Diagonal Gradient (simple combination of horizontal and vertical for demonstration)
img_array[:, :, 0] = xx.astype(np.uint16)  # Red Channel
img_array[:, :, 1] = yy.astype(np.uint16)  # Green Channel
img_array[:, :, 2] = ((xx + yy) / 2).astype(np.uint16)  # Blue Channel

# Create an Image object from the array
img = Image.fromarray(img_array, mode='I;16')

# Save the image
img.save("./tmp/48_bit_truecolor_with_gradients.png")