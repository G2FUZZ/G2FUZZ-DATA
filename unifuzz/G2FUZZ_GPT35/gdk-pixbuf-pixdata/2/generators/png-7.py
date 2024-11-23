import numpy as np
import cv2

# Create a dummy image
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]  # Blue color on the left half
image[:, 50:] = [0, 255, 0]  # Green color on the right half

# Apply gamma correction
gamma = 2.2
corrected_image = np.clip(((image / 255.0) ** (1 / gamma)) * 255, 0, 255).astype(np.uint8)

# Save the corrected image as a PNG file
cv2.imwrite('./tmp/gamma_corrected.png', corrected_image)