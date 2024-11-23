import numpy as np
import matplotlib.pyplot as plt

# Create a BMP image with a color gradient background
x, y = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
image = np.dstack((x, y, np.ones_like(x))) * 255

# Draw a rectangle on the image
plt.fill([20, 80, 80, 20], [20, 20, 80, 80], color='red')

# Add text to the image
plt.text(30, 50, "Complex BMP Image", fontsize=14, color='white')

# Save the image as a BMP file
plt.imsave('./tmp/complex_bmp_image.bmp', image.astype(np.uint8))