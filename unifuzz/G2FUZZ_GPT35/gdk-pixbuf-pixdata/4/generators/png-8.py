import numpy as np
import matplotlib.pyplot as plt

# Creating a simple image with gamma correction
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]  # Left side of the image in red
image[:, 50:] = [0, 0, 255]  # Right side of the image in blue

# Applying gamma correction
gamma = 2.2
image_gamma_corrected = (image / 255.0) ** (1 / gamma) * 255
image_gamma_corrected = image_gamma_corrected.astype(np.uint8)

# Saving the image
plt.imsave('./tmp/gamma_corrected_image.png', image_gamma_corrected)