import numpy as np
import matplotlib.pyplot as plt

# Create a sample image
image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

# Save the image as a BMP file
plt.imsave('./tmp/sample_bmp.bmp', image)