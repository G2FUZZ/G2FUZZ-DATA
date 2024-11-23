import numpy as np
import matplotlib.pyplot as plt

# Create a simple black image
img = np.zeros((100, 100, 3), dtype=np.uint8)
img.fill(255)  # Set color to white

# Save the image as a BMP file
plt.imsave('./tmp/white_image.bmp', img)