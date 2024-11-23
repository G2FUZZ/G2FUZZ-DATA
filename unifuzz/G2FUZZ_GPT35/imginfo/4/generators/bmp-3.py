import numpy as np
import matplotlib.pyplot as plt

# Define image properties
width = 100
height = 100
color_depth = 24  # 24-bit true color

# Generate random image data
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create and save the BMP file
plt.imsave('./tmp/random_image.bmp', image_data)