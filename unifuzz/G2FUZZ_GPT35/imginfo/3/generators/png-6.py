import numpy as np
import cv2

# Create a simple black image
image = np.zeros((100, 100, 3), dtype=np.uint8)

# Apply gamma correction
gamma = 1.5
corrected_image = np.power(image / 255.0, gamma) * 255.0
corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)

# Save the gamma corrected image
cv2.imwrite('./tmp/gamma_corrected_image.png', corrected_image)