import numpy as np
from PIL import Image

# Create a gradient image
width, height = 256, 256
img = np.zeros((height, width, 3), dtype=np.uint8)
for x in range(width):
    img[:, x] = [x, 255 - x, 128]

# Apply gamma correction
gamma = 2.2
img_corrected = (img / 255) ** (1 / gamma) * 255
img_corrected = np.clip(img_corrected, 0, 255).astype(np.uint8)

# Save the image with gamma correction
img_gamma = Image.fromarray(img_corrected)
img_gamma.save('./tmp/gamma_corrected.png')