import numpy as np
import matplotlib.pyplot as plt

# Generate a grayscale PNG image
gray_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
plt.imsave('./tmp/gray_image.png', gray_image, cmap='gray')

# Generate an indexed color PNG image
indexed_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
plt.imsave('./tmp/indexed_image.png', indexed_image, cmap='tab10')

# Generate a truecolor with alpha channel PNG image
truecolor_image = np.random.rand(100, 100, 4)
plt.imsave('./tmp/truecolor_image.png', truecolor_image)