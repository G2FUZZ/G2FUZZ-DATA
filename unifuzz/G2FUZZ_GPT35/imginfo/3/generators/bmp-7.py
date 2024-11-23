import numpy as np
import matplotlib.pyplot as plt

# Create a simple BMP image with a white background
image = np.ones((100, 100, 3)) * 255

# Add text to the image
plt.text(10, 50, "Platform Independence", fontsize=12, color='black')

# Save the image as a BMP file
plt.imsave('./tmp/platform_independence.bmp', image.astype(np.uint8))