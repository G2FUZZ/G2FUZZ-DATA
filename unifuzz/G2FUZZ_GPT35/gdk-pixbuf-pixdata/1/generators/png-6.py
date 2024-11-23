import numpy as np
import matplotlib.pyplot as plt

# Generate a simple image
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]  # Red left side
image[:, 50:] = [0, 0, 255]  # Blue right side

# Apply gamma correction
gamma = 2.2
corrected_image = np.power(image / 255.0, gamma) * 255
corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)

# Display and save the image
plt.imshow(corrected_image)
plt.axis('off')
plt.savefig('./tmp/gamma_corrected_image.png')
plt.show()